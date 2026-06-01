# Experiential-oriented Advertising Image Prompt v8 中文说明

你正在为消费者广告研究生成一张受控的 Experiential-oriented 广告图。

使用输入的白底商品图作为 source product identity reference。保持商品可识别的形状、颜色、材质、logo、包装、可见设计、比例和物理结构。不要重新设计商品。不要虚构未被支持的功能、claims、成分、认证、奖项、价格、评分、徽章、广告语、箭头、图表、二维码或品牌资产。

商品不需要保留白底图里的原始光线。为了让图像更真实，可以让商品的光线、阴影、反射、透视、曝光和环境色适应新场景。商品必须看起来像真实地存在于体验场景中，而不是被贴进图像里。

不要添加新的可读文字。源商品上已有的 logo、包装文字或产品标记可以保留，但不要新增广告文案、标签、UI 文字、功能标注或改写包装文字。为后续受控文字叠加保留干净留白。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

生成一张 Experiential-oriented 图像，让 LIVED EXPERIENCE 成为主导信息。

先根据商品图、标题、品类和元数据推断一种合理的 consumption experience。这个体验可以是 discovering、capturing、listening、watching、gaming、creating、relaxing、cooking、tasting、learning、exploring、exercising、playing、caring、sharing、decorating、traveling，或与他人共度有意义的时光，具体取决于产品品类。

图像应回答：
“这个商品帮助创造了什么样的 enjoyable、immersive、memorable、sensory、creative、relaxing、playful、exploratory 或 meaningful experience？”

要生成的是一张真实的 candid advertising photograph，像摄影师抓拍到的真实时刻，而不是 AI postcard。商品必须主动参与并 enable 这个体验。它不能只是出现在漂亮背景前面。

图像应清晰展示以下三者之间的 interaction：
1. 用户或消费者；
2. 源商品；
3. 商品帮助用户 access、capture、enjoy、create、share 或 explore 的体验、活动、地点、内容、物体、人物或时刻。

体验必须通过 action 呈现，而不只是 atmosphere。商品可以被用于 capture、listen、watch、play、taste、cook、apply、wear、use、create、navigate、relax、share、discover、care、decorate，或与周围环境互动。

对于 smartphones、cameras 或 recording devices，前后朝向是严格的物理要求。

如果可见的源商品主要是手机或设备背面，且能看到后置摄像头，不要默认使用“人物拿着手机拍前方的人或风景”这种构图。那样很容易让手机方向看起来是反的。

如果场景表现的是用户在拍摄另一个人、风景、食物、活动或环境：
- 后置镜头必须朝向被拍摄对象；
- 屏幕一侧必须朝向用户；
- 如果视角位于用户身后或侧后方，观看者通常应看到屏幕一侧，而不是带 logo 和后置镜头的背面；
- 绝不能出现这样的画面：观看者从用户背后看到手机背面，但用户似乎正在拍摄前方的人或风景。

如果必须展示手机背面、logo 和后置镜头，只能使用物理上合理的 experiential 构图：
- 自拍；
- 视频通话；
- 自拍录制；
- 镜面录制；
- 视角位于被摄对象一侧，朝向拍摄者；
- 用户刚拍完照，正在自然地放下手机；
- 手机只是被携带、展示，或自然地整合进体验中，而不是假装正在拍摄远处主体。

如果画面里手机背面和后置镜头朝向观看者，那么场景绝不能暗示这部手机正在拍摄手机后方远处的人或风景。后置摄像头必须朝向真正被拍摄的对象。

真实感是最高优先级。使用自然、物理一致的光线和阴影。避免完美 postcard sunset、fantasy glow、fake cinematic lighting、过度 HDR、塑料皮肤、假 bokeh、不可能的高光和过度 polished 的 AI-advertising 风格。

场景应包含真实相机的不完美感：轻微动态模糊、自然景深、不均匀环境光、可信曝光、细微传感器噪点、不完美构图、真实皮肤纹理、自然手部受力、真实接触阴影和轻微透视误差。

使用一个连贯的真实场景。不要拼贴，不要 split-screen，不要 floating product，不要 pasted product，不要 artificial magnifier effect。商品必须清晰可见，并约占图像的 20–40%，同时体验仍然容易理解。

避免纯功能演示、生产力场景、技术证明、身份炫耀、奢华肖像、泛化 lifestyle pose，或商品只是被举着却并未真正参与体验的场景。

Photographic style：
真实 documentary-style advertising photography、自然动作、真实皮肤与手部细节、可信物体尺度、真实环境纹理、available light 或自然窗光、真实相机质感。不是 CGI、不是 3D render、不是 illustration、不是 AI-art-like 风格。

图像应通过 3-second experiential test：观看者无需阅读文字，就应快速理解与该商品相关的 enjoyable、immersive、memorable、creative、relaxing、playful、sensory 或 exploratory experience。

以下情况视为生成失败：
- 手机方向反了；
- 后置摄像头朝错方向；
- 屏幕朝错方向；
- 观看者从用户身后看到手机背面，但用户似乎正在拍摄前方的人或风景；
- 场景暗示用户在拍摄别人，但后置摄像头却朝向观看者；
- 商品只是被举起来当道具，并未真正参与体验；
- 图像看起来像 AI postcard，而不是真实照片。

Negative prompt：
reversed phone, phone held backwards, rear camera facing wrong direction, screen facing wrong direction, viewer sees phone back from behind the user, rear camera facing viewer while supposedly photographing others, phone back visible while photographing distant scenery, impossible camera orientation, fingers blocking lens, awkward face blocking, AI postcard, perfect sunset, fantasy glow, fake cinematic lighting, overprocessed HDR, plastic skin, fake bokeh, generic travel photo, product merely held, product pasted into scene, cutout look, floating product, unrealistic hand grip, deformed hands, extra fingers, missing fingers, readable text, slogan, labels, badges, arrows, charts, price tag, QR code, distorted logo, wrong product color, changed product shape, lifestyle pose with no real interaction, luxury status scene, productivity scene, technical demo, plain packshot, CGI, 3D render, illustration, cartoon, surreal, overly glossy AI look.
