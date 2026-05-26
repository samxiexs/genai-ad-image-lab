# Three Orientation Prompt Design v4/v5/v6

This document defines the v4, v5, and v6 prompt logic for generating three controlled advertising-image orientations from the same white-background product image. Runtime API calls use the English `.txt` prompt files through `--prompt-version v4`, `--prompt-version v5`, or `--prompt-version v6`; Chinese `.zh.md` files are companion review versions for research discussion.

## Theoretical Basis

The v4, v5, and v6 prompt sets are grounded in Park, Jaworski, and MacInnis (1986)'s brand concept-image management framework. In their framework, a brand concept is a firm-selected brand meaning derived from basic consumer needs. The prompt therefore starts from concept definitions rather than from long lists of visual micro-details.

| Park et al. concept | v4/v5/v6 orientation | Advertising-image translation | Primary consumer response |
| --- | --- | --- | --- |
| Functional | `Product-oriented` | Product linked to externally generated consumption problems or practical tasks | Functional value clarity |
| Symbolic | `Symbolic-oriented` | Product linked to self-image, role, group, identity, or ego-identification needs | Symbolic meaning and self-expression |
| Experiential | `Experiential-oriented` | Product linked to sensory pleasure, variety, cognitive stimulation, or felt experience | Experiential value and stimulation |

`Context-oriented` is not a v4/v5/v6 theory label. It remains accepted only as a deprecated alias that maps to `Experiential-oriented` when `--prompt-version v4`, `--prompt-version v5`, or `--prompt-version v6` is used. Older `current` and `function_v2` runs keep their original `Product-oriented`, `Context-oriented`, and `Symbolic-oriented` orientation set.

## Shared Prompt Discipline

All three v6 prompts restore a compact set of experimental controls after the concept-only v5 test:

- Keep the source product identity constant: shape, material, color, packaging, logo, visible design, and physical structure.
- Do not invent product functions, ingredients, materials, certifications, awards, claims, slogans, ratings, prices, QR codes, badges, charts, arrows, or brand assets.
- Do not generate new readable text inside the image.
- Keep the product visually prominent and recognizable.
- Avoid unsupported demographic assumptions and overly specific visual micro-scenes.
- Allow composition, background, lighting, and style only when they support the selected brand concept and do not contradict the product facts.

This follows the prompt-control logic summarized in `local_only/prompt-ref.md`: structured concept-image linkage should carry the experimental manipulation, while product identity and non-concept constraints stay stable across conditions.

The v4 prompts are concise definition-first prompts with input grounding and generalization discipline. The v5 prompts are concept-only prompts that keep only the Park brand-concept definition block. The v6 prompts are the recommended balanced version: they restore subject preservation, no unsupported claims/text, product prominence, and concept-image linkage while avoiding the long micro-detail lists from v3.

## Orientation Separation Logic

Each v6 prompt defines one dominant concept route and keeps the other two routes non-dominant:

| Orientation | Dominant mechanism | Suppressed dominant impressions |
| --- | --- | --- |
| `Product-oriented` | Functional product-problem linkage | Symbolic identity and experiential stimulation |
| `Symbolic-oriented` | Self-image, role, group, or identity meaning | Functional explanation and sensory stimulation |
| `Experiential-oriented` | Sensory pleasure, variety, cognitive stimulation, or felt experience | Practical problem solving and symbolic identity |

This makes manipulation checks interpretable. A failed image is not just an aesthetic failure; it is usually a concept-contamination failure.

## Runtime Files

