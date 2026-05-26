# Generate Images

Generate advertising images from white-background product images listed in the CSV files.

Expected workflow:

1. Read product rows from `data/raw/white_bg_product_catalog.csv` or `data/experiment/white_bg_product_catalog_experiment.csv`.
2. Download or reference the white-background product image from `creative_id_image`.
3. Generate prompts based on product category and creative orientation.
4. Support three canonical creative orientations. `current` and `function_v2` use the legacy set:
   - `Product-oriented`
   - `Context-oriented`
   - `Symbolic-oriented`
   `v3`, `v4`, `v5`, and `v6` use the Park-theory-grounded set:
   - `Product-oriented`
   - `Symbolic-oriented`
   - `Experiential-oriented`
5. Save generated images to `outputs/`.

`Affect-oriented` is accepted as a deprecated alias for `Symbolic-oriented`. Under `--prompt-version v3`, `v4`, `v5`, or `v6`, `Context-oriented` is also accepted as a deprecated alias for `Experiential-oriented`.

Recommended output naming:

```text
{id}_{orientation}_{variant}.png
```

## Usage

Default actual run: use `gpt-image-2`, VectorEngine-compatible `/v1/images/edits`, the previous fixed random-10 sample, and all three orientations. Outputs go to a timestamped run directory such as `outputs/gpt-image-2_random10_seed20260523_three_orientations_20260525_153012/`.

```bash
python3 scripts/generate_images/generate_from_csv.py --api-key "sk-xxx"
```

Equivalent safer form that keeps the key out of the command line:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py
```

Preview the default batch and rendered prompts without network calls:

```bash
python3 scripts/generate_images/generate_from_csv.py --dry-run
```

Use the newer prompt set that separates Product as function from Symbolic as meaning:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version function_v2 \
  --api-key "sk-xxx"
```

Use the concise v4 Park-theory-grounded prompt set:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v4 \
  --api-key "sk-xxx"
```

Use the concept-only v5 Park-theory-grounded prompt set:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v5 \
  --api-key "sk-xxx"
```

Use the balanced v6 Park-theory-grounded prompt set:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v6 \
  --api-key "sk-xxx"
```

Run the previous fixed sample explicitly:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --selection-mode previous-random10 \
  --api-key "sk-xxx"
```

Run the first N rows in CSV order:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --selection-mode sequential \
  --start 0 \
  --limit 20 \
  --api-key "sk-xxx"
```

Run a deterministic random sample of N rows:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --selection-mode random \
  --sample-size 20 \
  --random-seed 20260523 \
  --api-key "sk-xxx"
```

Generate only one orientation:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --image-type context \
  --selection-mode sequential \
  --limit 5 \
  --api-key "sk-xxx"
```

Generate only Experiential-oriented v4 images:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --image-type experiential \
  --prompt-version v4 \
  --selection-mode random \
  --sample-size 10 \
  --random-seed 20260523 \
  --api-key "sk-xxx"
```

Generate only Product-oriented Function v2 images:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --image-type product \
  --prompt-version function_v2 \
  --selection-mode random \
  --sample-size 10 \
  --random-seed 20260523 \
  --api-key "sk-xxx"
```

Download white-background source images and render prompts without calling the image API:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --download-only \
  --selection-mode sequential \
  --limit 3
```

## Important Arguments

- `--csv`: input product CSV.
- `--prompt-file`: prompt template with CSV placeholders such as `{ori_title}` and `{level_one_category_name}`. When omitted, the script uses the orientation-specific prompt file.
- `--prompt-version`: prompt file set to use; `current` preserves the original prompts, `function_v2` uses the revised separation prompts, `v3` uses a longer Park-theory-grounded prompt, `v4` uses a concise definition-first prompt with grounding/generalization discipline, `v5` keeps only the brand-concept definition, and `v6` restores compact experimental controls and concept-image linkage.
- `--prompt`: inline prompt template; overrides `--prompt-file`.
- `--orientation`: generate one orientation only; deprecated alias `Affect-oriented` is normalized to `Symbolic-oriented`. Under `--prompt-version v3`, `v4`, `v5`, or `v6`, deprecated alias `Context-oriented` is normalized to `Experiential-oriented`.
- `--image-type`: short alias for generating one type only: `product`/`function`, `context`/`usage`, `symbolic`, or `experiential`/`experience`. Under `v3`, `v4`, `v5`, or `v6`, `context` and `usage` resolve to `Experiential-oriented`.
- `--orientations`: comma-separated orientations, or `all`; defaults to all three canonical orientations for the selected prompt version.
- `--selection-mode`: `previous-random10`, `sequential`, or `random`; defaults to `previous-random10`.
- `--limit`: maximum rows to process. Sequential mode defaults to 1 if `--limit` is omitted.
- `--sample-size`: randomly sample N rows after white-image filtering and optional `--start` selection.
- `--random-seed`: deterministic seed for `--sample-size`; defaults to `20260523` or `GENAI_AD_IMAGE_RANDOM_SEED`.
- `--ids`: comma-separated product ids to process.
- `--api-key`: runtime API key. Prefer `OPENAI_API_KEY` if you do not want the key in shell history.
- `--api-base-url`: defaults to `https://api.vectorengine.cn/v1`.
- `--endpoint`: defaults to `{api-base-url}/images/edits`.
- `--run-dir`: run root directory. Supports `{model}`, `{selection_label}`, `{orientation_label}`, `{prompt_version}`, and `{timestamp}` placeholders.
- `--dry-run`: render prompts only.
- `--download-only`: download source images only.
- `--model`: image model, defaults to `OPENAI_IMAGE_MODEL` or `gpt-image-2`.
- `--output-dir`: generated image destination, defaults to `{run-dir}/generated`.
- `--no-progress`: disables the progress bar and ETA.

## Outputs

- Run root: `outputs/{model}_{selection_label}_{orientation_label}_{timestamp}/`
- Function v2 run root: `outputs/{model}_{selection_label}_{orientation_label}_function_v2_{timestamp}/`
- v3 run root: `outputs/{model}_{selection_label}_{orientation_label}_v3_{timestamp}/`
- v4 run root: `outputs/{model}_{selection_label}_{orientation_label}_v4_{timestamp}/`
- v5 run root: `outputs/{model}_{selection_label}_{orientation_label}_v5_{timestamp}/`
- v6 run root: `outputs/{model}_{selection_label}_{orientation_label}_v6_{timestamp}/`
- Generated images: `{run-dir}/generated/{orientation}/{id}_{orientation}.png`
- Downloaded source images: `{run-dir}/source_images/{id}.{ext}`
- Manifest JSONL: `{run-dir}/generation_manifest.jsonl`
