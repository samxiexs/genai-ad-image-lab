# Research Conditions V16

This folder contains the runnable `v16` research-condition prompts. Both
`--prompt-version v16` and `--prompt-version definition-only-v16` resolve to
these files.

## Folder Layout

- `product_oriented/definition-only.txt`
- `symbolic_oriented/definition-only.txt`
- `experiential_oriented/definition-only.txt`

V16 retains the Park et al. (1986) functional, symbolic, and experiential
definitions. Each Explanation then adds a small number of evidence-mapped
visual operationalizations. These controls narrow the generated image toward
the target concept without asserting that a source article literally prescribes
the chosen layout or viewpoint.

## Intended Readings

- Product-oriented: functional performance in solving externally generated
  consumption problems, presented through connected product-centred panels.
- Symbolic-oriented: association with a desired group, role, or self-image,
  made visible through product-grounded identity cues.
- Experiential-oriented: sensory satisfaction, cognitive stimulation, variety,
  and experiential consumption, rendered through a participant-centred use
  episode when the category permits it.

## Evidence and Boundary

`docs/v16_prompt_rationale.md` records the source basis, the reasoning chain,
and the boundary of every V16 operationalization. Functional panel layouts and
participant-centred viewpoints are explicitly labelled as research-design
choices rather than visual formats prescribed by Park et al.

## Common Controls

- If `Symbolic` is true, retain real branding visible in the source image.
- If `Symbolic` is false, naturally remove or obscure branding so the product
  appears unbranded.
- Preserve a square 1:1 output format.
- Do not add new readable text inside the generated image.
- Keep the product recognizable from the provided white-background reference.
