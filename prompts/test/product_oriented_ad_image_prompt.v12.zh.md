# Product-oriented Advertising Image Prompt v12 中文说明

你正在为消费者广告实验生成受控刺激材料。

使用输入的白底商品图作为 exact source product。保持商品身份不变，包括核心形状、材质、颜色、包装、logo、可见设计和物理结构。

不要虚构未被支持的商品功能、成分、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品上已有文字、logo 或包装信息可以保留，但不要新增广告文案或改写包装文字。为后续受控文字叠加保留干净留白。

避免截图感、横幅模板感、低质量拼贴、meme 风格、杂乱电商 mockup、变形手部、破损包装、不可读乱码和不真实商品几何。

生成基于 Park, Jaworski, and MacInnis (1986) 的 Product-oriented 广告图，并让 FUNCTIONAL brand concept 成为主导构念。

Brand concept definition：
Park et al. 将 brand concept 定义为基于消费者需求而选择的品牌意义。本 prompt 表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决或预防消费问题、降低摩擦、支持实际任务，或让消费更可靠。

Primary route of persuasion：
主导路径是具体功能效用、实际问题解决、产品操作性和“产品如何帮助用户”的可见证据。图像必须传达商品在 functional brand concept 下“做什么/帮助什么”，而不是只传达它多高级、多好看、多情绪化、多象征或多适合送礼。

Advertising mechanism：
图像应帮助观看者快速推断商品的 practical job-to-be-done、关键 functional affordances、可见操作部件、handling logic、compatibility、fit、setup、storage、protection、freshness、care、performance、durability 或 ease of use。结合 Park functional 定义以及标题、品牌、品类、价格、促销和源图，推断合理功能线索，并把它们转化为非文字视觉证据。

Function reasoning instruction：
- 先推断产品类型、实际用户问题、可能使用任务、材质或机制，以及消费者购买它的主要功能原因。
- 推断必须受 source image 和 metadata 约束，不能虚构无视觉或品类依据的功能。
- 对电子产品、工具、电器、运动用品、家居用品、美容仪器、玩具、宠物用品、食品、药品、书籍、配饰、时尚品、珠宝和礼品，可推断 operation、interface、assembly、fit、fastening、portability、storage、cleaning、protection、compatibility、freshness、application、organization、comfort、durability 或 care 等功能证据。
- 对装饰性、穿戴型、奢侈型或送礼型商品，如果机械功能有限，可把 practical function 表达为 fit、fastening、scale、wearing support、safe storage、material handling、packaging protection、pairing、care 或 gift-readiness。不要把这些商品做成 status、glamour、romance 或抽象 aspiration 图。
- 不确定时，用一般性的 category affordance，不要编造 fake features。

Visual direction：
- 让商品成为主视觉，并至少展示两个具体 functional evidence cues。
- 优先使用受控的商品演示构图：中性桌面、干净 studio 工作台、整齐部件布局、真实开合状态、可见机制、尺度参照、配件关系、安全收纳、不同材质表面对比，或只用于解释 grip、fit、fastening、application、scale 的手部形式。
- 只有在解释功能时，才可加入相关中性道具。道具必须像证据，而不是生活方式装饰或象征氛围。
- 可接受一个整合在同一商业产品摄影中的次级 close-detail 区域，但其中不能有标签、箭头、callout 或文字。
- 光线、阴影、反射和背景应帮助澄清形状、材质、操作部件、affordance 和 usability。审美抛光只有在提升功能理解时才可接受。
- 避免让纯白或近白 packshot 成为主导方案。图像必须比简单美化商品照提供更多功能信息。
- 视觉内容必须与 Park functional 定义、商品标题、品类、价格层级、促销语境和源图保持语义一致。
- 为后续受控文字叠加保留干净留白。

Strict boundaries：
- 不要让生活方式故事、社交场景、浪漫场景、奢华 mood portrait 或抽象 symbolic composition 成为主导印象。
- 不要让美感、高级感、礼赠情绪、氛围或品牌个性成为主要说服原因。
- 不要把 visual metaphor 作为主要装置。功能意义必须通过具体商品证据可见。
- 不要在图像里添加生成文字、广告语、假标签、假徽章、认证、价格、评分、图表、箭头或比较 claims。
- 不要虚构商品功能、成分、奖项或品牌信息。
- 不要改变商品的形状、颜色、logo、包装或物理结构。
- 如果图像主要像 premium still life、symbolic mood image、experiential atmosphere image，或者只是打光更好的同一张 packshot，那么生成失败。

Verification standard：
观看者应能在 “This image helps me understand what practical problem the product solves” 和 “This image makes the product's functional value clear” 上给高分。图像应通过 3 秒 functional concept test：一个从未听过该商品的人，应快速理解它支持什么 practical task、affordance 或 functional benefit，同时不会主要把图像读成 symbolic brand meaning 或 experiential stimulation。
