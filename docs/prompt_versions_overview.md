# Prompt 版本说明与文献依据

本文档整理当前仓库中的广告图生成 prompt 版本，重点说明每个版本解决什么问题、运行时使用哪组三类取向、prompt 中显式引用了什么文献，以及设计上主要依据哪些文献或工程化指南。

## 总体脉络

当前 prompt 体系大致分成两代：

| 版本范围                     | 三类取向                                                                 | 核心逻辑                                                                                         | 文献状态                                                                            |
| ---------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| `current`, `function_v2` | `Product-oriented` / `Context-oriented` / `Symbolic-oriented`      | 旧版三分类：产品诊断、使用情境、自我表达/品牌意义                                                | prompt 中基本不显式引用论文，但可由广告诉求、图片说服、心理想象、视觉修辞等文献支撑 |
| `v3`-`v17`               | `Product-oriented` / `Symbolic-oriented` / `Experiential-oriented` | Park, Jaworski, and MacInnis (1986) 的 functional / symbolic / experiential brand concept 三分法 | prompt 中显式引用 Park et al. (1986)；其他文献主要作为设计和操纵检验依据            |

最重要的概念转换是：旧版的 `Context-oriented` 在新版中不再作为独立理论标签，而是被并入 Park 框架下的 `Experiential-oriented`；旧版的 `Affect-oriented` 或情绪/氛围取向更接近新版的 `Symbolic-oriented`，但二者并不完全等同。

## 核心理论框架

### Park et al. (1986)

`v3` 到 `v17` 的主理论来源是：

Park, C. W., Jaworski, B. J., & MacInnis, D. J. (1986). Strategic Brand Concept-Image Management. Journal of Marketing, 50(4), 135-145.

在本项目中，Park et al. 的三类 brand concept 被转译为三类生成广告图：

| Park brand concept | 本项目取向                | 视觉生成目标                                             |
| ------------------ | ------------------------- | -------------------------------------------------------- |
| Functional         | `Product-oriented`      | 让商品和外部消费问题、实际任务、可靠性、功能效用相连接   |
| Symbolic           | `Symbolic-oriented`     | 让商品承载自我形象、身份、角色、群体归属、品味或象征意义 |
| Experiential       | `Experiential-oriented` | 让商品连接感官愉悦、多样性、认知刺激、沉浸感或消费体验   |

注意：Park et al. (1986) 是品牌概念与品牌形象管理框架，不是广告图片类型分类文献。本项目的做法是把品牌概念转译成可生成、可操纵、可检验的广告图视觉取向。

### 辅助文献

这些文献主要用于解释为什么三类图像操纵有理论合理性，但它们通常没有直接写进 prompt 文本。

| 文献传统                 | 代表文献                                                                                                   | 对本项目的作用                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 品牌利益与品牌资产       | Keller (1993)                                                                                              | 用 functional / experiential / symbolic benefits 连接品牌联想和品牌资产，补强 Park 三分类的品牌理论位置                   |
| 产品相关 vs 情感图片     | Miniard et al. (1991)                                                                                      | 支撑 Product 与 Affect/Symbolic 的分离：product-relevant pictures 与 affect-laden pictures 可能走不同说服路径             |
| 信息型 vs 情绪型广告诉求 | Chandy et al. (2001), Guitart & Stremersch (2021), Akpinar & Berger (2017), Resnik & Stern (1977)          | 支撑 Product-oriented 的功能、属性、购买相关信息路径，也解释传统二分法为何不足以区分 Context/Experiential 与 Symbolic     |
| 使用想象与自我代入       | MacInnis & Price (1987), Elder & Krishna (2012), Escalas (2007)                                            | 支撑旧版 `Context-oriented` 和新版 `Experiential-oriented` 中的 usage simulation、mental imagery、embodied simulation |
| 体验消费与品牌体验       | Holbrook & Hirschman (1982), Hirschman & Holbrook (1982), Brakus et al. (2009)                             | 支撑 experiential/hedonic/sensory consumption，不把消费只看成信息处理                                                     |
| 视觉修辞与象征意义       | Scott (1994), McQuarrie & Mick (1999)                                                                      | 支撑 `Symbolic-oriented` 中的隐喻、氛围、视觉修辞和意义生成                                                             |
| 品牌人格与调性           | Aaker (1997)                                                                                               | 支撑 symbolic 图像中的品牌人格、身份感和自我表达                                                                          |
| 广告视觉执行变量         | Pieters & Wedel (2004), Houston et al. (1987), Hartmann et al. (2021), Li & Xie (2020), Dang et al. (2026) | 支撑产品面积、图文一致性、packshot/使用视角/人物可见性、视觉质量等横向控制变量                                            |

