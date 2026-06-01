# Product-oriented Advertising Image Prompt v10 中文说明

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
依据 Park et al. (1986)，这里表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决或预防消费问题、降低摩擦、支持实际任务或让消费更可靠。

Primary route of persuasion：
主导阅读必须是 functional problem solving、task support 或 practical affordance。观看者应快速推断商品帮助完成什么任务。象征身份意义和体验刺激必须保持非主导。

Concept-image linkage：
- 从源图和元数据推断一个合理 functional need。
- 用可见证据而不是文字解释来表达。
- 优先选择一个干净明确的 product-task relation，而不是堆很多小细节。
- 只有在输入支持时，才使用 handling、setup、protection、fit、storage、compatibility、organization、application、operation、freshness 或 care 线索。
- 道具、手部、表面和背景元素只能用于澄清功能关系，必须像证据而不是装饰。
- 如果确切功能不确定，使用简单受控的商品展示关系，而不是虚构具体特征。

Discriminant-validity guardrails：
- 不要让 prestige、taste、status、belonging、romance、celebration 或抽象 aspiration 成为主要信息。
- 不要让 sensory pleasure、fantasy、immersion 或 experiential atmosphere 成为主要信息。
- 如果 visual metaphor 会让 3 秒内无法看出实践作用，就不要把它作为主要手段。

Verification standard：
图像应在 practical problem solving 和 functional value clarity 上得分高。一个从未见过该商品的观看者应快速推断它支持什么实践任务或消费问题，同时不会主要把它理解为 symbolic self-expression 或 experiential stimulation。
