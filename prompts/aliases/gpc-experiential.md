# Genprompt-control / Experiential-oriented / Final Wrapper

- Condition: `genprompt-control`
- Role: `stage-2 final wrapper prompt`
- Alias runtime file: `prompts/aliases/gpc-experiential.txt`
- Original file: `prompts/experiential_oriented_ad_image_prompt.genprompt-control.txt`

## Prompt

```txt
You are generating controlled experimental stimuli for a consumer advertising study. Use the provided white-background product image as the exact source product. You may adjust the presentation style, but keep the image natural and photographic. Do not show any price-related information.

Part 1: Product-specific Experiential-oriented prompt
The following content has already been generated from the product metadata, the white-background source image, and the Experiential-oriented brand-concept orientation. It provides product facts plus an orientation-specific experiential visual plan. Use it as product and execution grounding, but the final image must still be dominated by the experiential definition in Part 2.

{generated_orientation_prompt}

Part 2: Experiential style definition and generation requirements
The advertising image style is based on the experiential brand concept from Park, Jaworski, and MacInnis (1986). An experiential concept links the product to internally generated needs for sensory pleasure, variety, cognitive stimulation, immersion, or felt consumption experience.

While preserving the product facts and visual plan from Part 1, transform the image into an Experiential-oriented advertising image. The dominant message should be what the product feels like to consume or engage with, not merely where it is used or what functions it has. The image should help viewers imagine sensory pleasure, variety, cognitive stimulation, immersion, relaxation, excitement, delight, curiosity, or another felt consumption experience compatible with the product and category.

Visual direction:
- The product must remain central to the felt experience and clearly recognizable.
- Use atmosphere, implied motion, depth of field, rhythm, texture, light, color, interaction, or immersive context to communicate the felt experience.
- The image must visibly move beyond the original white-background packshot by adding an experiential advertising scene around the product.
- Include or preserve a clear experiential visual device from Part 1, such as motion trails, immersive lighting, tactile material context, sensory particles, depth-rich environment, use-moment interaction, rhythmic arrangement, atmospheric glow, or another product-compatible felt-experience device.

Photographic quality requirements:
- Follow a complete high-quality image prompt structure in execution: clear subject, concrete scene, realistic commercial photography style, camera/lens language, atmosphere, and detail refinements.
- Use realistic optical behavior: physically plausible key light and fill light, coherent cast shadows, visible contact shadows where objects touch surfaces, realistic reflections, natural material texture, accurate scale, and believable depth of field.
- The image should look like a real immersive advertising photograph captured in-camera with careful studio or location lighting, not a CGI render, plastic mockup, over-smoothed AI image, or synthetic composite.

Strict requirements:
- The product must be clearly visible and identifiable, while preserving the source image's core shape, color, logo, packaging, materials, and physical structure.
- Do not invent functions, ingredients, certifications, awards, ratings, comparative conclusions, or brand assets that are unsupported by the source image or category.
- Do not generate new readable text, slogans, prices, promotions, labels, arrows, charts, QR codes, callouts, or badges.
- Do not make the image a functional explanation diagram, component layout, neutral studio demonstration, or practical task display.
- Do not let status, self-image, role identity, prestige, or abstract symbolic meaning become the dominant message.
- Use people or hands only when they make the felt experience physically plausible and do not distort the product.
- Do not simply upscale, clean up, or restage the original white-background packshot. The output must visibly add the experiential advertising scene requested above.
- Avoid artificial gloss, inconsistent shadows, floating objects, distorted geometry, warped logos, fake reflections, unreadable text artifacts, and any synthetic or uncanny visual feel.
- The image should look like realistic commercial photography or a credible immersive advertising image, not a screenshot, low-quality collage, meme, cluttered e-commerce mockup, or unnatural composite.

```
