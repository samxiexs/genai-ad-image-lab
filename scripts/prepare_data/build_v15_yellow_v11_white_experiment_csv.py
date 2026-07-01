#!/usr/bin/env python3
"""Build the final experiment CSV from screenshot-selected v15 and v11 rows.

Yellow rows are the 6 highlighted products from the v15 4 x 120 table.
White rows are screenshot-selected rows 11-15 from the v11 table and are
treated as non-symbolic.

The output keeps only the columns needed by the v14/v15 prompt metadata and
the image-generation script. `candidate_group` is retained for
--selection-mode random-per-group3.
"""

from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
YELLOW_CSV = REPO_ROOT / "data/experiment/white_bg_product_catalog_v15_120_each.csv"
WHITE_CSV = REPO_ROOT / "data/experiment/white_bg_product_catalog_v11_user_selected_from_screenshot.csv"
OUTPUT_CSV = REPO_ROOT / "data/experiment/white_bg_product_catalog_v15_yellow_v11_white_metadata.csv"
SUMMARY_MD = REPO_ROOT / "data/experiment/white_bg_product_catalog_v15_yellow_v11_white_metadata_summary.md"

YELLOW_SELECTED_IDS = [
    "65447",
    "50958",
    "26328",
    "14314",
    "1547520",
    "100401",
]

WHITE_SELECTED_ORDERS = ["11", "12", "13", "14", "15"]

OUTPUT_COLUMNS = [
    "id",
    "material_id",
    "ori_title",
    "creative_id_image",
    "creative_id_brand",
    "creative_id_price",
    "creative_id_promotion",
    "level_one_category_name",
    "is_white_image",
    "candidate_group",
    "symbolic",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_symbolic(value: str) -> str:
    return "true" if str(value).strip().lower() in {"1", "true", "yes"} else "false"


def project_row(row: dict[str, str], symbolic: str) -> dict[str, str]:
    projected = {column: row.get(column, "") for column in OUTPUT_COLUMNS}
    projected["symbolic"] = normalize_symbolic(symbolic)
    return projected


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def count_by(rows: list[dict[str, str]], column: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = row.get(column, "")
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def select_rows_by_values(
    rows: list[dict[str, str]],
    *,
    column: str,
    values: list[str],
    source_name: str,
) -> list[dict[str, str]]:
    indexed = {str(row.get(column, "")).strip(): row for row in rows}
    missing = [value for value in values if value not in indexed]
    if missing:
        raise ValueError(f"{source_name} missing {column} values: {missing}")
    return [indexed[value] for value in values]


def write_summary(
    *,
    output_rows: list[dict[str, str]],
    yellow_rows: list[dict[str, str]],
    white_rows: list[dict[str, str]],
) -> None:
    lines = [
        "# V15 yellow + V11 white screenshot-selected metadata CSV",
        "",
        f"- Yellow source: `{YELLOW_CSV}`",
        f"- White source: `{WHITE_CSV}`",
        f"- Output CSV: `{OUTPUT_CSV}`",
        "",
        "Build rule:",
        "",
        f"- Yellow rows are selected by id: `{', '.join(YELLOW_SELECTED_IDS)}`.",
        f"- White rows are selected by `user_selected_order`: `{', '.join(WHITE_SELECTED_ORDERS)}`.",
        "- Yellow rows keep their existing `symbolic` value.",
        "- White rows are assigned `symbolic=false`.",
        "- Only generation-script required columns, `candidate_group`, and v14/v15 metadata column `symbolic` are retained.",
        "",
        "Counts:",
        "",
        f"- selected yellow rows: {len(yellow_rows)}",
        f"- selected white rows: {len(white_rows)}",
        f"- output rows: {len(output_rows)}",
        f"- unique ids: {len({row['id'] for row in output_rows})}",
        f"- symbolic counts: {count_by(output_rows, 'symbolic')}",
        f"- candidate_group counts: {count_by(output_rows, 'candidate_group')}",
        "",
        "Rows:",
        "",
    ]
    for row in output_rows:
        lines.append(
            f"- {row['id']} | {row['candidate_group']} | symbolic={row['symbolic']} | {row['ori_title']}"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    yellow_source_rows = read_csv(YELLOW_CSV)
    white_source_rows = read_csv(WHITE_CSV)
    yellow_rows = select_rows_by_values(
        yellow_source_rows,
        column="id",
        values=YELLOW_SELECTED_IDS,
        source_name="yellow source",
    )
    white_rows = select_rows_by_values(
        white_source_rows,
        column="user_selected_order",
        values=WHITE_SELECTED_ORDERS,
        source_name="white source",
    )

    output_rows: list[dict[str, str]] = []
    for row in yellow_rows:
        output_rows.append(project_row(row, row.get("symbolic", "")))
    for row in white_rows:
        output_rows.append(project_row(row, "false"))

    write_csv(OUTPUT_CSV, output_rows)
    write_summary(
        output_rows=output_rows,
        yellow_rows=yellow_rows,
        white_rows=white_rows,
    )

    print(f"WROTE {OUTPUT_CSV}")
    print(f"WROTE {SUMMARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
