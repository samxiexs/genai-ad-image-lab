# Product-oriented Advertising Image Prompt v8 中文说明

你正在为消费者广告研究生成一张受控的 Product-oriented 广告图。

使用输入的白底商品图作为 source product identity reference。

商品不需要保留白底图里的原始光线。为了让图像更真实，可以让商品的光线、阴影、反射、透视、曝光和环境色适应新场景。商品必须看起来像真实拍摄进场景中的物体，而不是从白底图里剪下来贴上去。

不要添加新的可读文字。源商品上已有的 logo、包装文字或产品标记可以保留，但不要新增广告文案、标签、UI 文字、功能标注或改写包装文字。为后续受控文字叠加保留干净留白。

商品元数据：

- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

生成一张 Product-oriented 图像，让 FUNCTION 和 PRODUCT UNDERSTANDING 成为主导信息。

先推断产品类型、实际使用任务、用户问题、材质、结构，以及消费者购买它的主要功能原因。只展示由商品图、标题、品类和元数据支持的合理功能和 affordance。不确定时，使用一般性的、符合品类的 affordance，而不是编造特征。

要生成的是一个真实的 multi-view 商业产品展示图，而不是 lifestyle scene。

构图应主要从多个功能维度展示商品：

1. 一个主导 hero view；
2. 两到三个次级视角，例如 front view、back view、side view、top view、close-up detail、open/closed state、material texture、lens、button、cap、connector、compartment、strap、handle、package structure、scale reference、accessory relationship、storage state 或 handling detail；
3. 一个干净的 studio tabletop、neutral work surface、organized product demonstration board，或受控的商业产品展示布局。

整张图应像专业的产品演示摄影，包含多个协调一致的商品视角，而不是以人物为中心的使用故事。

总计至少展示三个具体的 product evidence cues。这些线索应帮助观看者理解商品的结构、可用性、材质、操作方式、收纳、保护、便携性、贴合度、舒适性、兼容性、护理方式或实际 affordance。

允许出现商品的多个实例或多个视角，但只能用于展示不同维度、角度、细节或功能 affordance。每一个实例都必须与源商品身份完全一致。

人物、手部或身体局部只能作为 scale、grip、fit、fastening、application 或 handling reference 出现。不要创造 lifestyle scene、travel scene、emotional scene、social scene、symbolic identity scene 或 experiential moment。

道具只有在帮助解释商品功能、尺度、收纳、兼容性、使用方式或材质时才可出现。道具必须像 functional evidence，而不是 lifestyle decoration。

商品应主导整张图，约占总视觉面积的 45–70%。使用物理准确的光线、接触阴影、反射、商品重量感、镜头透视、表面纹理、轻微真实相机瑕疵和可信的物体尺度。

避免 plain white packshot、beauty still life、lifestyle story、symbolic identity scene、luxury mood、emotional experience、entertainment scene、romance、travel 或 abstract metaphor。图像必须帮助观看者理解商品是什么、有哪些部分、以及它提供什么实际价值。

Photographic style：
真实的专业商业产品摄影、高分辨率、真实材质纹理、准确尺度、自然阴影、干净构图、柔和 studio 光或自然窗光。不是 CGI、不是 3D render、不是 illustration、不是 AI-art-like 风格。

图像应通过 3-second product-function test：观看者无需阅读任何文字，就应快速理解商品的实际任务、结构、affordance 或功能收益。

Negative prompt：
lifestyle usage scene, person-centered story, travel scene, emotional moment, social scene, symbolic identity scene, experiential scene, product used as prop, single ordinary use scene, low-quality collage, screenshot layout, banner template, infographic, arrows, charts, labels, badges, readable text, slogan, fake claim, price tag, sale tag, QR code, distorted logo, wrong product color, changed product shape, broken packaging, unrealistic geometry, floating product, pasted product, cutout look, impossible shadows, fake reflections, deformed hands, extra fingers, missing fingers, plain white packshot, premium still life with no function, luxury mood, CGI, 3D render, illustration, cartoon, surreal, overly glossy AI look.
