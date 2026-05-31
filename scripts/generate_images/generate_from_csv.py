#!/usr/bin/env python3
"""Generate ad images from white-background product images listed in a CSV.

This script intentionally uses only Python's standard library. It downloads the
source image URL from `creative_id_image`, fills a prompt template with row
metadata, sends the image plus prompt to the OpenAI Images Edit API, and writes
generated images to `outputs/`.
"""

from __future__ import annotations

import argparse
import base64
import csv
from dataclasses import dataclass
import json
import mimetypes
import os
import pathlib
import random
import re
import sys
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Iterable


REQUIRED_COLUMNS = [
    "id",
    "material_id",
    "ori_title",
    "creative_id_image",
    "creative_id_brand",
    "creative_id_price",
    "creative_id_promotion",
    "level_one_category_name",
    "is_white_image",
]

LEGACY_CANONICAL_ORIENTATIONS = ["Product-oriented", "Context-oriented", "Symbolic-oriented"]
V3_CANONICAL_ORIENTATIONS = ["Product-oriented", "Symbolic-oriented", "Experiential-oriented"]
ORIENTATION_ALIASES = {"Affect-oriented": "Symbolic-oriented"}
V3_ORIENTATION_ALIASES = {
    "Affect-oriented": "Symbolic-oriented",
    "Context-oriented": "Experiential-oriented",
}
ORIENTATION_CHOICES = sorted(
    set(LEGACY_CANONICAL_ORIENTATIONS + V3_CANONICAL_ORIENTATIONS + list(ORIENTATION_ALIASES) + list(V3_ORIENTATION_ALIASES))
)
IMAGE_TYPE_ALIASES = {
    "product": "Product-oriented",
    "product-oriented": "Product-oriented",
    "function": "Product-oriented",
    "functional": "Product-oriented",
    "context": "Context-oriented",
    "context-oriented": "Context-oriented",
    "usage": "Context-oriented",
    "symbolic": "Symbolic-oriented",
    "symbolic-oriented": "Symbolic-oriented",
    "symbol": "Symbolic-oriented",
    "experience": "Experiential-oriented",
    "experiential": "Experiential-oriented",
    "experiential-oriented": "Experiential-oriented",
}
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_API_BASE_URL = "https://api.vectorengine.cn/v1"
DEFAULT_IMAGES_EDIT_PATH = "/images/edits"
DEFAULT_CHAT_COMPLETIONS_PATH = "/chat/completions"
DEFAULT_BASE_PROMPT_MODEL = "gpt-4o-mini"
DEFAULT_BASE_PROMPT_FILES = {
    "v15": "prompts/neutral_product_ad_image_prompt.v15.txt",
    "v16": "prompts/neutral_product_ad_image_prompt.v16.txt",
    "v17": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt_generator.v17.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt_generator.v17.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt_generator.v17.txt",
    },
}
DEFAULT_RANDOM_SEED = 20260523
DEFAULT_SELECTION_MODE = "previous-random10"
DEFAULT_PROMPT_VERSION = "current"
GENERATED_BASE_PROMPT_PLACEHOLDERS = {
    "v15": "[v15 dry-run：正式运行时会先根据商品元数据和白底源图生成这里的商品专属中性 prompt。]",
    "v16": "[v16 dry-run: in a real run, this section will be generated from product metadata and the white-background source image.]",
    "v17": "[v17 dry-run: in a real run, this section will be an orientation-specific image prompt generated from product metadata, the source image, and the target brand-concept orientation.]",
}
DEFAULT_PREVIOUS_SAMPLE_IDS = [
    "79469",
    "1562371",
    "1241251",
    "103728",
    "1235091",
    "1557798",
    "1544158",
    "1251674",
    "28257",
    "104207",
]
DEFAULT_ORIENTATION_PROMPT_FILES = {
    "Product-oriented": "prompts/product_oriented_ad_image_prompt.txt",
    "Context-oriented": "prompts/context_oriented_ad_image_prompt.txt",
    "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.txt",
}
PROMPT_VERSION_FILES = {
    "current": DEFAULT_ORIENTATION_PROMPT_FILES,
    "function_v2": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.function_v2.txt",
        "Context-oriented": "prompts/context_oriented_ad_image_prompt.function_v2.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.function_v2.txt",
    },
    "v3": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v3.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v3.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v3.txt",
    },
    "v4": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v4.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v4.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v4.txt",
    },
    "v5": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v5.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v5.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v5.txt",
    },
    "v6": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v6.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v6.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v6.txt",
    },
    "v7": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v7.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v7.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v7.txt",
    },
    "v8": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v8.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v8.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v8.txt",
    },
    "v9": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v9.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v9.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v9.txt",
    },
    "v10": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v10.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v10.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v10.txt",
    },
    "v11": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v11.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v11.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v11.txt",
    },
    "v12": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v12.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v12.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v12.txt",
    },
    "v13": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v13.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v13.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v13.txt",
    },
    "v14": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v14.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v14.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v14.txt",
    },
    "v15": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v15.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v15.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v15.txt",
    },
    "v16": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v16.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v16.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v16.txt",
    },
    "v17": {
        "Product-oriented": "prompts/product_oriented_ad_image_prompt.v17.txt",
        "Symbolic-oriented": "prompts/symbolic_oriented_ad_image_prompt.v17.txt",
        "Experiential-oriented": "prompts/experiential_oriented_ad_image_prompt.v17.txt",
    },
}
PARK_PROMPT_VERSIONS = frozenset(
    {"v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11", "v12", "v13", "v14", "v15", "v16", "v17"}
)
GENERATED_BASE_PROMPT_VERSIONS = frozenset({"v15", "v16", "v17"})
ORIENTATION_SPECIFIC_GENERATED_PROMPT_VERSIONS = frozenset({"v17"})


