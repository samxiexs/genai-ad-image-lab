# Research Conditions V5

This folder stores the explanation-first `v5` refactor of the research-condition prompt families.

Compared with `prompts/research_conditions_v4/`, this version keeps the same folderized structure and matched visual-control block, but rewrites the condition-specific reasoning into a single explanation paragraph for each orientation.

Runtime version names:

- `definition-only-v5`
- `definition-control-v5`
- `visual-control-v5`
- `definition-genprompt-v5`
- `definition-control-genprompt-v5`
- `genprompt-control-v5`

Folder layout:

- `product_oriented/`
- `function_oriented/`
- `symbolic_oriented/`
- `experiential_oriented/`

Each orientation folder contains:

- `definition-only.txt`
- `definition-control.txt`
- `definition-genprompt.txt`
- `definition-control-genprompt.txt`
- `generator.definition-genprompt.txt`
- `generator.definition-control-genprompt.txt`

Design notes:

- `Product-oriented` and `Function-oriented` intentionally use the same functional definition and differ only in orientation label.
- `definition-only-v5` keeps the study definitions but replaces the old multi-part route instructions with one explanation paragraph.
- `definition-control-v5` and `definition-control-genprompt-v5` keep the same matched visual-control block across all orientations.
- `definition-genprompt-v5` and `definition-control-genprompt-v5` continue the same two-stage workflow as `v4`.
