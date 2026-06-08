# Research Conditions V3 Rationale

## Scope

`v3` is a boundary-hardened revision of `prompts/research_conditions_v2/`.

It does **not** overwrite:

- the original research-condition files in `prompts/test/` and `prompts/aliases/`
- the independent `v2` refactor in `prompts/research_conditions_v2/`

Instead, it creates a new runnable family in `prompts/research_conditions_v3/` and the matching script versions:

- `definition-only-v3`
- `definition-control-v3`
- `visual-control-v3`
- `definition-genprompt-v3`
- `definition-control-genprompt-v3`
- `genprompt-control-v3`

## Why V3 Exists

`v2` already separated the three brand-concept routes at the definition level and kept visual-control requirements largely uniform. The main remaining risk was cue leakage:

- Functional images drifting into clean hero product displays
- Symbolic images drifting into generic upscale lifestyle scenes
- Experiential images drifting into pleasant atmosphere without product-linked sensation

`v3` hardens these boundaries with literature-grounded control additions.

## Modification Map

### 1. Single Dominant Inference

Added to:

- `*_ad_image_prompt.definition-control.txt`
- `*_ad_image_prompt.definition-control-genprompt.txt`
- `*_ad_image_prompt_generator.definition-genprompt.txt`
- `*_ad_image_prompt_generator.definition-control-genprompt.txt`

New rule:

`The image must support one dominant viewer inference. Secondary visual cues may appear only if they reinforce the target condition. Avoid mixed readings where viewers may equally infer practical utility, identity meaning, and felt experience.`

Rationale:

- Scott (1994) argues that advertising images should be treated as visual rhetoric rather than decoration, which implies that ambiguous multi-route readings are methodologically meaningful rather than neutral noise.
- Phillips and McQuarrie (2004) show that visual rhetoric creates interpretive complexity; for experimental manipulation, this means cue ambiguity should be deliberately reduced when one dominant meaning route is required.
- Liu and Chilton (2022, CHI) show that prompt structure systematically affects text-to-image results and failure modes, supporting a more explicit and uniform control skeleton across conditions.

### 2. Functional Cue Hardening

Added to functional files:

- `product_oriented_*definition-control*.txt`
- `function_oriented_*definition-control*.txt`
- corresponding generator files

New rule family:

- Do not merely show the product as a clean hero object or neutral product display.
- Show concrete visual evidence of task support, problem solving, friction reduction, preparation, protection, organization, or use context.
- Keep cues externally oriented and task-relevant.

Rationale:

- Park, Jaworski, and MacInnis (1986) define functional brand concepts around externally generated consumption needs and practical problem solving.
- Voss, Spangenberg, and Grohmann (2003) distinguish utilitarian value from hedonic value, supporting the need to make utility visually diagnostic rather than merely making the product salient.

### 3. Symbolic Cue Hardening

Added to symbolic files:

- `symbolic_oriented_*definition-control*.txt`
- corresponding generator files

New rule family:

- Symbolic cues must be identity-diagnostic.
- They should imply role, taste, aspiration, group affiliation, self-presentation, or desired self-image.
- They should not collapse into merely attractive lifestyle imagery.

Rationale:

- Park et al. (1986) define symbolic brand concepts in terms of self-enhancement, role position, group membership, and ego-identification.
- Escalas and Bettman (2003; 2005) show that brands become linked to self-concept and reference groups, supporting the requirement that symbolic cues should diagnose how a person is seen or sees themselves.

### 4. Experiential Cue Hardening

Added to experiential files:

- `experiential_oriented_*definition-control*.txt`
- corresponding generator files

New rule family:

- Experiential cues must be product-contingent.
- Felt experience must appear to arise from encountering, touching, wearing, tasting, smelling, using, or consuming the specific product.
- Pleasant background atmosphere alone is insufficient.

Rationale:

- Holbrook and Hirschman (1982) frame experiential consumption in terms of fantasies, feelings, and fun, rather than generic scene attractiveness.
- MacInnis and Price (1987) show that imagery processing can activate multisensory, scene-based mental simulation, which supports using concrete sensory cues tied to product encounter rather than background beauty alone.

### 5. Generator-Level Specificity

Added to generator files in both:

- `definition-genprompt-v3`
- `definition-control-genprompt-v3`

New rule family:

- Prompt generation must preserve one dominant inference.
- Allowed cues are specified more concretely for each condition.
- Avoided cues are stated more explicitly.

Rationale:

- RePrompt (CHI 2023) supports more concrete prompt editing and cue-explicit rewriting as a way to improve alignment between intended expression and generated output.
- Liu and Chilton (2022, CHI) further support prompt-structure sensitivity in text-to-image generation, motivating explicit decomposition of allowed and avoided cue families.

## What Stayed Constant From V2

The following control block remained intentionally uniform across the three conditions:

- preserve source product identity
- do not redesign the product
- do not invent unsupported claims, functions, or brand assets
- do not add new readable text
- maintain realistic photographic integration
- preserve manipulation at the concept-route level rather than product-identity level

This continuity is intentional. `v3` changes cue-boundary logic, not product-fidelity logic.

## Recommended Interpretation in the Paper

The manipulation should be described as:

`AI-generated advertising image framing along three brand-concept routes: functional utility, symbolic identity, and experiential sensation.`

This framing keeps the study focused on dominant meaning routes in ad images rather than on product-category differences.
