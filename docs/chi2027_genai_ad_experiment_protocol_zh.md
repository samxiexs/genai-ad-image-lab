# CHI 2027 研究方案：理论驱动的生成式 AI 广告图

> 本文件是英文协议 [`chi2027_genai_ad_experiment_protocol.md`](chi2027_genai_ad_experiment_protocol.md) 的中文工作版本。两份文件的设计、样本量、题项编号、模型和参考文献编号必须同步更新。英文版用于投稿、预注册和国际审稿；本版用于中文团队协作、IRB/伦理材料准备和问卷落地。

## 研究目的与不可改变的设计原则

**研究问题。** 对同一张白底商品参考图，GenAI 分别生成 Product-oriented、Experiential-oriented 与 Symbolic-oriented 广告图时，哪种视觉策略更适合具有不同实用/享乐属性及不同象征性承载能力的商品？这种效果经由哪些消费者心理反应发生？当观看者知道图像由生成式 AI 制作时，结果是否改变？

**研究边界。** 本协议旨在建立可预注册、可通过 IRB 审查、可复现的实验，不预设假设一定成立。核心理论依据是 Park 等人的功能/象征/体验品牌概念框架 [R1]、Homburg 等人的产品设计维度 [R2]，以及视觉心理模拟研究 [R6, R7]。

1. 商品分类为 `2（实用型/享乐型）× 2（低/高象征性承载能力）`；每一格必须是**多个商品的集合**，绝不能等同于单一商品。
2. 当前 CSV 中的 `symbolic` 仅是待验证的商品类别假设，不是实验处理；它不得决定 logo 是否保留。
3. 所有最终刺激统一去品牌、去价格、去促销信息、去可读图中文字。这样可以隔离商品属性与视觉策略，避免品牌资产、价格和已有身份联想成为混淆因素。
4. 三种策略是图像的**主导阅读路径**，而不是声称某商品只有一种价值。商品可以兼具功能、体验和象征意义；本研究只操纵哪一种意义最突出。
5. 样本为中国成年在线消费者。论文与预注册使用英文；参与者看到中文材料。所有中文题项均为基于原理论/量表的情境适配版，必须在正式检验前完成翻译与测量验证。

## 1. 商品、刺激与可审计生成流程

### 1.1 初始商品池与四类商品

`data/experiment/Experiment-Test0709.csv` 目前含 15 个候选商品：实用-高象征 `n=4`、实用-低象征 `n=3`、享乐-高象征 `n=5`、享乐-低象征 `n=3`。正式实验每格至少保留 3 个通过预检验的 exemplar，即至少 12 个商品；若现有商品不达标，应从更大的商品目录补选，而不是为了平衡强行保留。

| 代码 | 含义 | 预检验必须满足的模式 |
| --- | --- | --- |
| U-LS | 主要服务于实际任务/问题解决，身份表达能力弱 | 实用性 > 享乐性；象征性低 |
| U-HS | 主要服务于实际任务/问题解决，同时与身份、角色或群体有关 | 实用性 > 享乐性；象征性高 |
| H-LS | 主要提供愉悦、刺激或享受，身份表达能力弱 | 享乐性 > 实用性；象征性低 |
| H-HS | 主要提供愉悦/刺激，同时与身份、角色或群体有关 | 享乐性 > 实用性；象征性高 |

U-HS 与 H-HS 是合理类别，不是理论矛盾：功能定位与象征定位可以彼此独立 [R4]。

### 1.2 Stimulus manifest

正式收集结果变量前，建立版本化、只读的 `stimulus_manifest.csv`。每一张候选图必须有一行，并保存：`product_id`、预检验类别、源图哈希、去品牌状态、取向、完整 prompt、prompt 版本、模型/提供方/版本、生成日期、API 参数、输出哈希、候选序号、自动 QC、人工 QC 与最终纳入状态。所有被拒绝图像及拒绝原因也必须保留。

每个 `商品 × 策略` 在固定图像模型与 wrapper 下至少生成 3 张候选图。先对源产品身份、禁用文字、虚构宣称和明显 artifact 做盲法技术 QC；按照已归档的生成顺序，选择**第一张**通过 QC 的图。不得根据广告态度、购买意愿、操纵检验结果或任何参与者结果挑图。若有 12 个商品，正式刺激固定为 `12 × 3 × 1 = 36` 张图。

三种策略必须共享：1:1 图幅、相同白底产品参考图、无可读文字、无虚构功能宣称、无价格、无品牌线索、相近的产品显著度。唯一有意改变的内容是理论上的视觉策略。

| 策略 | 主导阅读路径 | 图像执行边界 | 文献依据 |
| --- | --- | --- | --- |
| Product-oriented | 产品解决什么消费问题、如何被理解或使用 | 产品中心、可观察的产品—任务关系；不得编造性能或利益 | 功能概念 [R1]；功能性/可用性 [R2] |
| Experiential-oriented | 与产品互动/消费可能是什么感觉 | 以产品为基础的消费片段，近用户/参与者视角；身份地位不得成为主导含义 | 体验概念 [R1]；意象与具身模拟 [R6, R7] |
| Symbolic-oriented | 产品关于个人、角色或群体表达什么 | 通过设计、陈列、场景形成产品—身份关系；不得使用泛化的奢华/地位刻板印象 | 象征概念 [R1, R4] |

### 1.3 独立刺激验证与纳入规则

主实验前进行中国在线**刺激筛选 pilot**，暂定 `N = 180` 名有效成年人。全体参与者评价全部 36 张最终图（`12 商品 × 3 策略`）。12 个商品区块随机排序；每个区块先展示去品牌源图，再随机展示同一商品的三张策略图。参与者不知道策略标签。

