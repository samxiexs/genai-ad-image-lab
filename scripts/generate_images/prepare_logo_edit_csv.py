#!/usr/bin/env python3
"""Create an image-edit CSV that points to existing generated ad images.

The main generator expects one input image per CSV row and names output files from
the ``id`` column.  This helper gives every existing generated image a unique ID,
while retaining the product metadata (including its brand) from the experiment CSV.
"""

from __future__ import annotations

import argparse
import csv
import pathlib
import re
from collections.abc import Iterable


CANONICAL_LOGOS = {
    "Ninebot/九号": "Ninebot official wordmark",
    "Dyson/戴森": "Dyson official wordmark",
    "Hasselblad/哈苏": "Hasselblad official wordmark and star emblem",
    "Apple/苹果": "Apple bitten-apple symbol only, with no accompanying text",
    "Louis Vuitton/LV": "Louis Vuitton LV monogram",
    "Sony PlayStation/索尼": "PlayStation symbol and PlayStation wordmark",
    "Versace/范思哲": "VERSACE Medusa emblem and VERSACE wordmark",
    "EMPORIO ARMANI/阿玛尼": "EMPORIO ARMANI eagle emblem and wordmark",
    "HP/惠普": "HP circular logo",
    "Littleswan/小天鹅": "Little Swan official wordmark",
    "Midea/美的": "Midea official wordmark",
    "LEGO/乐高": "LEGO official red-square wordmark",
    "woodwick": "WoodWick official wordmark",
    "爱之湾": "爱之湾 official Chinese wordmark",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=pathlib.Path, help="Original experiment CSV.")
    parser.add_argument(
        "--input-dirs",
        required=True,
        nargs="+",
        type=pathlib.Path,
        help="One or more existing generated/Symbolic-oriented directories.",
    )
    parser.add_argument("--output-csv", required=True, type=pathlib.Path, help="CSV to write for image editing.")
    parser.add_argument("--orientation", default="Symbolic-oriented", help="Orientation encoded in input filenames.")
    return parser.parse_args()


def read_rows(path: pathlib.Path) -> tuple[list[str], dict[str, dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError(f"No header found in {path}")
        rows = list(reader)
    return list(reader.fieldnames), {row["id"]: row for row in rows}


def image_files(input_dirs: Iterable[pathlib.Path]) -> Iterable[pathlib.Path]:
    for directory in input_dirs:
        if not directory.is_dir():
            raise FileNotFoundError(f"Input directory does not exist: {directory}")
        yield from sorted(
            path for path in directory.iterdir() if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        )


def main() -> None:
    args = parse_args()
    fieldnames, source_rows = read_rows(args.csv)
    suffix = re.escape(f"_{args.orientation}")
    filename_pattern = re.compile(rf"^(?P<product_id>.+?){suffix}(?:_rollout\d+)?$")
    extra_fields = ["source_original_id", "source_run", "source_filename", "logo_brand"]
    output_fields = fieldnames + [field for field in extra_fields if field not in fieldnames]
    prepared_rows: list[dict[str, str]] = []
    seen_ids: set[str] = set()

    for image_path in image_files(args.input_dirs):
        match = filename_pattern.match(image_path.stem)
        if not match:
            raise ValueError(f"Filename does not match the requested orientation: {image_path.name}")
        original_id = match.group("product_id")
        if original_id not in source_rows:
            raise ValueError(f"No CSV metadata found for source image {image_path.name} (id={original_id!r})")

        run_name = image_path.parents[2].name  # <run-dir>/generated/<orientation>/<image>
        edit_id = f"{original_id}__{run_name}__{image_path.stem}"
        if edit_id in seen_ids:
            raise ValueError(f"Duplicate edit ID: {edit_id}")
        seen_ids.add(edit_id)

        row = dict(source_rows[original_id])
        brand = row.get("creative_id_brand", "").strip()
        row.update(
            {
                "id": edit_id,
                "creative_id_image": image_path.resolve().as_uri(),
                "source_original_id": original_id,
                "source_run": run_name,
                "source_filename": image_path.name,
                "logo_brand": CANONICAL_LOGOS.get(brand, f"{brand} official logo"),
            }
        )
        prepared_rows.append(row)

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(prepared_rows)
    print(f"Wrote {len(prepared_rows)} image-edit rows to {args.output_csv}")


if __name__ == "__main__":
    main()