## 版本总览

| 版本            | 运行时三类取向                    | 语言/流程                                                   | prompt 中显式引用                                                                             | 主要设计依据                                                                                                                               | 版本定位                                                                                                 |
| --------------- | --------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| `current`     | Product / Context / Symbolic      | 英文运行 prompt，另有中文参考文件                           | 无显式论文引用                                                                                | 本地三分类：product diagnostic、usage imagination、symbolic meaning；可由 Miniard et al.、MacInnis & Price、Scott、McQuarrie & Mick 等支撑 | 旧版基线，强调三种广告图说服路径，但不直接采用 Park 三品牌概念命名                                       |
| `function_v2` | Product / Context / Symbolic      | 英文运行 prompt，另有中文参考文件                           | 无显式论文引用                                                                                | 在 `current` 基础上强化功能证据、使用情境、象征意义的边界；后续 `v7`、`v12`、`v13` 借鉴其质量控制                                  | 旧版增强版，尤其强化 Product 的多维功能展示和三类之间的失败规则                                          |
| `v3`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park functional / symbolic / experiential brand concept                                                                                    | 第一个明确 Park-theory-grounded 的长版 prompt                                                            |
| `v4`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park 定义 + input grounding + generalization discipline                                                                                    | 精简 definition-first 版本，减少过多微观场景细节                                                         |
| `v5`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park brand concept definition                                                                                                              | concept-only 测试版，用来观察只给理论定义时模型是否能形成三类差异                                        |
| `v6`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park 定义 + 商品保持 + 基础质量控制                                                                                                        | 平衡版，恢复产品一致性、禁止虚假 claims、产品清晰可见等实验控制                                          |
| `v7`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park 定义 +`function_v2` 式图像质量/保真控制                                                                                             | 质量强化版，因为项目内经验显示 v2 风格控制能提升成图可用性                                               |
| `v8`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park 原始定义 + 最少质量控制                                                                                                               | 回到理论定义本身，减少工程提示对操纵的干扰                                                               |
| `v9`          | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | `v8` + 选定 `function_v2` 细节控制                                                                                                     | 在 Park 原始定义基础上补回产品主体、无新增文字、artifact avoidance 等关键约束                            |
| `v10`         | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | Park 定义 + grounded product facts + prompt-image alignment + artifact control + discriminant validity                                     | 综合研究版，开始明确把对齐、忠实度和三类区分度写进 prompt                                                |
| `v11`         | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | `v10` + source-image-first grounding                                                                                                     | 强化白底源图优先：先读可见事实，再用 metadata 辅助概念推断                                               |
| `v12`         | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | `function_v2` 视觉执行纪律 + Park 三定义                                                                                                 | 把旧版 v2 的视觉方向、推理步骤和 verification discipline 直接嫁接到 Park 三分类                          |
| `v13`         | Product / Symbolic / Experiential | 英文运行 prompt，另有中文 review 文件                       | Park et al. (1986)                                                                            | `v12` + source-image-first grounding + 三类 discriminant separation                                                                      | 更强区分度版本，强调“如果能轻易换标签就是失败”                                                         |
| `v14`         | Product / Symbolic / Experiential | 中文运行 prompt                                             | Park et al. (1986)                                                                            | `v13` 的中文化/轻量化表达                                                                                                                | 中文版 prompt，保留 Park 三类定义，但相比 v13 明显更短、更少控制条款                                     |
| `v15`         | Product / Symbolic / Experiential | 中文两阶段流程                                              | wrapper 显式引用 Park et al. (1986)；neutral prompt 不引用文献                                | Park 三分类 + prompt decomposition + source grounding                                                                                      | 先根据 metadata 与白底图生成中性商品 prompt，再把中性 prompt 注入三类风格 wrapper                        |
| `v16`         | Product / Symbolic / Experiential | 英文两阶段流程                                              | wrapper 显式引用 Park et al. (1986)；neutral prompt 不引用文献                                | `v15` 英文化 + Park 三分类 + 多维功能展示控制                                                                                            | `v15` 的全英文版；Product 部分强化多维功能证据                                                         |
| `v17`         | Product / Symbolic / Experiential | 英文 orientation-specific prompt generation + final wrapper | final wrapper 显式引用 Park et al. (1986)；generator 不一定直接写 Park 名称，但会指定目标取向 | Park 三分类 + 双重强调流程 + Alibaba Cloud 文生图提示指南式真实摄影约束                                                                    | 当前最新思路：先生成已经融合某一取向的商品专属 prompt，再由 final wrapper 重复三类理论定义和真实摄影要求 |

