# Research Conditions V8

This folder stores the BCM-stage-grounded `v8` refactor of the research-condition prompt families.

Compared with `prompts/research_conditions_v7/`, this version keeps the folderized structure, matched visual-control block, and prompt-oriented explanation style from the earlier successful v7 run, but adds one short experiential-control sentence to reduce unnecessary human figures in Experiential-oriented images.

Runtime version names:

- `definition-only-v8`
- `definition-control-v8`
- `visual-control-v8`
- `definition-genprompt-v8`
- `definition-control-genprompt-v8`
- `genprompt-control-v8`

Note: the historical bare `--prompt-version v8` prompt family is left unchanged. Use the explicit `*-v8` names above for this folderized BCM-stage-grounded version.

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
- `definition-only-v8` keeps the study definitions and uses a single BCM-stage-grounded explanation paragraph.
- Functional explanations emphasize introduction-stage functional performance, elaboration through problem-solving specialization/generalization, and fortification through performance-related products.
- Symbolic explanations emphasize introduction-stage group membership/self-identification, elaboration through market shielding, and fortification through lifestyle image extension.
- Experiential explanations emphasize introduction-stage sensory satisfaction/cognitive stimulation, elaboration through brand accessory/network strategies, and fortification through links to other experiential products; they also add one short sentence that human figures should not be deliberately used because the product itself can create visually stimulating sensory cues.
- `definition-control-v8` and `definition-control-genprompt-v8` keep the same matched visual-control block across all orientations.
- `definition-genprompt-v8` and `definition-control-genprompt-v8` continue the same two-stage workflow as `v5`.