@dataclass(frozen=True)
class OrientationPlan:
    requested_orientation: str
    orientation: str
    prompt_template: str
    prompt_source: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate ad images from white-background product-image CSV rows.",
    )
    parser.add_argument(
        "--csv",
        default="data/experiment/white_bg_product_catalog_experiment.csv",
        help="Input CSV path.",
    )
    parser.add_argument(
        "--prompt-file",
        default=None,
        help="Prompt template path. If omitted, the orientation-specific default prompt is used.",
    )
    parser.add_argument(
        "--prompt",
        default=None,
        help="Inline prompt template. Overrides --prompt-file when provided.",
    )
    parser.add_argument(
        "--orientation",
        default=None,
        choices=ORIENTATION_CHOICES,
        help=(
            "Single creative orientation. Overrides --orientations. Affect-oriented is a deprecated alias for "
            "Symbolic-oriented; under --prompt-version v3/v4/v5/v6/v7/v8/v9/v10/v11/v12/v13/v14/v15/v16/v17, "
            "Context-oriented is a deprecated alias for Experiential-oriented."
        ),
    )
    parser.add_argument(
        "--image-type",
        default=None,
        help="Short alias for generating one type only: product/function, context/usage, symbolic, or experiential.",
    )
    parser.add_argument(
        "--orientations",
        default="all",
        help="Comma-separated orientations to generate, or 'all'. Defaults to all three canonical orientations.",
    )
    parser.add_argument(
        "--prompt-version",
        default=os.environ.get("GENAI_AD_IMAGE_PROMPT_VERSION", DEFAULT_PROMPT_VERSION),
        choices=sorted(PROMPT_VERSION_FILES),
        help=(
            "Prompt set to use. Defaults to current; function_v2 keeps Product-oriented more function-focused; "
            "v3/v4/v5/v6/v7/v8/v9/v10/v11/v12/v13/v14/v15/v16/v17 use Park et al. functional/symbolic/experiential brand concepts."
        ),
    )
    parser.add_argument(
        "--run-dir",
        default=None,
        help=(
            "Run root directory. Supports {model}, {selection_label}, {orientation_label}, "
            "{prompt_version}, and {timestamp}. Defaults to "
            "outputs/{model}_{selection_label}_{orientation_label}_{timestamp}."
        ),
    )
    parser.add_argument(
        "--timestamp",
        default=None,
        help="Timestamp suffix for default run directories. Defaults to current YYYYMMDD_HHMMSS.",
    )
    parser.add_argument(
        "--no-timestamp",
        action="store_true",
        help="Do not append a timestamp to the default run directory.",
    )
    parser.add_argument("--output-dir", default=None, help="Generated image directory. Defaults to {run-dir}/generated.")
    parser.add_argument("--source-dir", default=None, help="Downloaded source image directory. Defaults to {run-dir}/source_images.")
    parser.add_argument("--manifest", default=None, help="JSONL manifest path. Defaults to {run-dir}/generation_manifest.jsonl.")
    parser.add_argument("--model", default=os.environ.get("OPENAI_IMAGE_MODEL", DEFAULT_MODEL), help="Image model.")
    parser.add_argument(
        "--api-base-url",
        default=os.environ.get("OPENAI_API_BASE") or os.environ.get("OPENAI_BASE_URL") or DEFAULT_API_BASE_URL,
        help="OpenAI-compatible API base URL. Defaults to the configured VectorEngine base URL.",
    )
    parser.add_argument(
        "--endpoint",
        default=os.environ.get("OPENAI_IMAGES_EDIT_ENDPOINT"),
        help="Images edit endpoint. If omitted, {api-base-url}/images/edits is used.",
    )
    parser.add_argument(
        "--base-prompt-file",
        default=os.environ.get("GENAI_AD_IMAGE_BASE_PROMPT_FILE"),
        help="Product prompt-generation template used by v15/v16/v17 before image generation.",
    )
    parser.add_argument(
        "--base-prompt-model",
        default=os.environ.get("OPENAI_BASE_PROMPT_MODEL") or os.environ.get("OPENAI_TEXT_MODEL") or DEFAULT_BASE_PROMPT_MODEL,
        help="Text/vision model used by v15/v16/v17 to generate the product prompt.",
    )
    parser.add_argument(
        "--base-prompt-endpoint",
        default=os.environ.get("OPENAI_CHAT_COMPLETIONS_ENDPOINT") or os.environ.get("OPENAI_BASE_PROMPT_ENDPOINT"),
        help="Chat completions endpoint for v15/v16/v17 prompt generation. If omitted, {api-base-url}/chat/completions is used.",
    )
    parser.add_argument(
        "--base-prompt-dir",
        default=None,
        help="Directory for saved v15/v16/v17 generated product prompts. Defaults to {run-dir}/base_prompts.",
    )
    parser.add_argument(
        "--base-prompt-max-tokens",
        type=int,
        default=int(os.environ.get("GENAI_AD_IMAGE_BASE_PROMPT_MAX_TOKENS", "700")),
        help="Maximum output tokens for v15/v16/v17 prompt generation.",
    )
    parser.add_argument(
        "--base-prompt-temperature",
        type=float,
        default=float(os.environ.get("GENAI_AD_IMAGE_BASE_PROMPT_TEMPERATURE", "0.2")),
        help="Temperature for v15/v16/v17 prompt generation.",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Runtime API key. Prefer OPENAI_API_KEY when you do not want the key in shell history.",
    )
    parser.add_argument("--size", default="1024x1024", help="Output size, e.g. 1024x1024, 1024x1536, 1536x1024.")
    parser.add_argument("--quality", default="medium", help="Model quality option, e.g. low, medium, high, auto.")
    parser.add_argument("--output-format", default="png", choices=["png", "jpeg", "webp"], help="Generated image format.")
    parser.add_argument("--n", type=int, default=1, help="Images to generate per row.")
    parser.add_argument(
        "--selection-mode",
        choices=["previous-random10", "sequential", "random"],
        default=DEFAULT_SELECTION_MODE,
        help="Row selection mode. Defaults to the previous fixed random-10 sample.",
    )
    parser.add_argument("--limit", type=int, default=None, help="Maximum rows to process. Sequential mode defaults to 1.")
    parser.add_argument("--start", type=int, default=0, help="Number of matching rows to skip before processing.")
    parser.add_argument("--sample-size", type=int, default=None, help="Randomly sample this many rows after filtering.")
    parser.add_argument(
        "--random-seed",
        type=int,
        default=int(os.environ.get("GENAI_AD_IMAGE_RANDOM_SEED", DEFAULT_RANDOM_SEED)),
        help=f"Random seed for --sample-size. Defaults to {DEFAULT_RANDOM_SEED}.",
    )
    parser.add_argument("--ids", default=None, help="Comma-separated product ids to process. Overrides --start filtering order.")
    parser.add_argument("--only-white", action="store_true", default=True, help="Only process rows where is_white_image == 1.")
    parser.add_argument("--include-non-white", dest="only_white", action="store_false", help="Allow rows where is_white_image != 1.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate outputs even if files already exist.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned requests without downloading images or calling the API.")
    parser.add_argument("--download-only", action="store_true", help="Download source images and render prompts, but do not call the API.")
    parser.add_argument("--sleep", type=float, default=0.0, help="Seconds to sleep between API calls.")
    parser.add_argument("--retries", type=int, default=2, help="Retry count for image download and API calls.")
    parser.add_argument("--timeout", type=int, default=120, help="HTTP timeout seconds.")
    parser.add_argument("--no-progress", action="store_true", help="Disable progress bar and ETA output.")
    return parser.parse_args()


