# def / product

- Condition: `definition-only`
- Role: `single-stage prompt`
- Alias runtime file: `prompts/aliases/def-product.txt`
- Original file: `prompts/test/product_oriented_ad_image_prompt.definition-only.txt`

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
```
