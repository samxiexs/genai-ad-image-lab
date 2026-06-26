# Research Conditions V10

This folder stores the BCM-stage-grounded `v10` definition-only research-condition prompt family.

Compared with `prompts/research_conditions_v9/`, this version keeps the same definition-only structure for further explanation refinement.

Runtime version names:

- `definition-only-v10`

Note: the historical bare `--prompt-version v10` prompt family is left unchanged if defined elsewhere. Use `definition-only-v10` for this folderized BCM-stage-grounded version.

Folder layout:

- `product_oriented/`
- `function_oriented/`
- `symbolic_oriented/`
- `experiential_oriented/`

Each orientation folder contains:

- `definition-only.txt`

Design notes:

- `Product-oriented` and `Function-oriented` intentionally use the same functional definition and differ only in orientation label.
- `definition-only-v10` keeps the study definitions and uses a single BCM-stage-grounded explanation paragraph.
- Functional explanations emphasize functional performance, problem-solving specialization/generalization, and performance-related products.
- Symbolic explanations emphasize self-identification, symbolic reference groups, exclusivity, and lifestyle image extension.
- Experiential explanations emphasize sensory satisfaction/cognitive stimulation, experiential and fantasy aspects of consumption, related stimulation, and links to other experiential products.