def read_rows(csv_path: pathlib.Path) -> list[dict[str, str]]:
    with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        missing = [column for column in REQUIRED_COLUMNS if column not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Missing required CSV columns: {', '.join(missing)}")
        return list(reader)


def effective_selection_mode(args: argparse.Namespace) -> str:
    if args.ids:
        return "ids"
    if args.sample_size is not None and args.selection_mode == DEFAULT_SELECTION_MODE:
        return "random"
    return args.selection_mode


def select_rows(rows: list[dict[str, str]], args: argparse.Namespace) -> list[dict[str, str]]:
    selected = rows
    if args.only_white:
        selected = [row for row in selected if str(row.get("is_white_image", "")).strip() == "1"]

    if args.ids:
        wanted = [item.strip() for item in args.ids.split(",") if item.strip()]
        by_id = {row.get("id"): row for row in selected}
        selected = [by_id[item] for item in wanted if item in by_id]
        if args.limit is not None and args.limit >= 0:
            selected = selected[: args.limit]
        return selected

    mode = effective_selection_mode(args)
    if mode == "previous-random10":
        by_id = {row.get("id"): row for row in selected}
        selected = [by_id[item] for item in DEFAULT_PREVIOUS_SAMPLE_IDS if item in by_id]
        if args.limit is not None and args.limit >= 0:
            selected = selected[: args.limit]
        return selected

    if mode == "random":
        selected = selected[args.start :]
        sample_size = args.sample_size
        if sample_size is None:
            sample_size = args.limit if args.limit is not None else len(DEFAULT_PREVIOUS_SAMPLE_IDS)
        if sample_size < 0:
            raise ValueError("--sample-size must be non-negative.")
        sample_size = min(sample_size, len(selected))
        selected = random.Random(args.random_seed).sample(selected, sample_size)
        return selected

    selected = selected[args.start :]
    if args.limit is None:
        selected = selected[:1]
    elif args.limit >= 0:
        selected = selected[: args.limit]
    return selected


def split_csv_values(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def normalize_image_type(image_type: str) -> str:
    normalized = image_type.strip().lower()
    if normalized not in IMAGE_TYPE_ALIASES:
        allowed = ", ".join(sorted(IMAGE_TYPE_ALIASES))
        raise ValueError(f"Unsupported --image-type {image_type!r}. Use one of: {allowed}")
    return IMAGE_TYPE_ALIASES[normalized]


def canonical_orientations_for_version(prompt_version: str) -> list[str]:
    if prompt_version in PARK_PROMPT_VERSIONS:
        return V3_CANONICAL_ORIENTATIONS
    return LEGACY_CANONICAL_ORIENTATIONS


def orientation_aliases_for_version(prompt_version: str) -> dict[str, str]:
    if prompt_version in PARK_PROMPT_VERSIONS:
        return V3_ORIENTATION_ALIASES
    return ORIENTATION_ALIASES


def resolve_orientation_names(args: argparse.Namespace) -> list[tuple[str, str]]:
    if args.image_type and args.orientation:
        raise ValueError("Use either --image-type or --orientation, not both.")
    canonical_orientations = canonical_orientations_for_version(args.prompt_version)
    if args.image_type:
        requested = [normalize_image_type(args.image_type)]
    elif args.orientation:
        requested = [args.orientation]
    elif str(args.orientations).strip().lower() in {"all", "three", "three-orientations"}:
        requested = canonical_orientations
    else:
        requested = split_csv_values(args.orientations)

    if not requested:
        raise ValueError("No orientations selected.")

    resolved: list[tuple[str, str]] = []
    seen: set[str] = set()
    for item in requested:
        canonical = canonical_orientation(item, args.prompt_version)
        if canonical not in canonical_orientations:
            allowed = ", ".join(canonical_orientations)
            aliases = ", ".join(sorted(orientation_aliases_for_version(args.prompt_version)))
            alias_hint = f" Deprecated aliases accepted for this version: {aliases}." if aliases else ""
            raise ValueError(f"Unsupported orientation {item!r} for prompt version {args.prompt_version!r}. Use one of: {allowed}.{alias_hint}")
        if canonical in seen:
            continue
        resolved.append((item, canonical))
        seen.add(canonical)
    return resolved


def load_prompt_template(args: argparse.Namespace, orientation: str) -> tuple[str, str]:
    if args.prompt:
        return args.prompt, "<inline>"
    prompt_files = PROMPT_VERSION_FILES[args.prompt_version]
    prompt_file = args.prompt_file or prompt_files[orientation]
    prompt_path = pathlib.Path(prompt_file)
    return prompt_path.read_text(encoding="utf-8"), str(prompt_path)


def resolve_orientation_plans(args: argparse.Namespace) -> list[OrientationPlan]:
    plans = []
    for requested, orientation in resolve_orientation_names(args):
        template, prompt_source = load_prompt_template(args, orientation)
        plans.append(
            OrientationPlan(
                requested_orientation=requested,
                orientation=orientation,
                prompt_template=template,
                prompt_source=prompt_source,
            )
        )
    return plans


def canonical_orientation(orientation: str, prompt_version: str) -> str:
    return orientation_aliases_for_version(prompt_version).get(orientation, orientation)


def render_prompt(
    template: str,
    row: dict[str, str],
    orientation: str,
    extra_values: dict[str, str] | None = None,
) -> str:
    values = {key: clean_value(value) for key, value in row.items()}
    values["orientation"] = orientation
    if extra_values:
        values.update({key: "" if value is None else str(value) for key, value in extra_values.items()})
    return template.format_map(DefaultDict(values))


class DefaultDict(dict):
    def __missing__(self, key: str) -> str:
        return ""


def clean_value(value: str | None) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def safe_name(value: str, max_len: int = 80) -> str:
    value = value.strip() or "unknown"
    value = re.sub(r"[^\w.-]+", "_", value, flags=re.UNICODE)
    return value[:max_len].strip("_") or "unknown"


def endpoint_from_base_url(base_url: str) -> str:
    return f"{base_url.rstrip('/')}{DEFAULT_IMAGES_EDIT_PATH}"


def chat_endpoint_from_base_url(base_url: str) -> str:
    return f"{base_url.rstrip('/')}{DEFAULT_CHAT_COMPLETIONS_PATH}"


def uses_generated_base_prompt(prompt_version: str) -> bool:
    return prompt_version in GENERATED_BASE_PROMPT_VERSIONS


def uses_orientation_specific_generated_prompt(prompt_version: str) -> bool:
    return prompt_version in ORIENTATION_SPECIFIC_GENERATED_PROMPT_VERSIONS


def generated_base_prompt_placeholder(prompt_version: str) -> str:
    return GENERATED_BASE_PROMPT_PLACEHOLDERS.get(prompt_version, "[dry-run: generated neutral product prompt placeholder.]")


def generated_prompt_template_field(prompt_version: str) -> str:
    if uses_orientation_specific_generated_prompt(prompt_version):
        return "generated_orientation_prompt"
    return "neutral_product_prompt"


def orientation_label(plans: list[OrientationPlan]) -> str:
    orientations = [plan.orientation for plan in plans]
    if orientations in (LEGACY_CANONICAL_ORIENTATIONS, V3_CANONICAL_ORIENTATIONS):
        return "three_orientations"
    if len(orientations) == 1:
        return safe_name(orientations[0].lower().replace("-", "_"))
    return f"{len(orientations)}_orientations"


def selection_label(args: argparse.Namespace, selected_rows: list[dict[str, str]]) -> str:
    mode = effective_selection_mode(args)
    if mode == "ids":
        return f"ids{len(selected_rows)}"
    if mode == "previous-random10":
        return f"random{len(selected_rows)}_seed{DEFAULT_RANDOM_SEED}"
    if mode == "random":
        return f"random{len(selected_rows)}_seed{args.random_seed}"
    if args.limit is None:
        return f"sequential{len(selected_rows)}_start{args.start}"
    return f"sequential{len(selected_rows)}_start{args.start}"


def resolve_output_paths(
    args: argparse.Namespace,
    selected_rows: list[dict[str, str]],
    plans: list[OrientationPlan],
) -> None:
    timestamp = args.timestamp or time.strftime("%Y%m%d_%H%M%S")
    values = {
        "model": safe_name(args.model),
        "selection_label": selection_label(args, selected_rows),
        "orientation_label": orientation_label(plans),
        "prompt_version": safe_name(args.prompt_version),
        "timestamp": "" if args.no_timestamp else timestamp,
    }
    if args.run_dir:
        run_dir = pathlib.Path(args.run_dir.format_map(DefaultDict(values)))
    else:
        run_name = f"{values['model']}_{values['selection_label']}_{values['orientation_label']}"
        if args.prompt_version != DEFAULT_PROMPT_VERSION:
            run_name = f"{run_name}_{values['prompt_version']}"
        if not args.no_timestamp:
            run_name = f"{run_name}_{timestamp}"
        run_dir = pathlib.Path("outputs") / run_name

    args.timestamp = timestamp
    args.run_dir = str(run_dir)
    args.output_dir = args.output_dir or str(run_dir / "generated")
    args.source_dir = args.source_dir or str(run_dir / "source_images")
    args.manifest = args.manifest or str(run_dir / "generation_manifest.jsonl")
    args.endpoint = args.endpoint or endpoint_from_base_url(args.api_base_url)
    args.base_prompt_endpoint = args.base_prompt_endpoint or chat_endpoint_from_base_url(args.api_base_url)
    args.base_prompt_dir = args.base_prompt_dir or str(run_dir / "base_prompts")


def expected_output_paths(output_prefix: pathlib.Path, output_format: str, n: int) -> list[pathlib.Path]:
    if n > 1:
        return [
            output_prefix.with_name(f"{output_prefix.name}_{index + 1}.{output_format}")
            for index in range(n)
        ]
    return [output_prefix.with_suffix(f".{output_format}")]


def format_duration(seconds: float | None) -> str:
    if seconds is None:
        return "--:--"
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


class ProgressTracker:
    def __init__(self, total: int, enabled: bool = True) -> None:
        self.total = max(total, 1)
        self.enabled = enabled
        self.done = 0
        self.started_at = time.monotonic()
        self.last_line_len = 0
        self.stream = sys.stderr
        self.is_tty = self.stream.isatty()

    def advance(self, status: str, label: str) -> None:
        self.done += 1
        if not self.enabled:
            return

        elapsed = time.monotonic() - self.started_at
        rate = self.done / elapsed if elapsed > 0 else 0
        eta = (self.total - self.done) / rate if rate > 0 else None
        fraction = min(self.done / self.total, 1)
        bar_width = 24
        filled = int(bar_width * fraction)
        bar = "#" * filled + "-" * (bar_width - filled)
        line = (
            f"[{bar}] {self.done}/{self.total} {fraction * 100:5.1f}% "
            f"elapsed {format_duration(elapsed)} eta {format_duration(eta)} "
            f"{status} {label}"
        )

        if self.is_tty:
            self.stream.write("\r" + line.ljust(self.last_line_len))
            self.last_line_len = len(line)
            if self.done >= self.total:
                self.stream.write("\n")
        else:
            self.stream.write(line + "\n")
        self.stream.flush()


def extension_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    suffix = pathlib.Path(path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return suffix
    return ".jpg"


def download_image(url: str, output_path: pathlib.Path, timeout: int, retries: int) -> pathlib.Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists() and output_path.stat().st_size > 0:
        return output_path

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; genai-ad-image-research/1.0)",
    }
    request = urllib.request.Request(url, headers=headers)
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = response.read()
            if not data:
                raise RuntimeError("Downloaded image is empty.")
            output_path.write_bytes(data)
            return output_path
        except Exception as exc:  # noqa: BLE001 - surface exact failure in manifest.
            last_error = exc
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
    raise RuntimeError(f"Failed to download image after {retries + 1} attempts: {last_error}")


def encode_multipart(fields: dict[str, str], files: list[tuple[str, pathlib.Path]]) -> tuple[bytes, str]:
    boundary = f"----genai-ad-image-{uuid.uuid4().hex}"
    body = bytearray()

    for name, value in fields.items():
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
        body.extend(str(value).encode("utf-8"))
        body.extend(b"\r\n")

    for field_name, file_path in files:
        mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
        body.extend(f"--{boundary}\r\n".encode())
        body.extend(
            (
                f'Content-Disposition: form-data; name="{field_name}"; '
                f'filename="{file_path.name}"\r\n'
            ).encode()
        )
        body.extend(f"Content-Type: {mime_type}\r\n\r\n".encode())
        body.extend(file_path.read_bytes())
        body.extend(b"\r\n")

    body.extend(f"--{boundary}--\r\n".encode())
    return bytes(body), f"multipart/form-data; boundary={boundary}"


def call_openai_image_edit(
    *,
    api_key: str,
    endpoint: str,
    image_path: pathlib.Path,
    prompt: str,
    model: str,
    size: str,
    quality: str,
    output_format: str,
    n: int,
    timeout: int,
    retries: int,
) -> dict:
    fields = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "output_format": output_format,
        "n": str(n),
    }
    body, content_type = encode_multipart(fields, [("image", image_path)])
    request = urllib.request.Request(
        endpoint,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": content_type,
        },
    )

    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"HTTP {exc.code}: {detail}")
        except Exception as exc:  # noqa: BLE001 - surface exact failure in manifest.
            last_error = exc
        if attempt < retries:
            time.sleep(min(2**attempt, 8))
    raise RuntimeError(f"OpenAI image edit failed after {retries + 1} attempts: {last_error}")