为使“全样本 × 36 图”的任务可行，每张图只用短筛选表，而不再逐图填写完整 V1--V5：S1 为主导含义强制三选一（功能性产品/问题信息、真实使用/消费体验、身份/角色/群体意义）；S2 为“这张图仍然呈现与参考图相同的产品”（1--7 分）；S3 为“这张图看起来是一则连贯、可信的广告”（1--7 分）。参与者可选填指出新增可读文字、虚构功能或实质产品不一致。每人共有 108 个必答反应，这是本筛选 pilot 有意设定的最高负荷。

此 pilot 仅检验可行性与操纵保真度，不证明任何广告策略提升消费者结果。一张最终图只有同时满足下列标准才保留：

- 至少 50% 的参与者选择其目标路线，且该比例的 95% CI 排除 33.3% 的随机猜测水平；
- 产品保真度与视觉质量均值均至少 `4.5/7`；
- 技术 QC 与参与者标注复核后，未确认存在新增文字、虚构功能或实质产品不一致；
- 对同一商品，三种策略图的平均视觉质量最大差异不超过 `0.60` 分。

若一张图失败，只修改该 `商品 × 策略` 的 prompt，保留被拒绝图及原因，并用相同短筛选表对替换图再招募独立定向样本 `N = 60`。多模态模型只做文字/身份漂移等辅助 QC；人类评分仍是纳入依据，LLM 不能替代消费者构念效度 [R20, R21]。

## 2. 变量、题项与计分规则

除特别注明外，均使用 1--7 分同意量表：`1 = 非常不同意`，`7 = 非常同意`。题项在构念内随机呈现；仅按各行明确规定的方向计分；在至少回答三分之二题项时取均值；对完整多题量表报告 McDonald's omega 与预注册 CFA。不得在看到条件差异后删题。

以下英文题项用于英文问卷/附录，中文题项用于中国样本。它们是广告或商品情境的适配表述，**不是**对受版权保护原量表的逐字复制。对实际完整施测的多题构念：商品分类构念在商品预检验中验证；图像验证构念在刺激验证中验证；主要结果构念在 Study 1 中验证，并在样本允许时做留出样本确认。Study 1 预注册的两题短结果量表报告两题相关及逐题稳健性结果；单题 M1--M3 过程指标不作 CFA 或量表信度主张。

### 表 1：商品预检验与刺激验证题项

| 编号/角色 | 构念与依据 | 英文适配题项 | 中文参与者题项 | 计分与用途 |
| --- | --- | --- | --- | --- |
| P1 / 商品分类 | **实用性**；基于 HED/UT 框架 [R3] | “This type of product is mainly useful for accomplishing practical tasks.”; “This type of product helps solve everyday consumption problems.”; “The practical performance of this type of product matters most.” | “这类产品主要用于完成实际任务。”；“这类产品有助于解决日常消费中的实际问题。”；“这类产品最重要的是其实用表现。” | 3 题均值；U 格应更高。 |
| P2 / 商品分类 | **享乐性**；HED/UT 框架 [R3] | “This type of product is mainly chosen for enjoyment.”; “Using this type of product can be pleasurable or stimulating.”; “The experience of this type of product matters most.” | “这类产品主要是为了获得愉悦而选择的。”；“使用这类产品能够带来愉悦或刺激。”；“这类产品最重要的是使用体验。” | 3 题均值；H 格应更高。 |
| P3 / 商品分类 | **象征性承载能力**；象征定位/人格表达 [R1, R4] | “Choosing this type of product can express something about its user.”; “This type of product can be connected with a desired role, lifestyle, or group.”; “Others may infer something about a user from this type of product.”; “This type of product can help people present a desired self-image.” | “选择这类产品能够表达使用者的一些特征。”；“这类产品可以与理想的角色、生活方式或群体联系起来。”；“他人可能会从这类产品推断使用者的某些特征。”；“这类产品可以帮助人们呈现理想的自我形象。” | 4 题均值；HS 格应更高。 |
| P4 / 匹配控制 | 商品熟悉度；产品呈现研究 [R12] | “I am familiar with this type of product.” | “我熟悉这类产品。” | 单题；匹配检查，不是主要协变量。 |
| P5 / 匹配控制 | 预期价格；价格是产品评估线索 [R11] | “I expect this type of product to be expensive.” | “我预计这类产品价格较高。” | 单题；匹配检查。 |
| V1 / 操纵检验 | **功能/Product 阅读**；功能概念与诊断性 [R1, R11] | “This image primarily helps me understand what practical problem the product addresses.” | “这张图片主要帮助我理解该产品解决什么实际问题。” | 单题；比较三种路线均值。 |
| V2 / 操纵检验 | **体验阅读**；体验概念、意象与品牌体验 [R1, R6, R13] | “This image primarily conveys what engaging with the product may feel like.” | “这张图片主要传达与该产品互动时可能是什么感受。” | 单题；比较三种路线均值。 |
| V3 / 操纵检验 | **象征阅读**；象征概念 [R1, R4] | “This image primarily conveys what the product says about a person, role, or group.” | “这张图片主要传达该产品体现了某个人、角色或群体的什么特征。” | 单题；比较三种路线均值。 |
| V4 / 刺激质量 | 产品保真度；受控生成/faithfulness 评估 [R20, R21] | “The advertised product appears to be the same product as the reference product.”; “The image preserves the product’s recognizable design.” | “广告中的产品看起来与参考产品是同一产品。”；“该图片保留了产品可识别的设计特征。” | 2 题均值；仅用于纳入资格。 |
| V5 / 刺激质量 | 感知视觉质量；基于 T2I 质量/一致性评估 [R20, R21] | “The image is visually coherent.”; “The image looks like a plausible advertisement.” | “该图片在视觉上是连贯的。”；“该图片看起来像一则可信的广告。” | 2 题均值；用于质量平衡，不作结果变量。 |

