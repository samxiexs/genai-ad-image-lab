# Research Conditions V7

This folder stores the BCM-stage-grounded `v7` refactor of the research-condition prompt families.

Compared with `prompts/research_conditions_v5/`, this version keeps the same folderized structure and matched visual-control block, but replaces each orientation's freeform explanation paragraph with a source-grounded prompt-oriented explanation derived from brand concept management stages: introduction, elaboration, and fortification.

Runtime version names:

- `definition-only-v7`
- `definition-control-v7`
- `visual-control-v7`
- `definition-genprompt-v7`
- `definition-control-genprompt-v7`
- `genprompt-control-v7`

Note: the historical bare `--prompt-version v7` prompt family is left unchanged. Use the explicit `*-v7` names above for this folderized BCM-stage-grounded version.

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
- `definition-only-v7` keeps the study definitions and uses a single BCM-stage-grounded explanation paragraph.
- Functional explanations emphasize introduction-stage functional performance, elaboration through problem-solving specialization/generalization, and fortification through performance-related products.
- Symbolic explanations emphasize introduction-stage group membership/self-identification, elaboration through market shielding, and fortification through lifestyle image extension.
- Experiential explanations emphasize introduction-stage sensory satisfaction/cognitive stimulation, elaboration through brand accessory/network strategies, and fortification through links to other experiential products.
- `definition-control-v7` and `definition-control-genprompt-v7` keep the same matched visual-control block across all orientations.
- `definition-genprompt-v7` and `definition-control-genprompt-v7` continue the same two-stage workflow as `v5`.
