# Prompt Aliases

This folder is the canonical runtime entry for the four research-condition families.

## Canonical families

- `def-*`
  - confirmed `definition-only` baseline
  - keep these unchanged as the theory-first core

- `dc-*`
  - `definition-control`
  - built by taking the confirmed `def-*` prompt and adding only the visual-control block

- `dg-*`
  - `definition-genprompt`
  - built by taking the confirmed `def-*` prompt, converting it into a product-specific generated prompt, and sending that generated prompt directly to image generation

- `dcg-*`
  - `definition-control-genprompt`
  - built by taking the same def-based generated prompt and embedding it into the `dc-*` wrapper

## Compatibility aliases

- `visual-control` as a version name is still supported by the script, but it now resolves to the `dc-*` family.
- `genprompt-control` as a version name is still supported by the script, but it now resolves to the `dcg-*` family.
- The legacy alias files `vc-*` and `gpc-*` are kept only as compatibility shortcuts and now point to the same def-based content as `dc-*` and `dcg-*`.

## Recommended runtime use

Use the canonical research-condition names:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-only
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-genprompt
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt
```

Manual one-orientation examples:

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-only --orientation Product-oriented --prompt-file prompts/aliases/def-product.txt
```

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control --orientation Product-oriented --prompt-file prompts/aliases/dc-product.txt
```

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-genprompt --orientation Product-oriented --base-prompt-file prompts/aliases/dg-product-gen.txt --prompt-file prompts/aliases/dg-product.txt
```

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt --orientation Product-oriented --base-prompt-file prompts/aliases/dcg-product-gen.txt --prompt-file prompts/aliases/dcg-product.txt
```

## Storage rule

- Research-condition runtime files live behind `prompts/aliases/*.txt`.
- Historical archived prompts live in `prompts/test/*.txt`.
- The script is now designed so research-condition versions load from `aliases`, while older historical versions can be resolved from `test` when root-level prompt files are absent.
