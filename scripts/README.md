# Scripts

This directory is reserved for future data preparation and image generation scripts.

## Inputs

Scripts should read from one of:

- `data/raw/white_bg_product_catalog.csv`
- `data/experiment/white_bg_product_catalog_experiment.csv`

Required fields:

```text
id, material_id, ori_title, creative_id_image, creative_id_brand,
creative_id_price, creative_id_promotion, level_one_category_name,
is_white_image
```

`creative_id_image` is the white-background product image URL and should be treated as the source image for generation.

## Outputs

Generated images, logs, API responses, and intermediate files should be written to `outputs/`. The directory is ignored by Git except for `.gitkeep`.

## Current Script

Use `scripts/generate_images/generate_from_csv.py` to read product rows, download the white-background image from `creative_id_image`, render a prompt template, and send the image plus prompt to the OpenAI Images Edit API. The same script now also supports a `--multiround` mode for the `definition-only-v6` prompt family, where it generates, judges, revises, regenerates, and re-judges each image.

Start safely with:

```bash
python3 scripts/generate_images/generate_from_csv.py --dry-run --limit 1
```
