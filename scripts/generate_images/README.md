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
   `v3`, `v4`, `v5`, `v6`, `v7`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13`, `v14`, `v15`, `v16`, `v17`, `definition-only`, `definition-control`, `visual-control`, `definition-genprompt`, `definition-control-genprompt`, `genprompt-control`, `definition-only-v6`, and the matching `-v2` / `-v3` families use the Park-theory-grounded set:
   - `Product-oriented`
   - `Symbolic-oriented`
   - `Experiential-oriented`
5. Save generated images to `outputs/`.

`Affect-oriented` is accepted as a deprecated alias for `Symbolic-oriented`. Under `--prompt-version v3`, `v4`, `v5`, `v6`, `v7`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13`, `v14`, `v15`, `v16`, `v17`, `definition-only`, `definition-control`, `visual-control`, `definition-genprompt`, `definition-control-genprompt`, `genprompt-control`, `definition-only-v6`, or the matching `-v2` / `-v3` family, `Context-oriented` is also accepted as a deprecated alias for `Experiential-oriented`.

Recommended output naming:

```text
{id}_{orientation}_{variant}.png
{id}_{orientation}_rollout01.png
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

Use the v7 Park-theory-grounded prompt set with function_v2-style quality controls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v7 \
  --api-key "sk-xxx"
```

Use the v8 prompt set for Park's original definition with only minimal quality controls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v8 \
  --api-key "sk-xxx"
```

Use the v9 prompt set for Park's original definition plus selected function_v2-style detail controls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v9 \
  --api-key "sk-xxx"
```

Use the v10 prompt set for the integrated research version that combines Park definitions with later prompt-alignment and discriminant-validity controls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v10 \
  --api-key "sk-xxx"
```

Use the v11 prompt set for the stronger source-grounded version that explicitly reads the white-background image first and uses metadata only as supporting evidence:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v11 \
  --api-key "sk-xxx"
```

Use the v12 prompt set for the function_v2-quality version that directly fuses v2-style visual discipline with Park's three brand-concept definitions:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v12 \
  --api-key "sk-xxx"
```

Use the v13 prompt set for the sharper-separation version that keeps v12-style execution discipline but strengthens source-image grounding and discriminant validity:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v13 \
  --api-key "sk-xxx"
```

Use the v14 prompt set from `prompts/research_conditions_v14/*/definition-only.txt`. By default, v14 is treated as a rollout prompt version: each selected product-orientation pair is generated 3 times as separate API calls, with output names such as `{id}_{orientation}_rollout01.png`, `{id}_{orientation}_rollout02.png`, and `{id}_{orientation}_rollout03.png`.

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v14 \
  --api-key "sk-xxx"
```

Set the v14 rollout count explicitly:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v14 \
  --rollouts 5 \
  --api-key "sk-xxx"
```

Disable v14 rollout and generate only once per product-orientation pair:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v14 \
  --no-rollout \
  --api-key "sk-xxx"
```

Preview the v14 rollout plan without network calls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v14 \
  --limit 1 \
  --dry-run
```

Use the v16 prompt set from `prompts/research_conditions_v16/*/definition-only.txt`. It also defaults to 3 rollout API calls per selected product-orientation pair:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v16 \
  --selection-mode sequential \
  --limit 14
```

Disable v15 rollout and generate only once per product-orientation pair:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v15 \
  --no-rollout \
  --selection-mode sequential \
  --limit 14
```

Use the v16 prompt set for the neutral-product-prompt two-stage flow:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v16 \
  --selection-mode sequential \
  --limit 14
```

Use the v17 prompt set for the full-English orientation-specific prompt-generation flow. The script first generates one Product/Symbolic/Experiential-specific image prompt per product per orientation, then sends that generated prompt to the image model:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v17 \
  --selection-mode sequential \
  --limit 14
```

Use the `definition-only` research alias for the confirmed definition-first baseline:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-only --api-key "sk-xxx"
```

Use `definition-control` for `def + visual control`:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control --api-key "sk-xxx"
```

Use `definition-only-v6` for the multiround-ready v6 definition-only family:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-only-v6 \
  --api-key "sk-xxx"
