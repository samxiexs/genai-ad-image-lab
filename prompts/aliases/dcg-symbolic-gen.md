# dcg / symbolic / gen

- Condition: `definition-control-genprompt`
- Role: `stage-1 generator prompt`
- Alias runtime file: `prompts/aliases/dcg-symbolic-gen.txt`
- Original file: `prompts/test/symbolic_oriented_ad_image_prompt_generator.definition-control-genprompt.txt`

## Prompt

```txt
You will convert the following definition-only Symbolic-oriented advertising prompt into one final image-generation prompt for the exact source product.

Base definition-only prompt:
You are generating one controlled Symbolic-oriented advertising image for a consumer advertising study. Use the provided white-background product image as the source product reference.

Generate a Symbolic-oriented image that communicates a symbolic brand concept. Park, Jaworski, and MacInnis (1986) define a brand concept as a selected brand meaning derived from basic consumer needs. For this prompt, the dominant construct is symbolic brand meaning. A symbolic concept links the product to internally generated needs for self-enhancement, role position, group membership, ego-identification, or desired self-image.

Product metadata:
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Task:
- Keep the same dominant construct and persuasive logic as the base definition-only prompt.
- Use the attached white-background product image and the product metadata to make the prompt specific to the actual product.
- Keep the source product recognizable and consistent with visible facts from the source image.
- Do not ask the image model to show price or promotion.
- Output one complete English image-generation prompt that can be sent directly to an image editing model with the same source product image.
- The final prompt should make viewers infer symbolic meaning rather than practical problem solving or experiential pleasure.

Output format:
Output only one complete English image-generation prompt. Do not include a title, explanation, bullets, numbering, or Markdown. Suggested length: 120-220 words.

Product metadata:
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}
```