def image_data_url(image_path: pathlib.Path) -> str:
    mime_type = mimetypes.guess_type(image_path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def extract_chat_completion_text(response: dict) -> str:
    if isinstance(response.get("output_text"), str) and response["output_text"].strip():
        return response["output_text"].strip()

    choices = response.get("choices") or []
    if choices:
        message = choices[0].get("message") or {}
        content = message.get("content", "")
        if isinstance(content, str):
            return content.strip()
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, str):
                    parts.append(item)
                elif isinstance(item, dict):
                    text = item.get("text")
                    if isinstance(text, str):
                        parts.append(text)
            joined = "\n".join(part.strip() for part in parts if part.strip())
            if joined:
                return joined

    raise RuntimeError("Text API response did not contain a usable prompt.")


def call_openai_chat_completion(
    *,
    api_key: str,
    endpoint: str,
    image_path: pathlib.Path,
    prompt: str,
    model: str,
    max_tokens: int,
    temperature: float,
    timeout: int,
    retries: int,
) -> dict:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "你是严谨的广告实验刺激材料 prompt 写作者，只输出用户要求的中性商品 prompt。",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_data_url(image_path)}},
                ],
            },
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    last_error: Exception | None = None
    for attempt in range(retries + 1):
        request = urllib.request.Request(
            endpoint,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"HTTP {exc.code}: {detail}")
        except Exception as exc:  # noqa: BLE001 - surface exact failure in manifest.
            last_error = exc
        if attempt < retries:
            time.sleep(min(2**attempt, 8))
    raise RuntimeError(f"OpenAI chat completion failed after {retries + 1} attempts: {last_error}")