```

Run the v6 multiround workflow on the final 15-product dataset:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --csv data/experiment/white_bg_product_catalog_final_15_selected.csv \
  --prompt-version definition-only-v6 \
  --multiround \
  --selection-mode sequential \
  --limit 15 \
  --model-provider api111 \
  --base-prompt-provider api111 \
  --run-dir outputs/final15_definition-only-v6_multiround \
  --api-key "sk-xxx"
```

Preview the multiround workflow without network calls:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --csv data/experiment/white_bg_product_catalog_final_15_selected.csv \
  --prompt-version definition-only-v6 \
  --multiround \
  --selection-mode sequential \
  --limit 1 \
  --dry-run
```

Use `definition-genprompt` for `def -> generated prompt -> image`:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-genprompt --selection-mode sequential --limit 14
```

Use `definition-control-genprompt` for `def -> generated prompt -> dc wrapper -> image`:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt --selection-mode sequential --limit 14
```

Backward-compatible version names still work:

- `visual-control` = `definition-control`
- `genprompt-control` = `definition-control-genprompt`

Independent refactor version names:

- `definition-only-v2`
- `definition-control-v2`
- `visual-control-v2`
- `definition-genprompt-v2`
- `definition-control-genprompt-v2`
- `genprompt-control-v2`

Boundary-hardened refactor version names:

- `definition-only-v3`
- `definition-control-v3`
- `visual-control-v3`
- `definition-genprompt-v3`
- `definition-control-genprompt-v3`
- `genprompt-control-v3`

Boundary-hardened refactor examples:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-v3 --api-key "sk-xxx"
```

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt-v3 --selection-mode sequential --limit 14
```

HeyRoute final image-generation example:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-control-v3 \
  --image-type function \
  --selection-mode sequential \
  --limit 10 \
  --model-provider heyroute \
  --run-dir outputs/heyroute_definition-control-function-v3
```

API111 final image-generation example:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-control-v3 \
  --image-type function \
  --selection-mode sequential \
  --limit 10 \
  --model-provider api111 \
  --run-dir outputs/api111_definition-control-function-v3 \
  --api-key "sk-xxx"
```

API111 raw image-generation endpoint example:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-control-v3 \
  --image-type function \
  --selection-mode sequential \
  --limit 10 \
  --model-provider api111 \
  --image-wire-api images_generations \
  --endpoint https://api.vectorengine.cn/v1/images/generations \
  --run-dir outputs/api111_definition-control-function-v3_generations \
  --api-key "sk-xxx"
```

HeyRoute base-prompt provider example:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-control-genprompt-v3 \
  --selection-mode sequential \
  --limit 10 \
  --base-prompt-provider heyroute \
  --run-dir outputs/heyroute_definition-control-genprompt-v3
```

Equivalent explicit flags for the provider config:

```bash
OPENAI_API_KEY="sk-xxx" python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-control-genprompt-v3 \
  --selection-mode sequential \
  --limit 10 \
  --base-prompt-model gpt-5.5 \
  --base-prompt-wire-api responses \
  --base-prompt-endpoint https://heyroute.ai/v1/responses \
  --base-prompt-reasoning-effort high \
  --disable-base-prompt-response-storage \
  --run-dir outputs/heyroute_definition-control-genprompt-v3_explicit
