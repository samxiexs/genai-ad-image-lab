# Symbolic-oriented Advertising Image Prompt v10 中文说明

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
依据 Park et al. (1986)，这里表达 symbolic brand concept。Symbolic 指商品与自我提升、角色位置、群体归属、ego-identification 或理想自我形象等内部需求相连。

Primary route of persuasion：
主导阅读必须是 symbolic meaning。观看者应快速推断选择、拥有、展示、赠送或关联该商品表达了怎样的 self-image、role、group membership、taste、belonging、aspiration 或 identity。功能解释和体验刺激必须保持非主导。

Concept-image linkage：
- 从源图和元数据推断一个合理 symbolic territory。
- 把该意义转化为 identity、role、belonging、aspiration、care、expertise、individuality、confidence、taste 或 prestige 的宽泛视觉线索。
- 优先保持一个连贯明确的 symbolic territory，而不是混合多种 mood。
- 只有在支持 symbolic meaning 且不违背商品事实时，才使用 atmosphere、setting、composition、light、depth、scale、negative space 和克制的 metaphor。
- 人物、道具和环境只有在澄清 symbolic meaning 时才可出现；避免无依据的人口统计刻板印象、社会阶层 claims、文化假设或虚构品牌故事。
- 商品必须作为意义载体保持可识别，不能只是 mood 装饰里的小物件。

Discriminant-validity guardrails：
- 不要让 mechanism、setup、compatibility、durability、storage、freshness 或 problem solving 成为主要信息。
- 不要让 sensory thrill、novelty、play、immersion 或 tactile atmosphere 成为主要信息，除非它们明显服务于 symbolic meaning。
- 不要把图像做得过于抽象，以致观看者无法推断商品代表什么。

Verification standard：
图像应在 symbolic meaning、self-expression 和 role or identity fit 上得分高。观看者应快速推断商品象征什么或拥有它表达什么，而不是主要学习商品做什么或聚焦感官体验。