### 表 2：主实验结果、机制与控制变量

| 编号/角色 | 构念与依据 | 英文适配题项 | 中文参与者题项 | 计分与用途 |
| --- | --- | --- | --- | --- |
| Y1 / 共同主要结果 | **广告态度** [R8, R9] | “Overall, I have a favorable opinion of this advertisement.”; “I find this advertisement appealing.”; “I react positively to this advertisement.” | “总体而言，我对这则广告持正面看法。”；“我觉得这则广告有吸引力。”；“我对这则广告的反应是积极的。” | 题库共 3 题；Study 1 的 9 图短版使用前两题取均值，并在 pilot 检验两题相关。与 Y2 做 Holm 校正。 |
| Y2 / 共同主要结果 | **购买考虑**；购买意向框架 [R10] | “I would consider this product if I needed this type of product.”; “I would be willing to learn more before deciding whether to buy it.”; “This advertisement makes me more likely to consider purchasing the product.” | “如果我需要这类产品，我会考虑它。”；“在决定是否购买前，我愿意进一步了解它。”；“这则广告提高了我考虑购买该产品的可能性。” | 题库共 3 题；Study 1 的 9 图短版使用第 1 和第 3 题取均值，并在 pilot 检验两题相关。与 Y1 做 Holm 校正。 |
| M1 / Product 机制 | **感知诊断性**；消费者产品评估 [R11, R12] | “This image gives me useful information for evaluating the product.”; “This image helps me understand how the product could be used.”; “This image helps me judge whether the product would suit my needs.” | “这张图片为我评估该产品提供了有用信息。”；“这张图片帮助我理解该产品可能如何使用。”；“这张图片帮助我判断该产品是否适合我的需要。” | 题库共 3 题；Study 1 的 9 图短版仅使用第 1 题作为过程指标；不报告量表信度，也不作因果中介主张。 |
| M2 / Experiential 机制 | **心理模拟/预期体验**；意象、视觉呈现与品牌体验 [R6, R7, R13] | “While viewing the image, I could imagine myself using or consuming the product.”; “The image made the product-use experience easy to picture.”; “The image gave me a concrete sense of what engagement with the product could feel like.” | “观看图片时，我能想象自己在使用或消费该产品。”；“这张图片让我很容易想象产品的使用体验。”；“这张图片让我具体感到与该产品互动可能是什么体验。” | 题库共 3 题；Study 1 的 9 图短版仅使用第 1 题作为过程指标；不报告量表信度，也不作因果中介主张。 |
| M3 / Symbolic 机制 | **产品—自我联结**；自我—品牌联结与象征消费 [R4, R5] | “This product could fit the kind of person I want to be.”; “Using this product could help express something meaningful about me.”; “I can see a connection between this product and a desired identity, role, or group.” | “该产品可能契合我想成为的那类人。”；“使用该产品可能有助于表达对我有意义的某些特征。”；“我能看到该产品与理想身份、角色或群体之间的联系。” | 题库共 3 题；Study 1 的 9 图短版仅使用第 3 题作为过程指标；不报告量表信度，也不作因果中介主张。 |
| C1 / 操纵检验 | 主导路线 | “Which aspect did this image emphasize most?” 选项：“what practical problem the product addresses”; “what using or consuming it may feel like”; “what it says about a person, role, or group.” | “这张图片最突出的是哪一方面？”选项：“产品解决什么实际问题”；“使用或消费它可能是什么感受”；“它体现某个人、角色或群体的什么特征”。 | 每图一题强制选择。刺激验证仍保留 V1--V3 路线评分；Study 1 使用低负担版本。 |
| C2 / 来源推断 | **推断的 AI 作者性**；AI 中介内容评价 [R18] | “Before being told anything about its origin, how likely did you think this image was made with generative AI?” | “在获知来源之前，您认为这张图片由生成式 AI 制作的可能性有多大？” | 1 = 极不可能；7 = 极有可能。探索性结果。 |
| C3 / 控制 | 商品熟悉度 [R12] | “Before this study, how familiar were you with this type of product?” | “在参加本研究前，您对这类产品有多熟悉？” | 1 = 完全不熟悉；7 = 非常熟悉。描述性/敏感性协变量。 |
| C4 / 控制 | **一般 AI 态度**；GAAIS 正/负双维度适配 [R15] | **Positive:** “AI can bring important benefits to society.”; “I would be comfortable using AI in everyday life.”; “AI can improve the quality of services people receive.” **Negative:** “I feel uneasy about AI becoming widespread.”; “AI creates risks that outweigh its benefits.”; “I tend to distrust AI-supported decisions.” | **正向：**“AI 能为社会带来重要益处。”；“我愿意在日常生活中使用 AI。”；“AI 能改善人们获得服务的质量。” **负向：**“AI 的广泛使用让我感到不安。”；“AI 带来的风险大于其益处。”；“我倾向于不信任 AI 辅助的决策。” | 正向 3 题与负向 3 题分别取均值；不反向后合成总分；仅敏感性控制。 |
| D1 / Study 2 主要结果 | **广告信任**；广告前测信任/可信度传统 [R9, R16] | “I regard this advertisement as trustworthy.”; “I consider the information conveyed by this advertisement credible.”; “I would rely on this advertisement when forming an initial impression of the product.” | “我认为这则广告值得信赖。”；“我认为这则广告传达的信息可信。”；“在形成对该产品的初步印象时，我愿意参考这则广告。” | 题库共 3 题；Study 2 的披露/对照前后短版使用前两题取均值，并在 pilot 检验两题相关及逐题稳健性。 |
| D2 / Study 2 主要结果 | **广告感知真实性**；品牌真实性与 GenAI 研究 [R17, R19] | “This advertisement feels genuine rather than fabricated.”; “The way this product is presented feels authentic.”; “This advertisement seems true to a plausible product-use context.” | “这则广告给人的感觉是真实的，而非拼凑出来的。”；“该产品的呈现方式让我觉得可信真实。”；“这则广告与合理的产品使用情境相符。” | 题库共 3 题；Study 2 的披露/对照前后短版使用前两题取均值，并在 pilot 检验两题相关及逐题稳健性。 |
| D3 / Study 2 过程变量 | **态度性说服知识**；说服知识模型 [R14] | “The way this advertisement was made seems appropriate.”; “The production method behind this advertisement seems fair to viewers.”; “Knowing how this advertisement was made changes how critically I evaluate it.” | “这则广告的制作方式是恰当的。”；“这则广告背后的制作方式对观看者是公平的。”；“了解广告的制作方式会改变我对它进行批判性评价的程度。” | 3 题，单独报告；探索性机制。 |
| D4 / 披露检验 | 披露回忆 [R16, R18] | “What did the message say about how the image was made?” | “提示信息如何说明该图片的制作方式？” | 选择题：生成式 AI / 未说明来源 / 人类摄影师 / 不记得。仅 per-protocol 敏感性分析可据此排除，ITT 主分析不得排除。 |