## 从 `current` 到 `v17` 的逐版构建变化

下表不再只说“版本定位”，而是明确说明每一版相对前一版增加了什么、弱化了什么，以及构建逻辑的主轴如何变化。

| 版本 | 相对前版的构建基线 | 主要新增 | 主要删减或弱化 |
| --- | --- | --- | --- |
| `current` | 旧版起点 | Product / Context / Symbolic 三路说服框架；Product diagnostic、usage imagination、symbolic meaning | 无 Park 显式理论标注；几乎无统一的 grounded generation 控制 |
| `function_v2` | `current` | 更强的功能证据、使用场景约束、象征边界；更像受控实验 prompt | 弱化“只要好看即可”的宽松视觉空间 |
| `v3` | `function_v2` 之后的理论重写 | Park functional / symbolic / experiential 三定义正式进入 prompt | 放弃旧版 `Context-oriented` 理论标签 |
| `v4` | `v3` | definition-first；减少微观视觉清单；强化 input grounding | 弱化 `v3` 的长版细节指导 |
| `v5` | `v4` | 保留理论定义作为主要操纵；形成 concept-only 测试版 | 大幅删去质量控制、保真控制和视觉执行纪律 |
| `v6` | `v5` | 恢复商品保持、无新增文字、无虚假 claims、商品可识别、基础摄影感 | 不再完全依赖理论定义自行驱动成图 |
| `v7` | `v6` | 借回 `function_v2` 式 fidelity、artifact avoidance、verification discipline | 弱化“最少控制”的纯理论状态 |
| `v8` | `v7` | 回到 Park 原始定义优先；只保留最小视觉控制 | 删去 `v7` 中较重的执行与验证条款 |
| `v9` | `v8` | 选择性补回产品主体清晰、无新增文字、artifact avoidance 等关键控制 | 不回到 `function_v2` 那种较长的控制清单 |
| `v10` | `v9` | grounded product facts、prompt-image alignment、artifact control、discriminant validity | 弱化“只看定义、不看对齐和操纵检验”的做法 |
| `v11` | `v10` | source-image-first grounding：先读白底图，再用 metadata 支撑推断 | 弱化 metadata 对可见事实的覆盖权重 |
| `v12` | `v11` | 直接融合 `function_v2` 的 visual direction、reasoning steps、verification discipline | 放弃更松散的 definition-first 执行方式 |
| `v13` | `v12` | 更强的三类分离规则；“可被重命名即失败”；所有 route 都改成 source-image-first | 删去部分项目化 personality taxonomy 与启发式清单 |
| `v14` | `v13` | 中文化、轻量化表达 | 弱化英文长版中的若干细控制条款 |
| `v15` | `v14` | 两阶段流程：先生成 neutral product prompt，再注入三类 wrapper | 不再让一个 prompt 同时承担 grounding 与 route 操纵 |
| `v16` | `v15` | 英文化；Product 强化多维 functional evidence | 弱化中文流程在人工审查上的便利性 |
| `v17` | `v16` | orientation-specific generator；final wrapper 二次强调理论与真实摄影；prompt structure 更完整 | 不再使用 neutral prompt 作为第一阶段中间层 |

