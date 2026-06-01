# Experiential-oriented Advertising Image Prompt v11 中文说明

你正在为消费者广告实验生成受控刺激材料。

把输入的白底商品图视为 grounded source product，并把它作为生成时最主要的事实锚点。开始决定场景前，先读取白底图，只提取可见商品事实：产品形态、组成部件、材质线索、颜色、包装形式、logo 或印刷元素、开合结构、可见配件，以及任何可以明确观察到的物理 affordance。

商品元数据只作为辅助解释信息，不能成为虚构不可见特征的理由。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Source-grounding requirements：
- 保持 source product identity 恒定，保留白底图中的可见形状、材质、颜色、包装、logo、设计细节、比例和物理结构。
- 任何氛围、互动或 usage cue 都必须同时与白底图和元数据一致。
- 如果标题或品类暗示某种感官属性，但白底商品本身并不足以支撑，就要保守处理，不能虚构。
- 把白底图商品当作 experiential anchor，而不是灵感来源。

不要虚构未被支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品包装上已有文字可以保留，但不要新增广告文案或改写包装。

Image fidelity controls：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉，清晰、光线充分、比例正确、物理合理、易于查看。
- 使用干净构图、合理光线、阴影、反射和连贯的物体关系。
- 避免截图感、横幅模板感、低质量拼贴、杂乱电商 mockup、变形手部、破损包装、不真实商品几何、不可能比例和物理上不合理的互动。
- 不要只留下白底 packshot；广告价值只能来自 grounded concept-image linkage。

Brand concept definition：
依据 Park et al. (1986)，这里表达 experiential brand concept。Experiential 指商品与感官愉悦、多样性、认知刺激、沉浸或被感受到的消费体验等内部需求相连。

Primary route of persuasion：
主导阅读必须是 felt experience。观看者应快速推断遇到、触碰、品尝、穿戴、探索、享受或消费该商品是什么感受。功能解释和象征身份意义必须明显次要。

Grounded reasoning sequence：
1. 从白底图识别商品可见事实，以及哪些感官或互动线索可以被合理推断。
2. 结合这些可见事实和标题、品牌、品类、价格、促销，推断一个合理 experiential need。
3. 构造一个简单明确的视觉关系，让该体验可见，同时不虚构未支持的感官 claims。

Concept-image linkage：
- 优先保持一条清楚的 felt-experience route，而不是泛化生活方式场景。
- 使用场景只有在帮助观看者推断“这种体验是什么感觉”时才可出现；不要把该类型降级为仅说明商品在哪里或何时被使用。
- 只有在白底图和元数据支持且不虚构商品属性时，才使用 atmosphere、motion implication、depth、interaction、texture、variety 或 immersive context。
- 商品必须在体验中保持可识别，不能被电影化氛围或装饰性道具遮蔽。

Discriminant-validity guardrails：
- 不要让 practical problem solving、feature explanation、setup、compatibility 或 task support 成为主要信息。
- 不要让 status、belonging、identity display、prestige 或 role signaling 成为主要信息。
- 不要虚构 flavors、scents、textures、ingredients 或 performance claims。

Verification standard：
图像应在 felt consumption experience、sensory pleasure、variety 或 cognitive stimulation 上得分高。观看者应快速推断商品能提供怎样的体验，同时仍能认出白底图中的原商品。
