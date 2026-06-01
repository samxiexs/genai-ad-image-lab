# Symbolic-oriented Advertising Image Prompt v11 中文说明

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
- 任何场景元素、道具、人物或 symbolic cue 都必须同时与白底图和元数据一致。
- 如果标题或品类暗示某种 prestige 或 identity meaning，但白底商品本身并不足以支撑，就要保守处理，不能过度宣称。
- 把白底图商品当作 meaning carrier，而不是灵感来源。

不要虚构未被支持的商品功能、成分、材质、认证、奖项、claims、广告语、评分、价格、二维码、徽章、图表、箭头或品牌资产。

不要在图像中生成新的可读文字。源商品包装上已有文字可以保留，但不要新增广告文案或改写包装。

Image fidelity controls：
- 生成一张连贯、精致的商业广告图。
- 商品必须是主视觉，清晰、光线充分、比例正确、物理合理、易于查看。
- 使用干净构图、合理光线、阴影、反射和连贯的物体关系。
- 避免截图感、横幅模板感、低质量拼贴、杂乱电商 mockup、变形手部、破损包装、不真实商品几何、不可能比例和物理上不合理的互动。
- 不要只留下白底 packshot；广告价值只能来自 grounded concept-image linkage。

Brand concept definition：
依据 Park et al. (1986)，这里表达 symbolic brand concept。Symbolic 指商品与自我提升、角色位置、群体归属、ego-identification 或理想自我形象等内部需求相连。

Primary route of persuasion：
主导阅读必须是 symbolic meaning。观看者应快速推断选择、拥有、展示、赠送或关联该商品表达了怎样的 self-image、role、group membership、taste、belonging、aspiration 或 identity。功能解释和体验刺激必须明显次要。

Grounded reasoning sequence：
1. 从白底图识别商品可见事实，以及哪些设计线索可以被信任。
2. 结合这些可见事实和标题、品牌、品类、价格、促销，推断一个合理 symbolic territory。
3. 构造一个简单明确的视觉关系，让该 symbolic territory 可见，同时不虚构未支持的品牌故事或受众刻板印象。

Concept-image linkage：
- 优先保持一个连贯明确的 symbolic territory，而不是混合多种 mood。
- 只有在支持 symbolic meaning 且不违背白底图与元数据时，才使用 atmosphere、setting、composition、light、depth、scale、negative space 或 restrained metaphor。
- 人物、道具和环境只有在澄清 symbolic meaning 时才可出现；避免无依据的人口统计刻板印象、社会阶层 claims、文化假设或虚构品牌历史。
- 商品必须作为意义载体保持可识别，不能只是装饰气氛里的小物件。

Discriminant-validity guardrails：
- 不要让 mechanism、setup、compatibility、durability、storage、freshness 或 problem solving 成为主要信息。
- 不要让 sensory thrill、novelty、play、immersion 或 tactile atmosphere 成为主要信息，除非它们明显服务于 symbolic meaning。
- 不要把图像做得过于抽象，以致观看者无法推断商品代表什么。

Verification standard：
图像应在 symbolic meaning、self-expression 和 role or identity fit 上得分高。观看者应快速推断商品象征什么或拥有它表达什么，同时仍能认出白底图中的原商品。