## 3. 翻译与测量验证

英文适配题由熟悉消费者研究的双语研究者起草；第二位双语译者独立译成中文；第三位不知道英文原题的译者回译；协调小组记录歧义与修改理由。这遵循 Brislin 的翻译—回译原则 [R22]。

在刺激验证前，对 20--30 名中国目标参与者做认知访谈：询问每题的理解，核对“象征性”“真实性”“生成式 AI”等词是否清晰，检查是否产生需求特征。只因理解问题修改题项，并记录修改；确认性数据收集前冻结版本。

不得因为英文原量表已验证就称其为“已验证中文版”。应报告翻译步骤、预测试信度、CFA；只有真正做跨语言比较时才报告测量不变性。

## 4. Study 0：商品分类与刺激验证

### 4.1 商品分类预检验

**问题：** 选定商品能否独立于研究团队直觉、品牌和价格，形成四类目标商品？

**样本与分配：** 从质量控制的中国在线样本面板招募 `N = 480` 有效成年人。采用平衡不完全区组：每人评价 15 个候选商品中的 5 个，每个商品约获 160 份评分。要求 18 岁以上、中文流利，且从未参与本项目其他研究。

**流程：** 呈现去品牌产品参考图和中性类别说明，不呈现广告图；测量 P1--P5，并随机化商品与量表顺序。

**纳入规则：** 每格选择至少 3 个商品。预注册对比标准为：目标取向比另一取向至少高 `0.75` 分且 `d >= .60`；高/低象征组在 P3 上差异 `d >= .80`。同一格内商品不应在熟悉度或预期价格上出现极端离群。应完整报告所有候选商品均值和是否入选；这是一组资格标准，不是事后显著性筛选。

### 4.2 图像刺激验证

按第 1.3 节执行。全体参与者均使用短 S1--S3 表评价全部 36 张图；每个三图商品区块开头展示源图，且不显示策略标签。将图像级评分、固定候选选择规则及所有拒绝图作为研究 artifact 保存。

## 5. Study 1：视觉策略与商品属性的匹配

### 5.1 假设与研究问题

- **H1（功能匹配）：** 对实用型相较享乐型商品，Product-oriented 相对另两种策略的优势更大，并预期伴随更高的感知诊断性（M1）。
- **H2（体验匹配）：** 对享乐型相较实用型商品，Experiential-oriented 的优势更大，并预期伴随更高的心理模拟（M2）。
- **H3（象征匹配）：** 对高相较低象征性承载能力商品，Symbolic-oriented 的优势更大，并预期伴随更高的产品—自我联结（M3）。
- **H4（整合匹配）：** `策略 × 实用/享乐 × 象征性` 交互是确认性检验；H1--H3 未蕴含的条件内精确排名均标记为探索性，避免武断地为 U-HS/H-HS 设定唯一最优图。
- **RQ1：** 在尚未披露来源前，策略是否影响参与者推断图片由 AI 制作的可能性？

H1--H3 对 Y1/Y2 两个共同主要结果同时检验，并对二者进行 Holm 校正。M1--M3 是预注册机制变量，不是额外主要终点。

### 5.2 设计与样本量

Study 1 改为混合设计：`3（策略，组内）× 3（具体商品 exemplar，组内）× 2（实用/享乐，组间）× 2（低/高象征性，组间）`。每名参与者随机分配到一个商品属性格，然后评价该格中保留的全部三个具体商品；每个商品均观看 Product-oriented、Experiential-oriented、Symbolic-oriented 三张图，共完成 9 次图像评价。因此，策略与具体商品的比较都在同一参与者内部完成；商品类型仍是组间变量。