## 旧版本到研究条件重构映射

为方便实验设计，本项目基于历史版本又抽出三套研究条件化 alias。它们不是逐字镜像副本，而是保留控制强度与理论内核后的规范化派生版。

| 新研究条件 | 主要来源 | 运行形态 | 继承重点 | 规范化调整 |
| --- | --- | --- | --- | --- |
| `definition-only` | `v5` | 单阶段 | Park 定义主导；最少控制 | 统一开头语气、metadata 段与 failure rule，使三取向可平行比较 |
| `visual-control` | `v8` | 单阶段 | Park 定义优先；最小但明确的视觉与真实感控制 | 统一 source-product、no-text、realism 和 contamination failure 的表达方式 |
| `genprompt-control` | `v17` | 两阶段 | orientation-specific generator + final wrapper 双阶段控制 | 统一 generator / wrapper 结构，并把工程性真实摄影约束与理论 route 控制分层表达 |

## 各版本的设计逻辑

### `current(V1)`

`current` 是旧版基线。它使用 `Product-oriented`、`Context-oriented`、`Symbolic-oriented` 三类：

- Product 强调产品清晰度、功能价值和 visual information diagnosticity。
- Context 强调具体使用情境、使用想象和 self-reference。
- Symbolic 强调品牌人格、自我表达、身份象征和视觉修辞。

这一版不在 prompt 里显式写入论文名称。理论上，它可由以下文献支撑：Miniard et al. (1991) 的 product-relevant vs affect-laden pictures、MacInnis & Price (1987) 的 imagery processing、Escalas (2007) 的 self-referencing、Scott (1994) 与 McQuarrie & Mick (1999) 的 visual rhetoric、Aaker (1997) 的 brand personality。

### `function_v2`

`function_v2` 仍沿用旧版三类，但比 `current` 更像受控实验 prompt：

- Product 从“产品清晰”进一步收紧为“功能效用、操作、问题-解决证据”。
- Context 更严格地要求单一、具体、真实的使用场景。
- Symbolic 更明确地区分 meaning / identity / brand personality，而不是一般好看或氛围化。

这一版也没有显式引用论文，但它后来成为 `v7`、`v12`、`v13` 质量控制的来源。尤其是 Product 的功能展示逻辑后来被继续强化为“多维功能证据”，例如 operation/interface、fit/fastening、scale reference、storage、compatibility、care、gift-readiness 等。

### `v3`

`v3` 是第一次把 prompt 明确迁移到 Park et al. (1986) 的 brand concept-image management 框架。它把三类改成：

- Product-oriented = functional brand concept。
- Symbolic-oriented = symbolic brand concept。
- Experiential-oriented = experiential brand concept。

这一步的意义是：三类不再只是“画面长什么样”，而是先有一个消费者需求层面的品牌概念，再把它转译成图像。

### `v4`

`v4` 是 concise definition-first 版本。相比 `v3`，它减少了长段视觉细节，让 prompt 更围绕 Park 定义本身和输入 grounding 展开。它适合测试“理论定义 + 少量生成边界”能不能自然带出三类差异。

### `v5`

`v5` 是 concept-only 版本，基本只保留 Park brand concept 定义。它不是最稳的生产版本，而是一个理论操纵测试版本：如果只给模型 functional / symbolic / experiential 的概念定义，模型是否能自己形成三种图像取向。

### `v6`

`v6` 是平衡版。它在 `v5` 的基础上恢复了实验控制：

