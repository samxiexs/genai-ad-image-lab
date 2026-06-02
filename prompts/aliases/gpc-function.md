# gpc / function

- Condition: `genprompt-control`
- Role: `legacy compatibility final wrapper alias for definition-control-genprompt`
- Alias runtime file: `prompts/aliases/gpc-function.txt`
- Original file: `prompts/test/function_oriented_ad_image_prompt.definition-control-genprompt.txt`

## Prompt

```txt
You are generating one controlled Function-oriented advertising image for a consumer advertising study.

Part 1: Function-specific prompt generated from the confirmed definition-only Function-oriented condition
The following prompt was generated from the white-background source product image, the product metadata, and the confirmed definition-only prompt. Use it as the product-specific concept plan for the final image.

{generated_orientation_prompt}

Part 2: The final image must still satisfy the following definition-first prompt plus the added visual-control requirements.
If Part 1 and Part 2 conflict, follow Part 2.

You are generating one controlled Function-oriented advertising image for a consumer advertising study. Use the provided white-background product image as the source product reference.

Generate a Function-oriented image that communicates a functional brand concept. Park, Jaworski, and MacInnis (1986) define a brand concept as a selected brand meaning derived from basic consumer needs. For this prompt, the dominant construct is functional brand meaning. A functional concept links the product to externally generated consumption needs, such as solving a current problem, preventing a potential problem, reducing friction, supporting a practical task, or making consumption more reliable.

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
- Make the product the dominant subject and show a plausible category-appropriate cue for practical utility, such as use, handling, scale, material detail, storage, setup, or another visible sign of function.

Failure rule:
If the image mainly reads as symbolic identity expression, experiential atmosphere, a plain white packshot, or an unrealistic synthetic composite, generation has failed.
```
