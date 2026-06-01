# Definition-only / Symbolic-oriented

- Condition: `definition-only`
- Role: `single-stage prompt`
- Alias runtime file: `prompts/aliases/def-symbolic.txt`
- Original file: `prompts/symbolic_oriented_ad_image_prompt.definition-only.txt`

## Prompt

```txt
You are generating one controlled Symbolic-oriented advertising image for a consumer advertising study.

Use the provided white-background product image as the source product reference.

Product metadata:
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Generate a Symbolic-oriented image that communicates a symbolic brand concept.

Park, Jaworski, and MacInnis (1986) define a brand concept as a selected brand meaning derived from basic consumer needs. For this prompt, the dominant construct is symbolic brand meaning. A symbolic concept links the product to internally generated needs for self-enhancement, role position, group membership, ego-identification, or desired self-image.

Let this symbolic meaning be the main reason the image is persuasive. The image should make viewers infer what choosing, owning, displaying, carrying, wearing, gifting, or valuing the product expresses about identity, taste, role, belonging, aspiration, or self-image, rather than mainly reading the image as a functional explanation or sensory experience.

Failure rule:
If the image mainly reads as practical problem solving or felt experiential pleasure instead of symbolic meaning, generation has failed.

```
