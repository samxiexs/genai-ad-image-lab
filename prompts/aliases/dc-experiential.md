# dc / experiential

- Condition: `definition-control`
- Role: `single-stage prompt`
- Alias runtime file: `prompts/aliases/dc-experiential.txt`
- Original file: `prompts/test/experiential_oriented_ad_image_prompt.definition-control.txt`

## Prompt

```txt
You are generating one controlled Experiential-oriented advertising image for a consumer advertising study. Use the provided white-background product image as the source product reference.
Generate an Experiential-oriented image that communicates an experiential brand concept. Park, Jaworski, and MacInnis (1986) define a brand concept as a selected brand meaning derived from basic consumer needs. For this prompt, the dominant construct is experiential brand meaning. An experiential concept links the product to internally generated needs for sensory pleasure, variety, cognitive stimulation, immersion, or felt consumption experience.

Product metadata:
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Additional visual-control requirements:
- Preserve the source product's recognizable shape, color, material, logo, packaging, visible design, proportions, and physical structure. Do not redesign the product.
- Do not invent unsupported functions, claims, ingredients, certifications, awards, prices, ratings, badges, slogans, arrows, charts, QR codes, or brand assets.
- Do not add new readable text. Existing logos or package text already present on the source product may remain, but do not create new ad copy, labels, feature callouts, or rewritten package text.
- Keep the image realistic and photographic. Adapt lighting, shadow, perspective, reflections, and scale so the product looks physically present in the scene rather than pasted from a cutout.
- Make the product actively participate in one plausible felt experience or consumption moment. Show a believable relationship among the user, the product, and the surrounding experience, rather than decorative atmosphere alone.

Failure rule:
If the image mainly reads as a neutral product demo, a symbolic status scene, a generic lifestyle pose with no felt experience, or an unrealistic synthetic composite, generation has failed.
```