def base_prompt_output_path(args: argparse.Namespace, product_id: str, orientation: str | None = None) -> pathlib.Path:
    if uses_orientation_specific_generated_prompt(args.prompt_version):
        orientation_label_value = safe_name((orientation or "unknown").lower().replace("-", "_"))
        return pathlib.Path(args.base_prompt_dir) / f"{product_id}_{orientation_label_value}_prompt.txt"
    return pathlib.Path(args.base_prompt_dir) / f"{product_id}_neutral_prompt.txt"


def load_base_prompt_template(args: argparse.Namespace, orientation: str | None = None) -> tuple[str, str]:
    prompt_file_config = args.base_prompt_file or DEFAULT_BASE_PROMPT_FILES.get(args.prompt_version)
    if isinstance(prompt_file_config, dict):
        if not orientation:
            raise ValueError(f"Prompt version {args.prompt_version!r} requires an orientation-specific base prompt template.")
        prompt_file = prompt_file_config.get(orientation)
    else:
        prompt_file = prompt_file_config
    if not prompt_file:
        raise ValueError(f"No default base prompt file is configured for prompt version {args.prompt_version!r}.")
    prompt_path = pathlib.Path(prompt_file)
    return prompt_path.read_text(encoding="utf-8"), str(prompt_path)


def generated_prompt_cache_key(args: argparse.Namespace, product_id: str, orientation: str) -> str:
    if uses_orientation_specific_generated_prompt(args.prompt_version):
        return f"{product_id}:{orientation}"
    return product_id