| 分配组别 | 有效样本 | 每位参与者做什么 |
| --- | ---: | --- |
| U-LS 商品格 | 60 | 评价 `3 个商品 × 3 种策略 = 9` 张图 |
| U-HS 商品格 | 60 | 评价 `3 个商品 × 3 种策略 = 9` 张图 |
| H-LS 商品格 | 60 | 评价 `3 个商品 × 3 种策略 = 9` 张图 |
| H-HS 商品格 | 60 | 评价 `3 个商品 × 3 种策略 = 9` 张图 |
| **Study 1 总计** | **240** | **每人完成 9 次图像评价** |

暂定 `N=240` 时，每张“具体商品 × 策略”图获得 60 个独立评分；每个“商品类型 × 策略”组合则有 `3 个商品 × 60 人 = 180` 次图像级评价。同一参与者的 9 次图像评分相关，绝不能误当作 9 个独立参与者。人数得以降低，是因为每人完整交叉评价三个商品与三种策略，而不是因为重复评分可以替代功效分析。正式招募前仍须以实际 12 个商品、pilot 得到的重复测量相关性、`alpha=.05`、最小 H1--H3 策略×商品属性对比及预期无效样本进行模拟确认。仅当模拟达到预注册功效标准时才采用此人数（资源受限主研究建议至少 `80%` power）；否则提高每个商品格人数。产品 exemplar 仍是抽样变异来源，因此仍需混合模型与模拟功效 [R23]。去品牌白底源图基线不再并入核心 Study 1；若后续确实需要，可单独进行小型校准研究，而不在这里增加第四次重复曝光。

### 5.3 流程

1. 知情同意；年龄、语言、重复参与和屏幕尺寸资格检查。
2. 随机分配到一个商品格；参与者将评价该格的全部三个 exemplar，及每个 exemplar 的全部三种策略图（`3 × 3 = 9` 个 trial）。
3. 使用预先生成的受约束随机顺序：同一源商品不得相邻出现；在同一商品格内，商品与策略在第 1--9 个位置尽可能均衡；不得显示 Product/Experiential/Symbolic 标签。图像逐张展示，绝不并排；每张至少观看 6 秒，允许继续查看。
4. 每看完一张图立即完成 Study 1 短量表：Y1 两题、Y2 两题、M1/M2/M3 各一项预选指标、一题 C1 主导路线选择题及 C2；这些图像级测量前不提及 AI。
5. 看完九张图后，分别测量三个商品的 C3 熟悉度、C4、一题指示性注意力检查、人口统计，并用不引导的开放题询问参与者认为研究在考察什么。开放题由不了解条件的研究者编码，用于诊断是否猜到假设，不作为排除规则。
6. 真实 debrief：九张图均由 AI 基于去品牌产品参考图生成，分别旨在突出不同的视觉意义。

### 5.4 排除与主分析

ITT 样本仅排除：撤回同意、重复平台 ID/设备指纹、不符合年龄/语言资格、未通过指示性注意力题、图像未成功加载或完成时间低于预测试中位数三分之一。不得根据条件、结果高低、AI 来源推断、产品喜欢程度或猜到研究目的排除。另报告纳入所有非重复完整样本的敏感性分析。

对 Y1、Y2 分别拟合效应编码混合模型：

```text
Y ~ strategy * product_orientation * symbolic_affordance
    + presentation_position
    + (1 | participant) + (1 | product_exemplar)
```

`strategy` 与 `product_exemplar` 是组内变量；`product_orientation` 与 `symbolic_affordance` 是 Study 0 确立的商品格属性。`presentation_position` 控制第 1--9 次曝光。不得把曝光后的过程指标放入主结果协变量模型。以 H1--H3 的计划对比报告系数、95% CI、标准化效应量、各 cell 均值和完整交互；并预注册探索性的 `strategy × presentation_position`，诊断顺序、疲劳或逐步猜到假设的影响。由于每个 `商品 × 策略` 只有一张生成图，推断针对这套预注册刺激和 prompt pipeline；它不估计同一 prompt 不同 rendering 的方差。

在 9 图版本中，M1--M3 是单题、以理论为基础的过程指标。预注册估计各策略的多层差异，并报告它们与 Y1/Y2 的关联，表述为“**与理论机制一致的过程证据**”；不得称为因果中介，也不得把它们称为经过心理测量验证的多题量表。熟悉度和一般 AI 态度仅进入敏感性模型。

## 6. Study 2：AI 披露的因果效应

### 6.1 设计逻辑

Khatiwada 等人的 CHI 新闻研究先测量未披露来源时的内容评价，再披露 LLM 参与并引导反思 [R18]。这能避免来源标签过早污染初始评价。但单纯前后测无法区分披露、重复答题与反思。因此本研究在初次评价后随机给予真实 AI 披露或**等时中性反思对照**。

### 6.2 设计与样本量

只使用通过验证的 GenAI 广告图，构成 `3（策略，组内）× 3（具体商品 exemplar，组内）× 2（商品取向，组间）× 2（象征性，组间）× 2（后曝光信息，组间）` 的混合设计；`time`（披露/反思前、后）亦为组内变量。每名参与者在一个商品类型格内完整经历同一组 `3 商品 × 3 策略 = 9` 张图的前后两轮测量。