- 保持源商品身份。
- 禁止新增可读文字、价格、虚假 claims、徽章、认证等。
- 保持商品可识别。
- 保持图片自然、干净、摄影感。

`v6` 的目标是在理论纯度和输出稳定性之间折中。

### `v7`

`v7` 是 Park 定义 + `function_v2` 风格质量控制。它承认一个实践事实：只给理论定义不一定能得到足够稳定、可用、真实的成图，因此把 `function_v2` 中更强的 fidelity、artifact avoidance、verification guidance 加回来。

### `v8`

`v8` 刻意回到 Park 原始定义 + 最少质量控制。它更像一个干净的理论版本，用来减少工程化提示对三类操纵的干预。

### `v9`

`v9` 在 `v8` 的基础上选择性补回 v2 风格控制，例如产品主体清晰、不要新增文字、避免 artifact、保持产品形态和包装。这一版比 `v8` 更稳，但仍尽量不回到过度细碎的视觉清单。

### `v10`

`v10` 是 integrated research version。它把 Park 定义与后续 prompt/image generation 控制逻辑结合起来：

- grounded product facts；
- prompt-image alignment；
- artifact control；
- concept contamination avoidance；
- discriminant-validity checks。

这一版开始把“生成图要能通过操纵检验”写进 prompt，而不只是让图看起来像某种风格。

### `v11`

`v11` 进一步强化 source-image-first grounding：先观察白底图中的可见事实，再使用商品 metadata。这样做的原因是，白底图是最可靠的产品事实来源，metadata 只应辅助理解品类和购买语境，不应该覆盖源图事实。

### `v12`

`v12` 是 function_v2-quality version。它直接融合旧版 v2 的视觉方向、推理步骤和 verification discipline，但把旧版三类的语义替换为 Park 的 functional / symbolic / experiential 三定义。

如果目标是保持图像质量稳定、操纵边界清楚，`v12` 是一个重要中间版本。

### `v13`

`v13` 是 sharper-separation 版本。它继承 `v12` 的执行纪律，但更强调：

- source image first, metadata second；
- 三类之间不能互相污染；
- 如果同一张图不改主要视觉线索就能被重命名为另一类，那么生成失败；
- Product 要读成功能/问题解决，Symbolic 要读成意义/身份，Experiential 要读成感官/体验。

`docs/v13_prompt_construction.md` 是解释这一版最详细的设计文档。该文档还说明：本地 Park PDF 是扫描版，不适合直接抽取原文，因此 v13 的 Park 定义块依赖本地整理笔记和后续论文对框架的复述。

### `v14`

`v14` 是中文版本。它保留 Park 三分类的理论来源，但从现有文件看，更像 v13 的中文轻量版，而不是逐句保留所有 v13 控制条款的完整翻译。它适合快速中文运行或人工讨论，但如果需要最强操纵边界，`v13`、`v16` 或 `v17` 更完整。

### `v15`

`v15` 是中文两阶段流程：

1. `neutral_product_ad_image_prompt.v15.txt` 先根据白底图和商品 metadata 生成“商品专属中性 prompt”。这一部分明确要求不要注入 Product / Symbolic / Experiential 风格，也不要提 Park 或研究术语。
2. 三个 orientation wrapper 再把 `{neutral_product_prompt}` 注入对应的 Park 三类定义中。

设计动机是把“商品事实 grounding”和“三类风格操纵”拆开。这样可以减少一个 prompt 同时做商品理解和风格操纵时的混乱。

### `v16`

`v16` 是 `v15` 的全英文版。它保留相同两阶段逻辑：

1. 先生成 neutral product prompt。
2. 再注入 Product / Symbolic / Experiential wrapper。

当前 `v16` 的 Product 部分已经强化为多维功能展示：不只是说“展示功能”，而是要求模型选择适合该商品类别的多个 functional evidence dimensions。

### `v17`

`v17` 是当前最新思路。它与 `v15/v16` 的差别是：第一阶段不再生成中性 prompt，而是直接生成 orientation-specific prompt。