| Purpose | File |
| --- | --- |
| Product English runtime prompt v4 | `prompts/product_oriented_ad_image_prompt.v4.txt` |
| Symbolic English runtime prompt v4 | `prompts/symbolic_oriented_ad_image_prompt.v4.txt` |
| Experiential English runtime prompt v4 | `prompts/experiential_oriented_ad_image_prompt.v4.txt` |
| Product English runtime prompt v5 | `prompts/product_oriented_ad_image_prompt.v5.txt` |
| Symbolic English runtime prompt v5 | `prompts/symbolic_oriented_ad_image_prompt.v5.txt` |
| Experiential English runtime prompt v5 | `prompts/experiential_oriented_ad_image_prompt.v5.txt` |
| Product English runtime prompt v6 | `prompts/product_oriented_ad_image_prompt.v6.txt` |
| Symbolic English runtime prompt v6 | `prompts/symbolic_oriented_ad_image_prompt.v6.txt` |
| Experiential English runtime prompt v6 | `prompts/experiential_oriented_ad_image_prompt.v6.txt` |
| Product Chinese review prompt v4 | `prompts/product_oriented_ad_image_prompt.v4.zh.md` |
| Symbolic Chinese review prompt v4 | `prompts/symbolic_oriented_ad_image_prompt.v4.zh.md` |
| Experiential Chinese review prompt v4 | `prompts/experiential_oriented_ad_image_prompt.v4.zh.md` |
| Product Chinese review prompt v5 | `prompts/product_oriented_ad_image_prompt.v5.zh.md` |
| Symbolic Chinese review prompt v5 | `prompts/symbolic_oriented_ad_image_prompt.v5.zh.md` |
| Experiential Chinese review prompt v5 | `prompts/experiential_oriented_ad_image_prompt.v5.zh.md` |
| Product Chinese review prompt v6 | `prompts/product_oriented_ad_image_prompt.v6.zh.md` |
| Symbolic Chinese review prompt v6 | `prompts/symbolic_oriented_ad_image_prompt.v6.zh.md` |
| Experiential Chinese review prompt v6 | `prompts/experiential_oriented_ad_image_prompt.v6.zh.md` |
| Structured prompt registry | `prompts/orientation_prompts.json` |

## Dry-Run Commands

Render all three v4 prompts without calling the image API:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v4 \
  --dry-run \
  --limit 1 \
  --no-progress
```

Render a single experiential prompt:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v4 \
  --orientation Experiential-oriented \
  --dry-run \
  --limit 1 \
  --no-progress
```

Legacy context alias under v4:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v4 \
  --orientation Context-oriented \
  --dry-run \
  --limit 1 \
  --no-progress
```

In the last command, the manifest and rendered `{orientation}` value use `Experiential-oriented`, while `requested_orientation` records `Context-oriented`.

Render the concept-only v5 prompts:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v5 \
  --dry-run \
  --limit 1 \
  --no-progress
```

Render the balanced v6 prompts:

```bash
python3 scripts/generate_images/generate_from_csv.py \
  --prompt-version v6 \
  --dry-run \
  --limit 1 \
  --no-progress
```

## Manipulation-Check Anchors

| Orientation | Should score high | Should score low for discriminant validity |
| --- | --- | --- |
| `Product-oriented` | Practical problem solving; functional value clarity; product-problem fit | Self-image meaning; sensory or cognitive stimulation |
| `Symbolic-oriented` | Symbolic meaning; role/group/self-image fit; self-expression | Functional explanation; sensory stimulation as the main message |
| `Experiential-oriented` | Sensory pleasure; variety; immersion; cognitive stimulation; felt experience | Practical problem solving; role/group/status signaling |

Suggested high-score items:

| Orientation | Items |
| --- | --- |
| `Product-oriented` | "This image helps me understand what practical problem the product solves." / "This image makes the product's functional value clear." |
| `Symbolic-oriented` | "This image communicates what the product symbolizes." / "This image expresses a role, group, or self-image meaning." |
| `Experiential-oriented` | "This image communicates the experience the product can provide." / "This image evokes sensory pleasure, variety, or stimulation." |

## Literature Rationale

- Park et al. (1986) supplies the definition-first classification: functional, symbolic, and experiential brand concepts.
- ControlNet, T2I-Adapter, GLIGEN, BoxDiff, DenseDiffusion, MultiDiffusion, InteractDiffusion, and Ranni support separating semantic intent, objects, layout, and interaction constraints instead of relying on ad hoc detail lists.
- Prompt-to-Prompt, Attend-and-Excite, OPT2I, and RePrompt support minimal concept-specific prompt changes while keeping product facts and generation constraints stable.
- DreamBooth, Textual Inversion, and VGD support treating the source product as a grounded/reference subject while the prompt focuses on brand meaning.
- Discrete Prompt Optimization, Learning to Sample Effective and Diverse Prompts, and DPO-Diff support avoiding unsupported style suffixes and optimizing for concept-image consistency.
