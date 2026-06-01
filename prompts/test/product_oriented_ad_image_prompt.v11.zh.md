# Product-oriented Advertising Image Prompt v11 中文说明

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
- 任何场景元素、互动或 affordance 都必须同时与白底图和元数据一致。
- 如果标题或品类暗示某个特征，但白底图里看不到，就要保守处理，不能夸大或虚构。
- 把白底图商品当作主角，而不是灵感来源。

不要虚构未被支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品包装上已有文字可以保留，但不要新增广告文案或改写包装。

Image fidelity controls：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉，清晰、光线充分、比例正确、物理合理、易于查看。
- 使用干净构图、合理光线、阴影、反射和连贯的物体关系。
- 避免截图感、横幅模板感、低质量拼贴、杂乱电商 mockup、变形手部、破损包装、不真实商品几何、不可能比例和物理上不合理的互动。
- 不要只留下白底 packshot；广告价值只能来自 grounded concept-image linkage。

Brand concept definition：
依据 Park et al. (1986)，这里表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决或预防消费问题、降低摩擦、支持实际任务或让消费更可靠。

Primary route of persuasion：
主导阅读必须是 functional problem solving、task support 或 practical affordance。观看者应快速推断商品帮助完成什么实践任务。象征身份意义和体验刺激必须明显次要。

Grounded reasoning sequence：
1. 从白底图识别商品可见事实，以及哪些部件或 affordance 可以被信任。
2. 结合这些可见事实和标题、品牌、品类、价格、促销，推断一个合理 practical need。
3. 构造一个简单明确的视觉关系，让这个 practical need 可见，同时不虚构未支持特征。

Concept-image linkage：
- 优先选择一个干净明确的 grounded product-task relation，而不是很多装饰性细节。
- 只有在白底图和元数据支持时，才使用 handling、setup、protection、fit、storage、compatibility、organization、application、operation、freshness 或 care 线索。
- 道具、手部、表面和背景元素只能用于澄清功能关系，必须像证据而不是氛围。
- 如果确切功能从白底图里看不清，就用保守的受控商品展示构图，而不是虚构具体机制。

Discriminant-validity guardrails：
- 不要让 prestige、taste、status、belonging、romance、celebration 或抽象 aspiration 成为主要信息。
- 不要让 sensory pleasure、fantasy、immersion 或 experiential atmosphere 成为主要信息。
- 如果 visual metaphor 会让 3 秒内看不出实践作用，就不要把它作为主要手段。

Verification standard：
图像应在 practical problem solving 和 functional value clarity 上得分高。一个从未见过该商品的观看者应快速推断它支持什么实践任务，同时仍能认出白底图中的原商品。
