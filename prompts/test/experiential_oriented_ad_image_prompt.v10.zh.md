# Experiential-oriented Advertising Image Prompt v10 中文说明

你正在为消费者广告实验生成受控刺激材料。

使用输入的白底商品图作为 grounded source product。保持商品身份不变，包括可见形状、材质、颜色、包装、logo、设计细节和物理结构。

只使用 input-grounded 的商品和品牌事实。不要虚构输入未支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品包装上已有文字可以保留，但不要新增广告文案或改写包装。

Image fidelity and prompt-alignment controls：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉锚点：清晰、光线充分、比例正确、物理合理、易于查看。
- 使用干净构图、合理光线、阴影、反射和连贯的物体关系。
- 避免截图感、横幅模板感、低质量拼贴、杂乱电商 mockup、变形手部、破损包装、不可读乱码、不真实几何、不可能比例和物理上不合理的互动。
- 不要只留下白底 packshot；广告价值只能来自与 concept 相关的视觉链接。

Brand concept definition：
依据 Park et al. (1986) 以及后续将体验与单纯使用场景区分开的图像研究，这里表达 experiential brand concept。Experiential 指商品与感官愉悦、多样性、认知刺激、沉浸或被感受到的消费体验等内部需求相连。

Primary route of persuasion：
主导阅读必须是 felt experience。观看者应快速推断遇到、触碰、品尝、穿戴、探索、享受或消费该商品是什么感受。功能解释和象征身份意义必须保持非主导。

Concept-image linkage：
- 从源图和元数据推断一个合理 experiential need。
- 把该需求转化为 sensory pleasure、comfort、freshness、discovery、rhythm、immersion、curiosity、play、relaxation、stimulation 或 variety 的可见线索。
- 优先保持一条清楚的 felt-experience route，而不是泛化生活方式场景。
- 使用场景只有在帮助观看者推断“这种体验是什么感觉”时才可出现；不要把该类型降级为仅说明商品在哪里或何时被使用。
- 只有在输入支持且不虚构商品属性时，才使用 atmosphere、motion implication、depth、interaction、texture、variety 或 immersive context。
- 商品必须在体验中保持可识别，不能被电影化氛围或装饰性道具遮蔽。

Discriminant-validity guardrails：
- 不要让 practical problem solving、feature explanation、setup、compatibility 或 task support 成为主要信息。
- 不要让 status、belonging、identity display、prestige 或 role signaling 成为主要信息。
- 不要虚构 flavors、scents、textures、ingredients 或 performance claims。

Verification standard：
图像应在 felt consumption experience、sensory pleasure、variety 或 cognitive stimulation 上得分高。观看者应快速推断商品能提供怎样的体验，而不是主要把图像理解为功能说明或 symbolic identity signal。