流程是：

1. `*_prompt_generator.v17.txt` 根据白底图、metadata 和目标取向，生成已经融合 Product / Symbolic / Experiential 之一的商品专属图像 prompt。
2. `*_prompt.v17.txt` 再把 `{generated_orientation_prompt}` 放入 final wrapper。
3. final wrapper 继续重复 Park 三类定义、操纵边界、真实商业摄影要求和失败规则。

这就是“双重强调”：第一阶段已经让模型围绕某一取向构思，第二阶段再次用理论定义和严格要求校准成图。

`v17` 还加入了来自 Alibaba Cloud Model Studio 文生图提示指南的工程化启发：高质量图像 prompt 应包含明确主体、具体场景、风格、镜头/光线、氛围和细节修饰，并使用真实光影、阴影、材质、反射、景深、尺度等语言来减少 AI 感、CGI 感和不真实合成感。这个指南是 prompt engineering 参考，不是学术文献。

## 三类取向的文献映射

### Product-oriented

新版 Product-oriented 对应 Park 的 functional brand concept。它强调商品与外部消费问题、实际任务、功能价值和可靠性之间的联系。

主要支撑：

- Park et al. (1986): functional brand concept。
- Keller (1993): functional benefits 与品牌联想。
- Resnik & Stern (1977), Chandy et al. (2001), Guitart & Stremersch (2021): 信息型广告诉求和购买相关信息。
- Miniard et al. (1991): product-relevant pictures。
- Houston et al. (1987), Pieters & Wedel (2004), Dang et al. (2026): 图文一致性、广告元素面积、信息呈现等横向控制。

视觉执行上，Product 不应只是白底商品图或高级 still life，而应让观众快速看到“这个商品解决什么问题 / 支持什么任务 / 有什么可见功能证据”。

### Symbolic-oriented

Symbolic-oriented 对应 Park 的 symbolic brand concept。它强调商品承载什么意义、身份、角色、群体归属、品味、自我表达或理想自我形象。

主要支撑：

- Park et al. (1986): symbolic brand concept。
- Keller (1993): symbolic benefits。
- Scott (1994), McQuarrie & Mick (1999): 广告图像作为视觉修辞和意义系统。
- Aaker (1997): brand personality。
- Holbrook & Hirschman (1982): symbolic / hedonic / esthetic aspects of consumption。
- Miniard et al. (1991): affect-laden pictures。

视觉执行上，Symbolic 可以使用光线、构图、隐喻、材质、空间、色彩和氛围，但不能让具体功能展示或使用步骤成为主导。

### Experiential-oriented

Experiential-oriented 对应 Park 的 experiential brand concept。它强调商品带来的感官愉悦、多样性、认知刺激、沉浸感、节奏、触感、味觉/嗅觉联想或消费体验。

主要支撑：

- Park et al. (1986): experiential brand concept。
- Keller (1993): experiential benefits。
- Holbrook & Hirschman (1982), Hirschman & Holbrook (1982): experiential / hedonic consumption。
- Brakus et al. (2009): brand experience。
- MacInnis & Price (1987), Elder & Krishna (2012), Escalas (2007): mental imagery、embodied simulation、self-reference。

视觉执行上，Experiential 可以包含使用场景，但主导信息必须是“接触/消费/使用这个商品是什么感觉”，而不只是“它在哪里被使用”。

## 图像生成与工程化依据

除消费者行为和品牌理论外，`v10` 以后尤其依赖生成模型控制逻辑。仓库中的 `docs/v13_prompt_construction.md` 和本地笔记把这些工程化依据归纳为：

