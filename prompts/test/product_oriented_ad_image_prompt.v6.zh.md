# Product-oriented Advertising Image Prompt v6 中文说明

你正在为消费者研究生成一张受控广告图刺激材料。

使用输入的白底商品图作为 grounded source product。保持商品身份不变，包括可见形状、颜色、材质、包装、logo 和物理结构。

商品元数据：
- Title: {ori_title}
- Brand: {creative_id_brand}
- Category: {level_one_category_name}
- Price: {creative_id_price}
- Promotion: {creative_id_promotion}

Brand concept definition：
Park, Jaworski, and MacInnis (1986) 将 brand concept 定义为基于消费者需求而选择的品牌意义。生成 Product-oriented 图像，表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决或预防消费问题、降低阻力、支持实践任务，或让消费更可靠。

General image-quality controls：
生成一张连贯、精致的广告图。商品应是主视觉主体，清晰、光线充分、几何一致、易于查看。使用干净构图、合理光影、不杂乱的背景，以及视觉上连贯的物体关系。避免低质量拼贴、截图或模板感布局、变形手部、破损包装、不可读合成文字和不真实的商品几何。

Evidence discipline：
只使用 source image 和商品元数据中的事实。不要虚构商品属性、机制、成分、健康或性能声明、奖项、认证、价格、广告语、评分、徽章、二维码、图表、箭头或新的可读广告文字。优先使用宽泛、品类适配、可泛化的概念线索，不使用细碎虚构的小场景。

Concept-image linkage：
让观看者推断商品的实践作用。呈现商品与消费问题、任务或 affordance 之间一般且视觉上合理的关系。背景、道具、手部、场景、光线或风格必须支持 functional concept，并且不能违背商品事实。用视觉证据，而不是文字 claims；若功能证据不确定，选择简单、受控的商品展示关系，不要虚构具体功能。
symbolic self-image 和 experiential stimulation 应保持次要。主导理解应是 functional problem solving 或 task support。