| 分配组别 | 每格有效样本 | 每位参与者做什么 |
| --- | ---: | --- |
| U-LS × AI 披露 | 30 | 对该格 9 张图完成披露前后 D1/D2 评价 |
| U-LS × 中性反思 | 30 | 对该格 9 张图完成两轮 D1/D2 评价 |
| U-HS × AI 披露 | 30 | 对该格 9 张图完成披露前后 D1/D2 评价 |
| U-HS × 中性反思 | 30 | 对该格 9 张图完成两轮 D1/D2 评价 |
| H-LS × AI 披露 | 30 | 对该格 9 张图完成披露前后 D1/D2 评价 |
| H-LS × 中性反思 | 30 | 对该格 9 张图完成两轮 D1/D2 评价 |
| H-HS × AI 披露 | 30 | 对该格 9 张图完成披露前后 D1/D2 评价 |
| H-HS × 中性反思 | 30 | 对该格 9 张图完成两轮 D1/D2 评价 |
| **Study 2 总计** |  | **240** |

暂定 `N=240` 时，每个“商品类型 × 后曝光信息”格有 30 名独立参与者；同一格的每张“具体商品 × 策略”图在每个信息条件下有 30 人的前后配对评分。主要披露检验汇总全部商品类型，检验 `time × disclosure` 与 `time × disclosure × strategy`；后者利用每人三种策略的组内比较。`time × disclosure × strategy × 商品属性` 等更高阶调节只作探索性分析。与 Study 1 一样，最终人数必须由 pilot 的重复测量相关性、披露效应大小和预期排除比例的模拟功效分析确认；若主 `time × disclosure` 或策略调节检验达不到预注册的 80% power，则增加每个“商品类型 × 信息”格的人数。

### 6.3 完整处理文字

两种页面具有相同布局、最低阅读时间和“继续”按钮。

**AI 披露条件**

> 您刚才评价的九张广告图片均由生成式 AI 系统基于去品牌化的产品参考图和研究定义的视觉指令生成。它们是研究材料，并不构成商业产品承诺。

**等时中性反思对照**

> 请花一点时间再次查看您刚才评价的广告图片。接下来的问题将询问您目前对它们的印象。

两组参与者均在 debrief 中获知图像确由生成式 AI 制作；对照组绝不接收“人类制作”的虚假来源信息。

### 6.4 流程与分析

1. 同 Study 1 完成同意与资格检查；随机分配到一个商品类型格，参与者评价该格全部 `3 商品 × 3 策略 = 9` 张图。
2. **披露前阶段：** 用与 Study 1 相同的受约束随机顺序逐张展示 9 张图；每张图后测 D1/D2 的预注册两题短版与 C2。此阶段不提及 AI。
3. 随机呈现 AI 披露或等时中性反思。信息在九张图的第一次评价之后、第二次评价之前出现一次。
4. **披露/反思后阶段：** 以另一条受约束随机顺序重新展示同九张图；每张图后重测 D1/D2 两题短版。为避免重复购买问题引发额外思考，不重测 Y1/Y2；如保留，必须预注册为仅探索性的单题结果。
5. 测 D3/D4、三个商品的 C3 熟悉度、C4、注意力与人口统计，随后真实 debrief。

Study 2 主要结果为 D1 广告信任与 D2 感知真实性的变化。为使 18 次图像曝光仍可行，D1/D2 在 Study 2 中使用预注册的两题短版；不将其宣称为完整三题量表，也不将重复 Y1/Y2 作为确认性结果。

对每个主要结果拟合：

```text
Y ~ time * disclosure * strategy
    + product_orientation + symbolic_affordance + phase_position
    + (1 | participant) + (1 | product_exemplar)
```

`time × disclosure` 是 AI 标签相对“单纯重看/反思”的因果效应；`time × disclosure × strategy` 检验该效应是否因三种策略不同。`phase_position` 控制各阶段第 1--9 次图片展示；第二轮使用独立受约束顺序。报告披露前平衡、差异中的差异估计、95% CI，并对 D1/D2 做 Holm 校正。D3 只作探索性过程证据，不进入主要结果回归。

## 7. 预注册、数据质量与伦理

在查看任何结果前预注册：Study 0 的商品/图像选择规则、固定效应与计划对比、主要结果、模拟功效、排除规则、处理文字以及确认性/探索性边界。对 prompt、manifest、问卷和代码进行时间戳版本控制。

招募前获得伦理审批。知情同意须说明：参与者将观看广告风格图像，可能接触 AI 生成材料，可无惩罚退出，且不需要购买任何产品。除非有额外伦理批准，不使用健康、高金融风险、儿童、酒精或容易激化身份刻板印象的类别。不得对任何参与者谎称 AI 图像由人类制作。报酬应达到或超过样本平台适用的公平时薪。

在源图和零售素材权利允许时发布：去品牌源图、完整 prompt、输出哈希、筛选 rubric、stimulus manifest、问卷、匿名化数据、预注册和分析代码。若源图不可再分发，应发布哈希与权利限制说明。

## 8. 变量—操作化—依据追溯表

| 元素 | 本方案操作化 | 文献依据 |
| --- | --- | --- |
| 三种视觉策略 | 在受控商品图上形成主导功能、体验或象征阅读 | Park 等 [R1]；Homburg 等 [R2] |
| 实用/享乐商品分类 | P1/P2 商品类别预检验，而非研究者标签 | Voss 等 [R3] |
| 象征性承载能力 | P3 身份/角色/群体/自我表达预检验 | Park 等 [R1]；Bhat & Reddy [R4] |
| 体验路径 | 与产品相关的参与者中心消费呈现；M2 | MacInnis & Price [R6]；Elder & Krishna [R7] |
| 象征机制 | M3 产品—自我联结 | Escalas [R5] |
| 广告结果 | Y1 广告态度、Y2 购买考虑 | MacKenzie 等 [R8]；Spears & Singh [R10] |
| AI 来源 | 未披露的来源推断，再到真实披露/等时反思 | Khatiwada 等 [R18]；Koning & Voorveld [R16] |
| 披露后信任/真实性 | D1/D2 前后测量 | MacKenzie & Lutz [R9]；Morhart 等 [R17]；Brüns & Meißner [R19] |
| 刺激抽样与功效 | 多商品 exemplar、组内策略比较、混合模型和模拟功效 | Westfall 等 [R23] |
| 跨语言处理 | 双语适配、回译、认知访谈、CFA | Brislin [R22] |