def get_generated_product_prompt(
    *,
    row: dict[str, str],
    product_id: str,
    orientation: str,
    source_path: pathlib.Path,
    args: argparse.Namespace,
    api_key: str,
    base_prompt_template: str,
    cache: dict[str, dict[str, object]],
) -> dict[str, object]:
    cache_key = generated_prompt_cache_key(args, product_id, orientation)
    if cache_key in cache:
        return cache[cache_key]

    request_prompt = render_prompt(base_prompt_template, row, orientation)
    output_path = base_prompt_output_path(args, product_id, orientation)
    request_path = output_path.with_name(f"{output_path.stem}.request.txt")

    if output_path.exists() and output_path.stat().st_size > 0 and not args.overwrite:
        prompt_text = output_path.read_text(encoding="utf-8").strip()
        result = {
            "text": prompt_text,
            "path": str(output_path),
            "request_path": str(request_path) if request_path.exists() else "",
            "source": "cache",
            "request_prompt": request_prompt,
        }
        cache[cache_key] = result
        return result

    response = call_openai_chat_completion(
        api_key=api_key,
        endpoint=args.base_prompt_endpoint,
        image_path=source_path,
        prompt=request_prompt,
        model=args.base_prompt_model,
        max_tokens=args.base_prompt_max_tokens,
        temperature=args.base_prompt_temperature,
        timeout=args.timeout,
        retries=args.retries,
    )
    prompt_text = extract_chat_completion_text(response)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(prompt_text.strip() + "\n", encoding="utf-8")
    request_path.write_text(request_prompt.strip() + "\n", encoding="utf-8")

    result = {
        "text": prompt_text,
        "path": str(output_path),
        "request_path": str(request_path),
        "source": "api",
        "request_prompt": request_prompt,
        "api_usage": response.get("usage") or {},
    }
    cache[cache_key] = result
    return result


