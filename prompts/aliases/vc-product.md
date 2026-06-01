# vc / product

- Condition: `visual-control`
- Role: `legacy compatibility alias for definition-control`
- Alias runtime file: `prompts/aliases/vc-product.txt`
- Original file: `prompts/test/product_oriented_ad_image_prompt.definition-control.txt`

## Prompt

```txt
You are generating one controlled Product-oriented advertising image for a consumer advertising study. Use the provided white-background product image as the source product reference.

Generate a Product-oriented image that communicates a functional brand concept. Park, Jaworski, and MacInnis (1986) define a brand concept as a selected brand meaning derived from basic consumer needs. For this prompt, the dominant construct is functional brand meaning. A functional concept links the product to externally generated consumption needs, such as solving a current problem, preventing a potential problem, reducing friction, supporting a practical task, or making consumption more reliable.

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
