# Product-oriented Advertising Image Prompt v9 中文说明

你正在为消费者广告实验生成受控刺激材料。

使用输入的白底商品图作为 exact source product。保持商品身份不变，包括可见形状、材质、颜色、包装、logo、设计细节和物理结构。

不要虚构输入未支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品上已有的文字、logo 或包装信息可以保留，但不要新增广告文案或改写包装文字。

Image-quality controls：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉，清晰、光线充分、比例合理、易于查看。
- 避免截图感、横幅模板感、低质量拼贴、破损包装、不可读乱码、不真实商品几何和物理上不合理的互动。
- 不要只留下白底 packshot；在保持商品身份的同时增加广告图价值。

Brand concept definition：
依据 Park, Jaworski, and MacInnis (1986)，这里表达 functional brand concept。Functional 指商品与外部产生的消费需求相连：解决当前问题、预防潜在问题、降低摩擦、支持实际任务或让消费更可靠。

Primary route of persuasion：
图像应让观看者理解商品的实际作用。观看者应能推断商品帮助完成什么问题、任务或 affordance。不要让象征身份、精致感或感官氛围成为主要说服路径。

Concept-image linkage：
- 从源图和元数据推断一个合理 functional need。
- 用具体视觉证据而不是文字 claims 去表达。
- 只有在输入支持时，才使用 handling、setup、protection、fit、organization、operation、application、storage、freshness 等关系。
- 道具、表面、手部或背景元素只用于澄清功能，不应变成生活方式装饰或象征氛围。
- 如果功能不确定，使用简单受控的商品展示构图，而不是虚构具体特征。

Verification standard：
图像应通过 3 秒 functional concept test：观看者应快速理解商品的实践作用，而不是主要把图像理解为 symbolic identity expression 或 experiential stimulation。
