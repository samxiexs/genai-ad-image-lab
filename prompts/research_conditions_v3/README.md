# Research Conditions V3

This folder stores the boundary-hardened refactor of the four research-condition families.

It is copied from `prompts/research_conditions_v2/` and then tightened at the cue-boundary level so the three brand-concept routes are less likely to collapse into mixed readings during generation.

Runtime version names:

- `definition-only-v3`
- `definition-control-v3`
- `visual-control-v3`
- `definition-genprompt-v3`
- `definition-control-genprompt-v3`
- `genprompt-control-v3`

Design summary:

- `definition-only-v3` remains the copied baseline from `v2`.
- `definition-control-v3` adds stronger dominant-inference and cue-boundary constraints.
- `definition-genprompt-v3` keeps the copied baseline prompt family but uses the tightened generator guidance.
- `definition-control-genprompt-v3` combines the tightened generator guidance with the tightened control wrapper.

These `-v3` versions are mapped directly by `scripts/generate_images/generate_from_csv.py` to the files in this folder.