```

Prompt-file routing note:

- Research-condition versions load from `prompts/aliases/*.txt`.
- Historical archived versions are resolved from `prompts/test/*.txt` when root-level prompt files are absent.
- The independent refactor family loads from `prompts/research_conditions_v2/*.txt` and does not overwrite the original research-condition files.
- The boundary-hardened refactor family loads from `prompts/research_conditions_v3/*.txt` and does not overwrite either the original files or the `v2` refactor.

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
- `--prompt-version`: prompt file set to use; `current` preserves the original prompts, `function_v2` uses the revised separation prompts, `v3`-`v17` keep the historical Park-theory-grounded series, `definition-only` / `definition-control` / `definition-genprompt` / `definition-control-genprompt` keep the original four research-condition files, `visual-control` / `genprompt-control` remain backward-compatible names for those originals, the `-v2` family runs the independent refactor in `prompts/research_conditions_v2/`, the `-v3` family runs the boundary-hardened refactor in `prompts/research_conditions_v3/`, and `definition-only-v6` runs the new multiround-ready `prompts/research_conditions_v6/` family without touching the historical `v6` prompt set.
- `--base-prompt-file`: v16/v17/definition-genprompt/definition-control-genprompt/genprompt-control and the matching `-v2` / `-v3` prompt-generation template; defaults to the matching version file.
- `--model-provider`: optional provider preset for the final image-generation stage; `heyroute` uses `https://heyroute.ai/v1/responses` with `gpt-5.5`, and `api111` defaults to `gpt-image-2` on the source-image-preserving image endpoint.
- `--image-wire-api`: final image-generation wire API, one of `images_edits`, `images_generations`, or `responses`; defaults to `images_edits` unless a provider preset overrides it.
- `--image-reasoning-effort`: Responses API reasoning effort for final image generation, one of `low`, `medium`, or `high`.
- `--disable-image-response-storage`: sends `store=false` for Responses API final image generation.
- `--base-prompt-provider`: optional provider preset for prompt generation; `heyroute` uses `https://heyroute.ai/v1/responses` with `gpt-5.5`, and `api111` uses `https://api.vectorengine.cn/v1/responses` with `gpt-5.5`.
- `--base-prompt-model`: text/vision model used by v16/v17/definition-genprompt/definition-control-genprompt/genprompt-control and the matching `-v2` / `-v3` family for prompt generation, defaults to `OPENAI_BASE_PROMPT_MODEL`, `OPENAI_TEXT_MODEL`, or `gpt-5.5`.
- `--base-prompt-wire-api`: prompt-generation wire API, either `chat_completions` or `responses`; defaults to `chat_completions` unless a provider preset overrides it.
- `--base-prompt-endpoint`: prompt-generation endpoint used by v16/v17/definition-genprompt/definition-control-genprompt/genprompt-control and the matching `-v2` / `-v3` family; defaults to the provider preset endpoint or `{api-base-url}/chat/completions` / `{api-base-url}/responses`.
- `--base-prompt-dir`: directory for saved generated prompts, defaults to `{run-dir}/base_prompts`.
- `--base-prompt-reasoning-effort`: Responses API reasoning effort for prompt generation, one of `low`, `medium`, or `high`.
- `--disable-base-prompt-response-storage`: sends `store=false` for Responses API prompt generation.
- `--multiround`: runs the five-step round1 generate -> round1 judge -> revise prompt -> round2 generate -> round2 judge workflow. Currently supported only with `--prompt-version definition-only-v6`.
- `--analysis-provider`: optional provider preset for multiround judge and revise calls. Defaults to `--base-prompt-provider`.
- `--analysis-model`: text/vision model used by multiround judge and revise calls. Defaults to `--base-prompt-model`.
- `--analysis-wire-api`: wire API used by multiround judge and revise calls. Defaults to `--base-prompt-wire-api`.
- `--analysis-endpoint`: endpoint used by multiround judge and revise calls. Defaults to `--base-prompt-endpoint`.
- `--analysis-max-tokens`: maximum output tokens for multiround judge and revise calls. Defaults to `--base-prompt-max-tokens`.
- `--analysis-reasoning-effort`: Responses API reasoning effort for multiround judge and revise calls. Defaults to `--base-prompt-reasoning-effort`.
- `--prompt`: inline prompt template; overrides `--prompt-file`.
- `--orientation`: generate one orientation only; deprecated alias `Affect-oriented` is normalized to `Symbolic-oriented`. Under `--prompt-version v3`, `v4`, `v5`, `v6`, `v7`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13`, `v14`, `v15`, `v16`, `v17`, `definition-only`, `definition-control`, `visual-control`, `definition-genprompt`, `definition-control-genprompt`, `genprompt-control`, `definition-only-v6`, or the matching `-v2` / `-v3` family, deprecated alias `Context-oriented` is normalized to `Experiential-oriented`.
- `--image-type`: short alias for generating one type only: `product`/`function`, `context`/`usage`, `symbolic`, or `experiential`/`experience`. Under `v3`, `v4`, `v5`, `v6`, `v7`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13`, `v14`, `v15`, `v16`, `v17`, `definition-only`, `definition-control`, `visual-control`, `definition-genprompt`, `definition-control-genprompt`, `genprompt-control`, `definition-only-v6`, or the matching `-v2` / `-v3` family, `context` and `usage` resolve to `Experiential-oriented`.
- `--orientations`: comma-separated orientations, or `all`; defaults to all three canonical orientations for the selected prompt version.
- `--selection-mode`: `previous-random10`, `sequential`, or `random`; defaults to `previous-random10`.
- `--limit`: maximum rows to process. Sequential mode defaults to 1 if `--limit` is omitted.
- `--sample-size`: randomly sample N rows after white-image filtering and optional `--start` selection.
- `--random-seed`: deterministic seed for `--sample-size`; defaults to `20260523` or `GENAI_AD_IMAGE_RANDOM_SEED`.
- `--ids`: comma-separated product ids to process.
- `--api-key`: runtime API key. Prefer `OPENAI_API_KEY` if you do not want the key in shell history.
- `--api-base-url`: defaults to `https://api.vectorengine.cn/v1`.
- `--endpoint`: final image-generation endpoint; defaults to the provider preset endpoint or `{api-base-url}/images/edits` / `{api-base-url}/responses`.
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
- v7 run root: `outputs/{model}_{selection_label}_{orientation_label}_v7_{timestamp}/`
- v8 run root: `outputs/{model}_{selection_label}_{orientation_label}_v8_{timestamp}/`
- v9 run root: `outputs/{model}_{selection_label}_{orientation_label}_v9_{timestamp}/`
- v10 run root: `outputs/{model}_{selection_label}_{orientation_label}_v10_{timestamp}/`
- v11 run root: `outputs/{model}_{selection_label}_{orientation_label}_v11_{timestamp}/`
- v12 run root: `outputs/{model}_{selection_label}_{orientation_label}_v12_{timestamp}/`
- v13 run root: `outputs/{model}_{selection_label}_{orientation_label}_v13_{timestamp}/`
- v14 rollout run root: `outputs/{model}_{selection_label}_{orientation_label}_v14_rollout3_{timestamp}/`
- v15 rollout run root: `outputs/{model}_{selection_label}_{orientation_label}_v15_rollout3_{timestamp}/`
- v2 refactor run root example: `outputs/{model}_{selection_label}_{orientation_label}_definition-control-v2_{timestamp}/`
- v3 refactor run root example: `outputs/{model}_{selection_label}_{orientation_label}_definition-control-v3_{timestamp}/`
- v16 run root: `outputs/{model}_{selection_label}_{orientation_label}_v16_{timestamp}/`
- v17 run root: `outputs/{model}_{selection_label}_{orientation_label}_v17_{timestamp}/`
- definition-only run root: `outputs/{model}_{selection_label}_{orientation_label}_definition-only_{timestamp}/`
- definition-only-v6 run root: `outputs/{model}_{selection_label}_{orientation_label}_definition-only-v6_{timestamp}/`
- definition-control run root: `outputs/{model}_{selection_label}_{orientation_label}_definition-control_{timestamp}/`
- definition-genprompt run root: `outputs/{model}_{selection_label}_{orientation_label}_definition-genprompt_{timestamp}/`
- definition-control-genprompt run root: `outputs/{model}_{selection_label}_{orientation_label}_definition-control-genprompt_{timestamp}/`
- backward-compatible names still available: `visual-control`, `genprompt-control`
- v16 neutral product prompts: `{run-dir}/base_prompts/{id}_neutral_prompt.txt`
- v17/definition-genprompt/definition-control-genprompt/genprompt-control orientation-specific generated prompts: `{run-dir}/base_prompts/{id}_{orientation}_prompt.txt`
- Generated images: `{run-dir}/generated/{orientation}/{id}_{orientation}.png`
- Multiround round1 images: `{run-dir}/generated/round1/{orientation}/{id}_{orientation}.png`
- Multiround round2 images: `{run-dir}/generated/round2/{orientation}/{id}_{orientation}.png`
- Multiround judgments: `{run-dir}/judgments/round1/` and `{run-dir}/judgments/round2/`
- Multiround revised prompts: `{run-dir}/revised_prompts/{orientation}/{id}_{orientation}.txt`
- Multiround manifest JSONL: `{run-dir}/multiround_manifest.jsonl`
- Multiround summary JSON: `{run-dir}/multiround_summary.json`
- Downloaded source images: `{run-dir}/source_images/{id}.{ext}`
- Manifest JSONL: `{run-dir}/generation_manifest.jsonl`
