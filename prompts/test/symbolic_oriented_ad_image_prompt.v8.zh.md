# Symbolic-oriented Advertising Image Prompt v8 中文说明

你正在为消费者广告研究生成一张受控的 Symbolic-oriented 广告图。

使用输入的白底商品图作为 source product identity reference。保持商品可识别的形状、颜色、材质、logo、包装、可见设计、比例和物理结构。不要重新设计商品。不要虚构未被支持的功能、claims、成分、认证、奖项、价格、评分、徽章、广告语、箭头、图表、二维码或品牌资产。

商品不需要保留白底图里的原始光线。为了让图像更真实，可以让商品的光线、阴影、反射、透视、曝光和环境色适应新场景。商品必须看起来像真实地融入人物的风格、空间或日常 routine 中，而不是被贴进图像里。

不要添加新的可读文字。源商品上已有的 logo、包装文字或产品标记可以保留，但不要新增广告文案、标签、UI 文字、功能标注或改写包装文字。为后续受控文字叠加保留干净留白。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

生成一张 Symbolic-oriented 图像，让 IDENTITY EXPRESSION 成为主导信息。

先根据商品图、标题、品类和元数据推断一个合理的 symbolic meaning。这个意义可以是现代身份、创意品味、职业自信、精致日常风格、独立性、艺术身份、知识分子身份、社交自信、领导力、冒险身份、关怀身份、有条理的生活方式、玩心人格，或属于某个理想群体，具体取决于产品品类。

图像应回答：
“什么样的人会选择、拥有、携带、穿戴、展示、赠送、使用或珍视这个商品？”

要生成的是一张真实的 editorial advertising photograph，在其中商品作为可见的 identity signal 发挥作用。商品必须被有意地整合进人物的风格、角色、空间、日常 routine、价值观、品味或社会语境中。它不能只是一个被动道具。

图像应清晰展示以下三者之间的 symbolic relationship：
1. 这个人、拥有者、赠送者或使用者；
2. 源商品；
3. 围绕他们的 identity cues，例如 personal styling、workspace、tools、accessories、posture、social context、curated personal objects、creative environment、professional setting、minimalist home、organized routine、caring routine、urban daily life、hobby setting 或 community context。

使用两到三个与该商品品类相关的 identity cues，并且这些 cues 应共同支持同一个 symbolic meaning。商品必须明显参与 identity expression，并且看起来像被刻意选择的。

对于本身不容易产生明显 symbolic value 的商品，可以从符合品类的 ownership signals 去推断 symbolic meaning，例如 practical、organized、caring、thoughtful、tasteful、prepared、playful、creative、refined、independent 或 attentive to daily life。不要在品类不支持的情况下强行制造 luxury、glamour、status 或 romance。

真实感是关键。使用可信的自然光、物理一致的阴影、真实的手部接触、自然姿态、真实布料纹理、真实物体尺度、真实环境细节、轻微真实相机瑕疵和自然色彩分级。避免过度精致的时尚幻想、塑料皮肤、完美 showroom 光线、假的 luxury glow 和过度人工的 cinematic effects。

使用一个连贯的摄影场景。不要拼贴，不要 split-screen，不要 floating product，不要 pasted product，不要 artificial magnifier effect。商品必须清晰可见，并约占图像的 15–35%。

避免 generic luxury shortcuts。不要只依赖好看的模特、正装、西装、屋顶、城市天际线、跑车、香槟、豪宅、glamorous lighting 或 fashion pose。只有在与商品品类相关且商品本身仍然承担 symbolic meaning 时，这些元素才可出现。

对于 smartphones、cameras 或 personal devices：
这类设备可以传达 creative taste、modern identity、personal independence、social confidence、refined everyday style 或 connected life。它应作为人物所选择的 look、routine 或 role 的一部分而出现。不要把场景做成 camera-function demo、travel snapshot、video call、entertainment moment 或 productivity proof。

Photographic style：
真实 editorial advertising photography、自然人体姿势、真实皮肤与手部细节、可信尺度、真实 styling、自然窗光或真实 urban available light、真实相机质感。不是 CGI、不是 3D render、不是 illustration、不是 AI-art-like 风格。

图像应通过 3-second symbolic test：观看者无需阅读文字，就应快速理解与该商品相关的 identity、role、taste、group belonging、confidence、value 或 desired self。

以下情况视为生成失败：
- 商品只是被拿在手上，但没有身份意义；
- 图像只依赖一个好看的模特或奢华背景；
- 图像变成功能演示；
- 图像变成体验场景；
- 商品看起来像被贴进场景里；
- 即使把商品移除，symbolic meaning 依然同样强。

Negative prompt：
generic attractive model, fake luxury, rooftop cliché, sports car, champagne, mansion, perfect showroom, plastic skin, fantasy glow, overly cinematic lighting, product merely held, passive prop, product pasted into scene, cutout look, floating product, impossible shadows, fake reflections, lifestyle pose with no identity meaning, technical demo, productivity proof, travel experience, entertainment scene, emotional scene, romantic scene, unrealistic hand grip, deformed hands, extra fingers, missing fingers, readable text, slogan, labels, badges, arrows, charts, price tag, QR code, distorted logo, wrong product color, changed product shape, plain packshot, CGI, 3D render, illustration, cartoon, surreal, overly glossy AI look.
