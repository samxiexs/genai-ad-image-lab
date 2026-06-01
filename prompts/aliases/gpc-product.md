# Genprompt-control / Product-oriented / Final Wrapper

- Condition: `genprompt-control`
- Role: `stage-2 final wrapper prompt`
- Alias runtime file: `prompts/aliases/gpc-product.txt`
- Original file: `prompts/product_oriented_ad_image_prompt.genprompt-control.txt`

## Prompt

```txt
You are generating controlled experimental stimuli for a consumer advertising study. Use the provided white-background product image as the exact source product. You may adjust the presentation style, but keep the image natural and photographic. Do not show any price-related information.

Part 1: Product-specific Product-oriented prompt
The following content has already been generated from the product metadata, the white-background source image, and the Product-oriented brand-concept orientation. It provides product facts plus an orientation-specific functional visual plan. Use it as product and execution grounding, but the final image must still be dominated by the functional definition in Part 2.

{generated_orientation_prompt}

Part 2: Functional style definition and generation requirements
The advertising image style is based on the functional brand concept from Park, Jaworski, and MacInnis (1986). A functional concept links the product to externally generated consumption needs: solving or preventing a consumption problem, reducing friction, supporting a practical task, or making consumption more reliable.

While preserving the product facts and visual plan from Part 1, transform the image into a Product-oriented advertising image. The dominant message should be what the product does, what practical task it supports, what consumption problem it solves, or how it makes use more reliable. The image must feel like a controlled commercial product-function demonstration, not a single beautified product shot.

Function reasoning requirements:
- Preserve the specific product facts from Part 1 and the source image.
- Show multiple functional evidence dimensions rather than one generic function. Use category-appropriate cues such as operation/interface, assembly/setup, fit/fastening, scale reference, portability, storage, cleaning, protection, compatibility, freshness, application, organization, comfort, durability, care, ease of use, or gift-readiness.
- Select only dimensions that fit the actual product and category. Do not mechanically include every example.
- For decorative, wearable, luxury, or giftable products with limited mechanical function, express practical value through fit, fastening, scale, wearing support, safe storage, material handling, packaging protection, pairing, care, or gift-readiness.

Visual direction:
- Make the product the dominant subject and show concrete functional evidence cues.
- Use a controlled product-demonstration composition, such as a neutral tabletop, clean studio work surface, organized component layout, realistic open/closed state, visible mechanism, scale reference, accessory relationship, safe storage, material surface contrast, before/after state, or a hand form used only to clarify grip, fit, fastening, application, or scale.
- A secondary close-detail area or layered composition is acceptable if it feels like part of one commercial product photograph and contains no labels, arrows, callouts, or text.
- Relevant neutral props may appear only when they explain function. Props must behave like functional evidence, not lifestyle decoration or symbolic atmosphere.

Photographic quality requirements:
- Follow a complete high-quality image prompt structure in execution: clear subject, concrete scene, realistic commercial photography style, camera/lens language, atmosphere, and detail refinements.
- Use realistic optical behavior: physically plausible key light and fill light, coherent cast shadows, visible contact shadows where objects touch surfaces, realistic reflections, natural material texture, accurate scale, and believable depth of field.
- The image should look like a real product photograph captured in-camera with careful studio lighting, not a CGI render, plastic mockup, over-smoothed AI image, or synthetic composite.

Strict requirements:
- The product must be clearly visible and identifiable, while preserving the source image's core shape, color, logo, packaging, materials, and physical structure.
- Do not invent functions, ingredients, certifications, awards, ratings, comparative conclusions, or brand assets that are unsupported by the source image or category.
- Do not generate new readable text, slogans, prices, promotions, labels, arrows, charts, QR codes, callouts, or badges.
- Do not let premiumness, identity signaling, emotional atmosphere, gifting mood, or sensory experience become the dominant message.
- Do not simply upscale, clean up, or restage the original white-background packshot. The output must visibly add the functional demonstration composition requested above.
- Avoid artificial gloss, inconsistent shadows, floating objects, distorted geometry, warped logos, fake reflections, unreadable text artifacts, and any synthetic or uncanny visual feel.
- The image should look like realistic commercial photography, not a screenshot, low-quality collage, meme, cluttered e-commerce mockup, or unnatural composite.

```
