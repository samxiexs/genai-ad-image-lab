# Research Conditions V6

This folder stores the `definition-only-v6` multiround prompt family.

It is intentionally separate from the existing historical runtime version name
`v6`. The old `--prompt-version v6` remains unchanged. This folder is used only
by the new runtime version name:

- `definition-only-v6`

Folder layout:

- `product_oriented/`
- `function_oriented/`
- `symbolic_oriented/`
- `experiential_oriented/`

Each orientation folder contains:

- `definition-only.txt`
- `judge.txt`
- `revise.txt`

Design notes:

- `definition-only.txt` starts from the concise `v4` definition-only wording.
- `judge.txt` is used only by the multiround evaluation loop.
- `revise.txt` is used only by the multiround prompt-revision loop.
- `Product-oriented` and `Function-oriented` keep the same functional concept
  definition while preserving their separate labels.
