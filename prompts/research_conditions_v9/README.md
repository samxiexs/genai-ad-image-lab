# Research Conditions V9

This folder stores the BCM-stage-grounded `v9` definition-only research-condition prompt family.

Compared with `prompts/research_conditions_v8/`, this version keeps only the `definition-only` prompts.

Runtime version names:

- `definition-only-v9`

Note: the historical bare `--prompt-version v9` prompt family is left unchanged if defined elsewhere. Use `definition-only-v9` for this folderized BCM-stage-grounded version.

Folder layout:

- `product_oriented/`
- `function_oriented/`
- `symbolic_oriented/`
- `experiential_oriented/`

Each orientation folder contains:

- `definition-only.txt`

Design notes:

- `Product-oriented` and `Function-oriented` intentionally use the same functional definition and differ only in orientation label.
- `definition-only-v9` keeps the study definitions and uses a single BCM-stage-grounded explanation paragraph.
- Functional explanations emphasize introduction-stage functional performance, elaboration through problem-solving specialization/generalization, and fortification through performance-related products.
- Symbolic explanations emphasize introduction-stage group membership/self-identification, elaboration through market shielding, and fortification through lifestyle image extension.
- Experiential explanations emphasize introduction-stage sensory satisfaction/cognitive stimulation, elaboration through brand accessory/network strategies, and fortification through links to other experiential products; they also add one short sentence that human figures should not be deliberately used because the product itself can create visually stimulating sensory cues.
