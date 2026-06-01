# Prompt Aliases

This folder keeps a simplified, review-friendly copy of the requested research-condition prompts.

## Naming

- `def-*`: `definition-only` single-stage prompts.
- `gpc-*`: `genprompt-control` two-stage prompts.
- `gpc-*-gen.txt`: stage-1 generator prompt.
- `gpc-*.txt`: stage-2 final wrapper prompt.

## Recommended runtime use

For normal runs, the easiest and safest option is still the built-in version alias:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-only
python3 scripts/generate_images/generate_from_csv.py --prompt-version genprompt-control
```

That keeps the three orientations mapped automatically.

## Manual runtime use with the concise alias files

Use the concise alias files when you want to force one exact prompt file for one orientation.
Because `--prompt-file` overrides the prompt template for the current run, you should also specify the matching orientation.

### Definition-only example

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version definition-only \
  --orientation Product-oriented \
  --prompt-file prompts/aliases/def-product.txt
```

### Genprompt-control example

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version genprompt-control \
  --orientation Product-oriented \
  --base-prompt-file prompts/aliases/gpc-product-gen.txt \
  --prompt-file prompts/aliases/gpc-product.txt
```

Replace `Product-oriented` and the file stem with `Symbolic-oriented` / `symbolic` or `Experiential-oriented` / `experiential` as needed.

## Files in this folder

- `def-product.txt` / `def-product.md`
- `def-symbolic.txt` / `def-symbolic.md`
- `def-experiential.txt` / `def-experiential.md`
- `gpc-product-gen.txt` / `gpc-product-gen.md`
- `gpc-product.txt` / `gpc-product.md`
- `gpc-symbolic-gen.txt` / `gpc-symbolic-gen.md`
- `gpc-symbolic.txt` / `gpc-symbolic.md`
- `gpc-experiential-gen.txt` / `gpc-experiential-gen.md`
- `gpc-experiential.txt` / `gpc-experiential.md`

The `.txt` files are symlink aliases to the original runtime prompts. The `.md` files are review copies with the full prompt content in Markdown.