| 工程问题             | 设计要求                                                         | 相关方法或文献传统                                                                         |
| -------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 保持源商品一致       | 不改变形状、颜色、logo、包装、材质、结构                         | DreamBooth, Textual Inversion, subject/reference consistency                               |
| 让 prompt 与图像对齐 | 先读源图事实，再用 metadata 支撑推断                             | GLIGEN, ControlNet, T2I-Adapter, Ranni 等 grounded generation / instruction-following 思路 |
| 避免虚假内容         | 不编造功能、奖项、认证、价格、标签、文字                         | prompt faithfulness, prompt-image consistency, RePrompt/OPT2I 等 prompt optimization 思路  |
| 强化三类区分度       | 每次只让一个 brand concept 成为 dominant construct               | Prompt-to-Prompt、Attend-and-Excite 等 focused semantic editing 思路                       |
| 提高真实感           | 主体、场景、镜头、光线、阴影、反射、材质、景深、尺度都要物理一致 | Alibaba Cloud text-to-image prompt guide 的工程建议；这不是学术文献                        |

上述生成模型文献和指南主要服务于“让图能稳定生成、真实可信、和 prompt 对齐”。它们不是三类广告取向的消费者理论来源。

## 当前使用建议

| 目标                                              | 建议版本         | 理由                                                                                   |
| ------------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------- |
| 需要直接运行研究条件化 alias 并对应 `v5/v8/v17` 三种控制强度 | `definition-only` / `visual-control` / `genprompt-control` | 便于论文写作、manipulation check 和版本追踪；分别对应 theory-only、minimal visual control、two-stage genprompt control |
| 需要最新、区分度最强、且尽量真实的英文生成流程    | `v17`          | 第一阶段生成取向专属 prompt，第二阶段 final wrapper 再次用 Park 定义和真实摄影要求约束 |
| 需要英文、两阶段、先中性 grounding 后注入三类风格 | `v16`          | 适合保持商品事实稳定，同时让三类操纵来自统一 wrapper                                   |
| 需要中文两阶段流程                                | `v15`          | 中文可读性强，便于人工检查中性 prompt 和三类 wrapper                                   |
| 需要稳定的单阶段英文 prompt                       | `v13`          | 已有完整设计说明，source-image-first 和 discriminant separation 都比较成熟             |
| 需要观察 Park 定义本身的操纵力                    | `v5` 或 `v8` | 控制条款少，更接近理论定义测试                                                         |
| 需要旧版 Product / Context / Symbolic 对比        | `function_v2`  | 旧版三分类中最强的执行纪律，可作为历史基线                                             |

## 相关本地文档

- `scripts/generate_images/README.md`: 运行参数、版本选择、v15/v16/v17 两阶段或取向专属流程说明。
- `docs/three_orientation_prompt_design.md`: `v4`-`v13` 的 Park 三分类逻辑、版本意图和操纵检验锚点。
- `docs/v13_prompt_construction.md`: `v13` 的详细构造说明，包括 source-image-first、discriminant validity 和生成模型控制依据。
- `docs/research_prompt_conditions_v5_v8_v17.md`: `definition-only`、`visual-control`、`genprompt-control` 三套研究条件的 evidence map 与写法说明。
- `docs/literature/广告图片类型分类_文献支撑_0514.md`: Product / Context / Affect 旧三分类与广告、品牌、消费者心理文献的对应关系。
- `docs/literature/LLM生成广告图_20篇逐篇阅读矩阵_0514.md`: 生成式广告图、视觉质量、品牌对齐、图文一致性、AI 披露等更宽的文献矩阵。

## 引用状态备注

- 真正直接写进多数新版 prompt 的核心文献只有 Park, Jaworski, and MacInnis (1986)。
- Keller (1993)、Miniard et al. (1991)、MacInnis & Price (1987)、Scott (1994)、McQuarrie & Mick (1999)、Aaker (1997)、Holbrook & Hirschman (1982) 等是设计解释和论文写作时的支撑文献，不应误写成每个 prompt 都显式引用了它们。
- Alibaba Cloud 文生图提示指南用于 `v17` 的真实摄影 prompt 工程，不是学术文献。
- 若要在论文正文或投稿材料中正式引用本文档列出的所有论文，建议再逐条核对 DOI、页码和原文表述。
