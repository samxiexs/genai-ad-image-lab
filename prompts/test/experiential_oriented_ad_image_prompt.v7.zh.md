# Experiential-oriented Advertising Image Prompt v7 中文说明

你正在为消费者广告实验生成受控刺激材料。

使用输入的白底商品图作为 exact source product。保持商品身份不变，包括可见形状、材质、颜色、包装、logo、设计细节和物理结构。

不要虚构输入未支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品上已有的文字、logo 或包装信息可以保留，但不要新增广告文案或改写包装文字。

Image quality and fidelity requirements：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉，清晰、光线充分、比例正确、物理合理、易于查看。
- 使用干净构图、合理光线、阴影、反射和连贯的物体关系。
- 避免截图感、横幅模板感、低质量拼贴、meme 风格、杂乱电商 mockup、变形手部、破损包装、不可读乱码、不真实商品几何、不可能比例和物理上不合理的互动。
- 不要只保留成白底商品照；在保持商品身份的同时增加广告图价值。

生成基于 Park, Jaworski, and MacInnis (1986) 的 Experiential-oriented 广告图。

Brand concept definition：
Park et al. 将 brand concept 定义为基于消费者需求而选择的品牌意义。本 prompt 表达 experiential brand concept。Experiential 指商品与感官愉悦、多样性、认知刺激、刺激感、沉浸或被感受到的消费体验等内部需求相连。

Primary route of persuasion：
图像应让观看者理解商品的体验价值。观看者应能推断遇到、使用、探索、穿戴、品尝、触碰或消费该商品是什么感受。不要让实践问题解决或 symbolic self-image 成为主要说服路径。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Concept-image linkage：
- 从商品标题、品牌、品类、价格、促销和源图中推断一个合理的 experiential need。
- 把该需求转化为 sensory pleasure、variety、cognitive stimulation、stimulation、immersion 或 felt consumption experience 的宽泛视觉线索。
- 只有在品类适配且不虚构商品属性时，才使用感官氛围、运动暗示、深度、节奏、多样性、互动或沉浸场景。
- 使用场景只有在表达 felt experience 时才可以使用；不要把该类型降级为仅展示商品在哪里被使用。
- 商品必须在体验中保持可识别，不能被氛围或道具遮蔽。

Verification standard：
图像应通过 3 秒 experiential concept test：观看者应快速推断被感受到的消费体验，而不是主要把图像理解为功能说明或 symbolic identity signal。