def save_images(response: dict, output_prefix: pathlib.Path, output_format: str) -> list[pathlib.Path]:
    saved_paths: list[pathlib.Path] = []
    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    for index, image_obj in enumerate(response.get("data", [])):
        b64_json = image_obj.get("b64_json")
        if not b64_json:
            continue
        suffix = f"_{index + 1}" if len(response.get("data", [])) > 1 else ""
        output_path = output_prefix.with_name(f"{output_prefix.name}{suffix}.{output_format}")
        output_path.write_bytes(base64.b64decode(b64_json))
        saved_paths.append(output_path)
    if not saved_paths:
        raise RuntimeError("API response did not contain data[].b64_json images.")
    return saved_paths


def append_manifest(manifest_path: pathlib.Path, record: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("a", encoding="utf-8") as manifest_file:
        manifest_file.write(json.dumps(record, ensure_ascii=False) + "\n")


def iter_records(
    rows: Iterable[dict[str, str]],
    args: argparse.Namespace,
    plans: Iterable[OrientationPlan],
) -> Iterable[dict]:
    for row in rows:
        product_id = safe_name(row.get("id", ""))
        source_url = row.get("creative_id_image", "").strip()
        source_ext = extension_from_url(source_url)
        source_path = pathlib.Path(args.source_dir) / f"{product_id}{source_ext}"
        for plan in plans:
            orientation = safe_name(plan.orientation)
            output_prefix = pathlib.Path(args.output_dir) / plan.orientation / f"{product_id}_{orientation}"
            extra_values = {}
            if uses_generated_base_prompt(args.prompt_version):
                extra_values[generated_prompt_template_field(args.prompt_version)] = generated_base_prompt_placeholder(args.prompt_version)
            prompt = render_prompt(plan.prompt_template, row, plan.orientation, extra_values)
            yield {
                "row": row,
                "product_id": product_id,
                "source_url": source_url,
                "source_path": source_path,
                "output_prefix": output_prefix,
                "prompt": prompt,
                "orientation": plan.orientation,
                "requested_orientation": plan.requested_orientation,
                "prompt_source": plan.prompt_source,
                "prompt_template": plan.prompt_template,
            }


def main() -> int:
    args = parse_args()
    plans = resolve_orientation_plans(args)
    rows = select_rows(read_rows(pathlib.Path(args.csv)), args)
    resolve_output_paths(args, rows, plans)
    base_prompt_templates: dict[str, tuple[str, str]] = {}
    if uses_generated_base_prompt(args.prompt_version):
        for plan in plans:
            base_prompt_templates[plan.orientation] = load_base_prompt_template(args, plan.orientation)

    if not rows:
        print("No rows selected.", file=sys.stderr)
        return 1

    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key and not (args.dry_run or args.download_only):
        print("OPENAI_API_KEY or --api-key is required unless --dry-run or --download-only is used.", file=sys.stderr)
        return 2

    selected_ids = ", ".join(row.get("id", "") for row in rows)
    print(f"RUN dir={args.run_dir}", flush=True)
    print(f"MODEL {args.model}", flush=True)
    print(f"ENDPOINT {args.endpoint}", flush=True)
    print(f"PROMPT_VERSION {args.prompt_version}", flush=True)
    if uses_generated_base_prompt(args.prompt_version):
        print(f"BASE_PROMPT_MODEL {args.base_prompt_model}", flush=True)
        print(f"BASE_PROMPT_ENDPOINT {args.base_prompt_endpoint}", flush=True)
    print(f"ROWS {len(rows)} ids={selected_ids}", flush=True)
    print(f"ORIENTATIONS {', '.join(plan.orientation for plan in plans)}", flush=True)

    total_records = len(rows) * len(plans)
    progress = ProgressTracker(total_records, enabled=not args.no_progress)
    generated_prompt_cache: dict[str, dict[str, object]] = {}

    for record in iter_records(rows, args, plans):
        row = record["row"]
        output_prefix: pathlib.Path = record["output_prefix"]
        expected_outputs = expected_output_paths(output_prefix, args.output_format, args.n)
        label = f"id={row.get('id')} orientation={record['orientation']}"
        manifest_record = {
            "id": row.get("id"),
            "material_id": row.get("material_id"),
            "category": row.get("level_one_category_name"),
            "brand": row.get("creative_id_brand"),
            "orientation": record["orientation"],
            "requested_orientation": record["requested_orientation"],
            "source_url": record["source_url"],
            "source_path": str(record["source_path"]),
            "output_prefix": str(output_prefix),
            "run_dir": args.run_dir,
            "timestamp": args.timestamp,
            "selection_mode": effective_selection_mode(args),
            "prompt_version": args.prompt_version,
            "model": args.model,
            "endpoint": args.endpoint,
            "size": args.size,
            "quality": args.quality,
            "output_format": args.output_format,
            "sample_size": args.sample_size,
            "random_seed": args.random_seed,
            "prompt_source": record["prompt_source"],
            "status": "planned",
            "prompt": record["prompt"],
        }
        if uses_generated_base_prompt(args.prompt_version):
            base_prompt_template, base_prompt_source = base_prompt_templates[record["orientation"]]
            generated_prompt_field = generated_prompt_template_field(args.prompt_version)
            base_request_prompt = render_prompt(base_prompt_template, row, record["orientation"])
            manifest_record["base_prompt_source"] = base_prompt_source
            manifest_record["base_prompt_model"] = args.base_prompt_model
            manifest_record["base_prompt_endpoint"] = args.base_prompt_endpoint
            manifest_record["base_prompt_generation_prompt"] = base_request_prompt
            manifest_record[generated_prompt_field] = generated_base_prompt_placeholder(args.prompt_version)

        try:
            if all(path.exists() for path in expected_outputs) and not args.overwrite:
                manifest_record["status"] = "skipped_exists"
                append_manifest(pathlib.Path(args.manifest), manifest_record)
                print(f"SKIP existing output for {label}: {expected_outputs}", flush=True)
                progress.advance("skipped", label)
                continue

            print(f"PROCESS {label} category={row.get('level_one_category_name')}", flush=True)
            if args.dry_run:
                manifest_record["status"] = "dry_run"
                append_manifest(pathlib.Path(args.manifest), manifest_record)
                if uses_generated_base_prompt(args.prompt_version):
                    print("BASE_PROMPT_REQUEST", flush=True)
                    print(manifest_record["base_prompt_generation_prompt"], flush=True)
                    print("FINAL_IMAGE_PROMPT_WITH_PLACEHOLDER", flush=True)
                print(record["prompt"], flush=True)
                progress.advance("dry_run", label)
                continue

            source_path = download_image(
                record["source_url"],
                record["source_path"],
                timeout=args.timeout,
                retries=args.retries,
            )
            manifest_record["source_path"] = str(source_path)

            if args.download_only:
                manifest_record["status"] = "downloaded"
                append_manifest(pathlib.Path(args.manifest), manifest_record)
                progress.advance("downloaded", label)
                continue

            if uses_generated_base_prompt(args.prompt_version):
                base_prompt_template, _base_prompt_source = base_prompt_templates[record["orientation"]]
                generated_prompt = get_generated_product_prompt(
                    row=row,
                    product_id=record["product_id"],
                    orientation=record["orientation"],
                    source_path=source_path,
                    args=args,
                    api_key=api_key or "",
                    base_prompt_template=base_prompt_template,
                    cache=generated_prompt_cache,
                )
                generated_prompt_text = str(generated_prompt["text"])
                generated_prompt_field = generated_prompt_template_field(args.prompt_version)
                record["prompt"] = render_prompt(
                    record["prompt_template"],
                    row,
                    record["orientation"],
                    {generated_prompt_field: generated_prompt_text},
                )
                manifest_record["prompt"] = record["prompt"]
                manifest_record[generated_prompt_field] = generated_prompt_text
                manifest_record["generated_product_prompt"] = generated_prompt_text
                manifest_record["generated_product_prompt_path"] = generated_prompt["path"]
                manifest_record["base_prompt_request_path"] = generated_prompt.get("request_path")
                manifest_record["base_prompt_cache_status"] = generated_prompt["source"]
                if generated_prompt.get("api_usage"):
                    manifest_record["base_prompt_api_usage"] = generated_prompt["api_usage"]

            response = call_openai_image_edit(
                api_key=api_key or "",
                endpoint=args.endpoint,
                image_path=source_path,
                prompt=record["prompt"],
                model=args.model,
                size=args.size,
                quality=args.quality,
                output_format=args.output_format,
                n=args.n,
                timeout=args.timeout,
                retries=args.retries,
            )
            saved_paths = save_images(response, output_prefix, args.output_format)
            manifest_record["status"] = "generated"
            manifest_record["outputs"] = [str(path) for path in saved_paths]
            manifest_record["api_usage"] = response.get("usage")
            append_manifest(pathlib.Path(args.manifest), manifest_record)
            print(f"SAVED id={row.get('id')} outputs={saved_paths}", flush=True)
            progress.advance("generated", label)
            if args.sleep > 0:
                time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001 - keep batch processing robust.
            manifest_record["status"] = "error"
            manifest_record["error"] = str(exc)
            manifest_record["traceback"] = traceback.format_exc()
            append_manifest(pathlib.Path(args.manifest), manifest_record)
            print(f"ERROR id={row.get('id')}: {exc}", file=sys.stderr)
            progress.advance("error", label)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
