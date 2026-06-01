# def / experiential

- Condition: `definition-only`
- Role: `single-stage prompt`
- Alias runtime file: `prompts/aliases/def-experiential.txt`
- Original file: `prompts/test/experiential_oriented_ad_image_prompt.definition-only.txt`

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
```
