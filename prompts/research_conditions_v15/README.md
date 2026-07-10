# Research Conditions V15

This folder contains the literature-grounded `v15` research-condition prompts. Both `--prompt-version v15` and `--prompt-version definition-only-v15` resolve to these files.

## Folder Layout

- `product_oriented/definition-only.txt`
- `symbolic_oriented/definition-only.txt`
- `experiential_oriented/definition-only.txt`

Each prompt preserves the Park et al. (1986) brand-concept definition, uses one compact explanation paragraph, keeps the `symbolic` metadata control, requests a square image, and prohibits newly added readable text.

## Source Boundary

Park et al. (1986) directly defines functional, symbolic, and experiential brand concepts. Homburg, Schwemmle, and Kuehnl (2015) directly supports the visual operationalization of functionality and symbolism, but it does not define Park's experiential brand concept. The experiential explanation therefore relies primarily on Park et al.; its active-use and person-framing rules are documented below as experiment-specific narrowing rather than attributed to Homburg et al.

Page references use the articles' printed journal page numbers:

- Park, Jaworski, and MacInnis (1986): pp. 136, 140-141.
- Homburg, Schwemmle, and Kuehnl (2015): pp. 44, 46-47.

## Sentence-Level Evidence Map

### Product-oriented Explanation

| Sentence | Source basis | Status and narrowing rationale |
| --- | --- | --- |
| 1. Emphasize functional performance in solving consumption-related problems. | Park et al. (1986), p. 140: functional positioning emphasizes performance in solving consumption-related problems. | Direct theory-grounded paraphrase. |
| 2. Make what the product does, how it is used, and whether it can fulfill its purpose inferable from looking. | Homburg et al. (2015), p. 44 defines functionality as perceived ability to fulfill purpose; p. 46 reports that functional design reveals what products do, implies how to use them, and whether they do their job. | Direct theory-grounded paraphrase adapted to an image-generation instruction. |
| 3. Use a coherent multi-panel grid with connected product-centered functional views. | Homburg et al. (2015), pp. 44, 46 supports visual inference of purpose, use, and performance. | Experiment-specific narrowing: multiple panels expose several observable functional cues while preserving the successful v15 Product composition. The article does not prescribe a grid. |
| 4. Show a specific need or performance across related usage situations. | Park et al. (1986), pp. 140-141 distinguishes problem-solving specialization from generalization across usage situations. | Theory-grounded visual operationalization. |
| 5. Keep the product dominant and separate functional inference from symbolic or experiential inference. | Park et al. (1986), p. 136 explains that combining concepts can obscure a brand's basic meaning. | Experiment-specific control for construct separation; person prominence is restricted so it cannot become the main identity cue. |

### Experiential-oriented Explanation

| Sentence | Source basis | Status and narrowing rationale |
| --- | --- | --- |
| 1. Convey sensory satisfaction or cognitive stimulation and experiential aspects of consumption. | Park et al. (1986), pp. 136, 140 defines experiential needs and states that positioning should convey sensory satisfaction or cognitive stimulation while highlighting experiential aspects associated with consumption. | Direct theory-grounded paraphrase. |
| 2. Show a believable, currently occurring moment of active use or consumption rather than an isolated product or atmosphere. | Park et al. (1986), p. 140 centers experiential positioning on effects and experiential aspects associated with consumption. | Experiment-specific narrowing: visible active use makes the consumption experience observable and avoids an unsupported atmosphere-only proxy. |
| 3. Keep the product and action clear while making the person anonymous and secondary. | Park et al. (1986), p. 136 distinguishes experiential stimulation from symbolic self-image, role, and group membership. | Experiment-specific control: back views, cropped bodies, hands, or first-person views retain human use without creating a salient identity treatment. |
| 4. Use realistic sensory and situational cues without turning the image into a functional-efficiency demonstration. | Park et al. (1986), pp. 136, 140 separates experiential stimulation from functional problem-solving. | Theory-grounded construct-separation rule plus an experiment-specific realism requirement. |
| 5. Make the primary inference the felt experience of use, not practical problem-solving or identity communication. | Park et al. (1986), p. 136 defines the three concepts through distinct consumer needs and warns that mixed concepts make basic meaning harder to identify. | Experiment-specific manipulation check stated as the intended dominant inference. |

### Symbolic-oriented Explanation

| Sentence | Source basis | Status and narrowing rationale |
| --- | --- | --- |
| 1. Emphasize the product's relationship to group membership or self-identification. | Park et al. (1986), p. 140 states that symbolic positioning can emphasize group membership or self-identification. | Direct theory-grounded paraphrase. |
| 2. Communicate self-image to the consumer and others through roles, groups, lifestyle, values, dispositions, place or time, or a distinctive image. | Park et al. (1986), p. 136 identifies group, role, and self-image; Homburg et al. (2015), p. 44 defines symbolic design as a self-image message to oneself and others and discusses values, dispositions, identity, and place/time associations. | Direct synthesis of the two articles without reducing symbolism to status alone. |
| 3. Use one product-only route or one representative-person route. | Homburg et al. (2015), p. 44 grounds symbolic meaning in visual product elements; Park et al. (1986), p. 136 grounds it in association with a desired group, role, or self-image. | Experiment-specific narrowing: one coherent route reduces mixed or competing identity signals. The articles do not prescribe these two layouts. |
| 4. Do not default to success, executive, or luxury-business stereotypes. | Park et al. (1986), p. 136 provides several symbolic need types; Homburg et al. (2015), p. 44 includes values, dispositions, identity, and place/time associations, while p. 47 treats achievement as only one possible item. | Experiment-specific anti-stereotype control: it prevents one narrow achievement cue from dominating the broader symbolic construct; category-grounded use remains possible when genuinely appropriate. |
| 5. Keep the product as the symbolic source and separate symbolic inference from function or sensory stimulation. | Park et al. (1986), p. 136 distinguishes symbolic, functional, and experiential concepts; Homburg et al. (2015), pp. 44, 46 defines symbolic design as what the product communicates about self-image. | Theory-grounded construct-separation rule expressed as the intended dominant inference. |

## Common Controls

- If `Symbolic` is true, retain real branding visible in the source image.
- If `Symbolic` is false, naturally remove or obscure branding so the product appears unbranded.
- Preserve a square 1:1 output format.
- Do not add new readable text inside the generated image.
- Keep the product recognizable from the provided white-background reference.