## 参考文献

参考文献与 DOI 完全沿用英文版的 [References](chi2027_genai_ad_experiment_protocol.md#references)，以避免中英文两份文件的书目信息漂移。核心来源均为同行评审发表物；R20--R21 是用于生成/保真流程的 HCI 或计算机视觉文献，不作为消费者主要构念的唯一依据；没有 arXiv-only 文献被用作主要结果、中介或操纵检验的唯一依据。

| 编号 | 文献 |
| --- | --- |
| R1 | Park, Jaworski, & MacInnis (1986), *Strategic Brand Concept-Image Management*. https://doi.org/10.1177/002224298605000401 |
| R2 | Homburg, Schwemmle, & Kuehnl (2015), *New Product Design*. https://doi.org/10.1509/jm.14.0199 |
| R3 | Voss, Spangenberg, & Grohmann (2003), *Measuring the Hedonic and Utilitarian Dimensions of Consumer Attitude*. https://doi.org/10.1509/jmkr.40.3.310.19238 |
| R4 | Bhat & Reddy (1998), *Symbolic and Functional Positioning of Brands*. https://doi.org/10.1108/07363769810202664 |
| R5 | Escalas (2004), *Narrative Processing*. https://doi.org/10.1207/s15327663jcp1401&2_19 |
| R6 | MacInnis & Price (1987), *The Role of Imagery in Information Processing*. https://doi.org/10.1086/209082 |
| R7 | Elder & Krishna (2012), *The Visual Depiction Effect in Advertising*. https://doi.org/10.1086/661531 |
| R8 | MacKenzie, Lutz, & Belch (1986), *The Role of Attitude Toward the Ad*. https://doi.org/10.1177/002224378602300205 |
| R9 | MacKenzie & Lutz (1989), *Structural Antecedents of Attitude Toward the Ad*. https://doi.org/10.1177/002224298905300204 |
| R10 | Spears & Singh (2004), *Measuring Attitude Toward the Brand and Purchase Intentions*. https://doi.org/10.1080/10641734.2004.10505164 |
| R11 | Kempf & Smith (1998), *Consumer Processing of Product Trial*. https://doi.org/10.1177/002224379803500304 |
| R12 | Jiang & Benbasat (2007), *Functional Mechanisms of Online Product Presentations*. https://doi.org/10.1287/isre.1070.0124 |
| R13 | Brakus, Schmitt, & Zarantonello (2009), *Brand Experience*. https://doi.org/10.1509/jmkg.73.3.052 |
| R14 | Campbell (1995), *Advertising Tactics and Manipulative Intent*. https://doi.org/10.1086/209419 |
| R15 | Schepman & Rodway (2023), *GAAIS*. https://doi.org/10.1080/10447318.2022.2085400 |
| R16 | Koning & Voorveld (2025), *Disclaimer! This Content Is AI-Generated*. https://doi.org/10.1080/15252019.2025.2554149 |
| R17 | Morhart et al. (2015), *Brand Authenticity*. https://doi.org/10.1016/j.jcps.2014.11.006 |
| R18 | Khatiwada et al. (2026), *When AI Rewrites the News*. 项目本地 PDF：[`local_only/When AI Rewrites the News How Sentiment, Framing, and LLM Disclosure Shape Perceptions.pdf`](../local_only/When%20AI%20Rewrites%20the%20News%20How%20Sentiment%2C%20Framing%2C%20and%20LLM%20Disclosure%20Shape%20Perceptions.pdf) |
| R19 | Brüns & Meißner (2024), *Do You Create Your Content Yourself?* https://doi.org/10.1016/j.jretconser.2024.103790 |
| R20 | Liu & Chilton (2022), *Design Guidelines for Prompt Engineering Text-to-Image Generative Models*. https://doi.org/10.1145/3491102.3501825 |
| R21 | Hu et al. (2023), *TIFA*. https://doi.org/10.1109/ICCV51070.2023.01875 |
| R22 | Brislin (1970), *Back-Translation for Cross-Cultural Research*. https://doi.org/10.1177/135910457000100301 |
| R23 | Westfall, Kenny, & Judd (2014), *Statistical Power and Optimal Design*. https://doi.org/10.1037/xge0000014 |

### 完整 APA 7 书目信息

- **[R1]** Park, C. W., Jaworski, B. J., & MacInnis, D. J. (1986). Strategic brand concept-image management. *Journal of Marketing, 50*(4), 135--145. https://doi.org/10.1177/002224298605000401
- **[R2]** Homburg, C., Schwemmle, M., & Kuehnl, C. (2015). New product design: Concept, measurement, and consequences. *Journal of Marketing, 79*(3), 41--56. https://doi.org/10.1509/jm.14.0199
- **[R3]** Voss, K. E., Spangenberg, E. R., & Grohmann, B. (2003). Measuring the hedonic and utilitarian dimensions of consumer attitude. *Journal of Marketing Research, 40*(3), 310--320. https://doi.org/10.1509/jmkr.40.3.310.19238
- **[R4]** Bhat, S., & Reddy, S. K. (1998). Symbolic and functional positioning of brands. *Journal of Consumer Marketing, 15*(1), 32--43. https://doi.org/10.1108/07363769810202664
- **[R5]** Escalas, J. E. (2004). Narrative processing: Building consumer connections to brands. *Journal of Consumer Psychology, 14*(1--2), 168--180. https://doi.org/10.1207/s15327663jcp1401&2_19
- **[R6]** MacInnis, D. J., & Price, L. L. (1987). The role of imagery in information processing: Review and extensions. *Journal of Consumer Research, 13*(4), 473--491. https://doi.org/10.1086/209082
- **[R7]** Elder, R. S., & Krishna, A. (2012). The visual depiction effect in advertising: Facilitating embodied mental simulation through product orientation. *Journal of Consumer Research, 38*(6), 988--1003. https://doi.org/10.1086/661531
- **[R8]** MacKenzie, S. B., Lutz, R. J., & Belch, G. E. (1986). The role of attitude toward the ad as a mediator of advertising effectiveness: A test of competing explanations. *Journal of Marketing Research, 23*(2), 130--143. https://doi.org/10.1177/002224378602300205
- **[R9]** MacKenzie, S. B., & Lutz, R. J. (1989). An empirical examination of the structural antecedents of attitude toward the ad in an advertising pretesting context. *Journal of Marketing, 53*(2), 48--65. https://doi.org/10.1177/002224298905300204
- **[R10]** Spears, N., & Singh, S. N. (2004). Measuring attitude toward the brand and purchase intentions. *Journal of Current Issues & Research in Advertising, 26*(2), 53--66. https://doi.org/10.1080/10641734.2004.10505164
- **[R11]** Kempf, D. S., & Smith, R. E. (1998). Consumer processing of product trial and the influence of prior advertising: A structural modeling approach. *Journal of Marketing Research, 35*(3), 325--338. https://doi.org/10.1177/002224379803500304
- **[R12]** Jiang, Z., & Benbasat, I. (2007). Investigating the influence of the functional mechanisms of online product presentations. *Information Systems Research, 18*(4), 454--470. https://doi.org/10.1287/isre.1070.0124
- **[R13]** Brakus, J. J., Schmitt, B. H., & Zarantonello, L. (2009). Brand experience: What is it? How is it measured? Does it affect loyalty? *Journal of Marketing, 73*(3), 52--68. https://doi.org/10.1509/jmkg.73.3.052
- **[R14]** Campbell, M. C. (1995). When attention-getting advertising tactics elicit consumer inferences of manipulative intent: The importance of balancing benefits and investments. *Journal of Consumer Research, 21*(4), 715--739. https://doi.org/10.1086/209419
- **[R15]** Schepman, A., & Rodway, P. (2023). The general attitudes towards artificial intelligence scale (GAAIS): Confirmatory validation and associations with personality, corporate distrust, and general trust. *International Journal of Human--Computer Interaction, 39*(13), 2724--2741. https://doi.org/10.1080/10447318.2022.2085400
- **[R16]** Koning, B., & Voorveld, H. A. M. (2025). Disclaimer! This content is AI-generated: How AI-disclosures influence trust in advertisements and organizations. *Journal of Interactive Advertising, 25*(3), 240--253. https://doi.org/10.1080/15252019.2025.2554149
- **[R17]** Morhart, F., Malär, L., Guèvremont, A., Girardin, F., & Grohmann, B. (2015). Brand authenticity: An integrative framework and measurement scale. *Journal of Consumer Psychology, 25*(2), 200--218. https://doi.org/10.1016/j.jcps.2014.11.006
- **[R18]** Khatiwada, P., Pappu, V., Bagozzi, B. E., & Mauriello, M. L. (2026). *When AI rewrites the news: How sentiment, framing, and LLM disclosure shape perceptions*. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. 项目提供的本地 PDF：[`local_only/When AI Rewrites the News How Sentiment, Framing, and LLM Disclosure Shape Perceptions.pdf`](../local_only/When%20AI%20Rewrites%20the%20News%20How%20Sentiment%2C%20Framing%2C%20and%20LLM%20Disclosure%20Shape%20Perceptions.pdf)
- **[R19]** Brüns, J. D., & Meißner, M. (2024). Do you create your content yourself? Using generative artificial intelligence for social media content creation diminishes perceived brand authenticity. *Journal of Retailing and Consumer Services, 79*, 103790. https://doi.org/10.1016/j.jretconser.2024.103790
- **[R20]** Liu, V., & Chilton, L. B. (2022). Design guidelines for prompt engineering text-to-image generative models. In *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3491102.3501825
- **[R21]** Hu, Y., Liu, B., Kasai, J., Wang, Y., Ostendorf, M., Krishna, R., & Smith, N. A. (2023). TIFA: Accurate and interpretable text-to-image faithfulness evaluation with question answering. In *Proceedings of ICCV 2023*, 20406--20417. https://doi.org/10.1109/ICCV51070.2023.01875
- **[R22]** Brislin, R. W. (1970). Back-translation for cross-cultural research. *Journal of Cross-Cultural Psychology, 1*(3), 185--216. https://doi.org/10.1177/135910457000100301
- **[R23]** Westfall, J., Kenny, D. A., & Judd, C. M. (2014). Statistical power and optimal design in experiments in which samples of participants respond to samples of stimuli. *Journal of Experimental Psychology: General, 143*(5), 2020--2045. https://doi.org/10.1037/xge0000014
