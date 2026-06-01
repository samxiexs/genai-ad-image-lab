# Product-oriented Advertising Image Prompt v7 中文说明

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

生成基于 Park, Jaworski, and MacInnis (1986) 的 Product-oriented 广告图。

Brand concept definition：
Park et al. 将 brand concept 定义为基于消费者需求而选择的品牌意义。本 prompt 表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决或预防消费问题、降低阻力、支持实践任务，或让消费更可靠。

Primary route of persuasion：
图像应让观看者理解商品的实践作用。观看者应能推断商品帮助解决什么消费问题、任务或 affordance。不要让 symbolic self-image、生活方式向往、感官愉悦、新奇感或抽象氛围成为主要说服路径。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Concept-image linkage：
- 从商品标题、品牌、品类、价格、促销和源图中推断一个合理的 functional need。
- 把该需求转化为视觉证据，而不是标签或文字 claims。
- 只有在输入支持时，才使用一般性的 product-task、product-problem、product-affordance、handling、application、protection、organization、fit、operation 或 care 关系。
- 道具、表面、手部或背景元素只有在澄清功能关系时才可出现；不要让它们变成生活方式装饰。
- 如果功能证据不确定，使用简单受控的商品展示构图，而不是虚构具体功能。

Verification standard：
图像应通过 3 秒 functional concept test：观看者应快速理解商品的实践作用，而不是主要把图像理解为 symbolic identity expression 或 experiential stimulation。
