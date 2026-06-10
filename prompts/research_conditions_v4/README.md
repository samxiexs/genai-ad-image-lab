# Research Conditions V4

This folder stores the folderized `v4` refactor of the research-condition prompt families.

Compared with `prompts/research_conditions_v3/`, this version makes two deliberate design changes:

- Each orientation has its own dedicated subdirectory.
- The visual-control block is kept literally identical across all orientations so the control layer is truly matched.

Runtime version names:

- `definition-only-v4`
- `definition-control-v4`
- `visual-control-v4`
- `definition-genprompt-v4`
- `definition-control-genprompt-v4`
- `genprompt-control-v4`

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
- `definition-only-v4` updates the three concept definitions using the current study wording.
- `definition-control-v4` and `definition-control-genprompt-v4` keep the visual-control requirements exactly identical across all four orientations.
- `definition-genprompt-v4` and `definition-control-genprompt-v4` continue the two-stage workflow used by the generator script.
