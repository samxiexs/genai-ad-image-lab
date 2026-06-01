# 研究条件化 Prompt 方案：`definition-only`、`visual-control` 与 `genprompt-control`

本文档把历史 `v5`、`v8`、`v17` 重构为三套可直接用于实验的研究条件。目标不是逐字复制历史版本，而是在保留各版本理论内核与控制强度的前提下，形成三套结构平行、命名稳定、便于 manipulation check 的运行 prompt。

## 总体映射

| 研究条件 | 历史来源 | 运行形态 | 核心作用 |
| --- | --- | --- | --- |
| `definition-only` | `v5` | 单阶段 | 让操纵主要来自 Park 三定义本身，尽量少加视觉和工程限制。 |
| `visual-control` | `v8` | 单阶段 | 在保留 Park 定义优先的前提下，加入最小但明确的视觉控制与保真要求。 |
| `genprompt-control` | `v17` | 两阶段 | 先生成 orientation-specific 商品专属 prompt，再用 final wrapper 进行第二层理论与真实感约束。 |

## `definition-only`

### 条件定位

`definition-only` 是 theory-first control。它保留三类取向最核心的 Park 定义，并只加入最基本的研究语境、source image 指向、metadata 段和失败规则。它的目标不是最大化成图稳定性，而是测试：如果主要操纵只来自 functional / symbolic / experiential brand concept 的理论定义，模型是否仍会自发生成可区分的三类广告图。

### 文件

- `prompts/product_oriented_ad_image_prompt.definition-only.txt`
- `prompts/symbolic_oriented_ad_image_prompt.definition-only.txt`
- `prompts/experiential_oriented_ad_image_prompt.definition-only.txt`

### 证据依据

| Prompt block | 作用 | 依据 |
| --- | --- | --- |
| 研究语境 + source image 指向 | 保证模型知道是在处理同一个白底商品，而不是开放式纯文生图。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401) 的 concept-image consistency 逻辑。 |
| Park brand concept 定义段 | 让 functional / symbolic / experiential 成为主操纵。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401)。 |
| “dominant message” 段 | 把品牌概念转成图像层面的第一阅读路径。 | [academic] Park 的 brand meaning 框架；[Keller (1993)](https://journals.sagepub.com/doi/10.1177/002224299305700101) 对 functional / symbolic / experiential benefits 的整理。 |
| failure rule | 让实验判定基于 dominant construct，而不是纯审美。 | [academic] Park 的三路区分；本项目 `v13` 以后形成的 discriminant validity 逻辑。 |

### 为什么这样写

- Product 版只要求观众读到 practical task / problem solving，是因为 functional concept 的核心不是“看起来专业”，而是“和外部消费问题相连”。
- Symbolic 版把“what the product expresses”写成中心句，是因为 symbolic concept 的关键在于意义承载，而不是使用功能。
- Experiential 版把“what it feels like”写成中心句，是因为 experiential concept 的最小转译单位是 felt experience，而不是一般场景出现。

## `visual-control`

### 条件定位

`visual-control` 在 `definition-only` 之上加入最小但明确的控制块。它仍然坚持 Park 定义优先，但不再完全依赖模型自行补全执行细节，而是最少限度地规定：商品身份要保持、不能新增不受支持的功能或文字、画面要有真实摄影感、取向必须可区分。

### 文件

- `prompts/product_oriented_ad_image_prompt.visual-control.txt`
- `prompts/symbolic_oriented_ad_image_prompt.visual-control.txt`
- `prompts/experiential_oriented_ad_image_prompt.visual-control.txt`

### Shared scaffold 证据图

| Shared block | 为什么需要 | 依据 |
| --- | --- | --- |
| Preserve source product identity | 三个条件应改变 brand meaning，而不是改变商品身份。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401); [DreamBooth](https://arxiv.org/abs/2208.12242); [Textual Inversion](https://arxiv.org/abs/2208.01618)。 |
| Do not invent unsupported claims or functions | 品牌概念可以变化，但商品事实不能被虚构。 | [academic] [GLIGEN](https://arxiv.org/abs/2301.07093), [ControlNet](https://arxiv.org/abs/2302.05543), [T2I-Adapter](https://arxiv.org/abs/2302.08453) 对 grounded control 的思路。 |
| Do not add new readable text | 操纵应主要活在图像概念，而不是额外 ad copy。 | [academic] controllable generation 的 prompt faithfulness 传统；[Dang et al. (2026)](https://doi.org/10.1177/00222437251373042) 对图文构成与一致性的提醒。 |
| Realistic photographic integration | 减少 cutout、CGI、synthetic composite 对操纵的污染。 | [academic] grounded / faithful generation 传统；[Li & Xie (2020)](https://doi.org/10.1177/0022243719881113) 对图像质量的营销相关性。 |
| Failure rule | 把失败定义为 concept contamination，而不是仅仅“不好看”。 | [academic] 本项目 `v13` 形成的 discriminant validity 逻辑；[Prompt-to-Prompt](https://arxiv.org/abs/2208.01626), [Attend-and-Excite](https://arxiv.org/abs/2301.13826) 所代表的 focused semantic control 思路。 |

### Orientation-specific 证据图

#### Product-oriented

| 段落 | 为什么这样写 | 依据 |
| --- | --- | --- |
| infer product type / practical task / reason to buy | 让功能价值成为第一阅读。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401); [Keller (1993)](https://journals.sagepub.com/doi/10.1177/002224299305700101)。 |
| concrete functional evidence cues | 用可见证据承载功能，而不是靠假文案。 | [academic] [Miniard et al. (1991)](https://econpapers.repec.org/RePEc:oup:jconrs:v:18:y:1991:i:1:p:92-107); [Houston et al. (1987)](https://jglobal.jst.go.jp/en/public/200902029854929496)。 |
| no lifestyle story dominance | 防止 Product 漂到 experiential 或 symbolic。 | [academic] informational vs emotional appeal 传统；Park 的 route separation。 |

#### Symbolic-oriented

| 段落 | 为什么这样写 | 依据 |
| --- | --- | --- |
| infer one symbolic meaning | 让图像先回答“这个产品意味着什么”。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401); [Keller (1993)](https://journals.sagepub.com/doi/10.1177/002224299305700101)。 |
| product as visible meaning carrier | 象征意义必须依附于商品，而不是背景独立成立。 | [academic] [Scott (1994)](https://openurl.ebsco.com/contentitem/doi%3A10.1086%2F209396); [McQuarrie & Mick (1999)](https://academic.oup.com/jcr/article/26/1/37/1916388)。 |
| restrained metaphor / atmosphere / role cues | 象征意义通常通过视觉修辞和身份线索显化。 | [academic] Scott; McQuarrie & Mick; [Aaker (1997)](https://journals.sagepub.com/doi/10.1177/002224379703400304)。 |
| avoid generic luxury shortcuts | 避免把 Symbolic 误写成千篇一律的 glamour 模板。 | [academic] symbolic meaning 不等于 luxury；品牌人格和身份表达要 category-compatible。 |

#### Experiential-oriented

| 段落 | 为什么这样写 | 依据 |
| --- | --- | --- |
| infer one plausible consumption experience | 让图像先回答“接触这个产品是什么感觉”。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401); [Brakus et al. (2009)](https://journals.sagepub.com/doi/abs/10.1509/jmkg.73.3.052)。 |
| product actively participates in the experience | 防止体验图退化成“产品摆在美景前”。 | [academic] [MacInnis & Price (1987)](https://academic.oup.com/jcr/article/13/4/473/1796774); [Elder & Krishna (2012)](https://academic.oup.com/jcr/article-pdf/38/6/988/19297006/38-6-988.pdf)。 |
| interaction over pure atmosphere | 体验必须通过行动或接触变得可读。 | [academic] MacInnis & Price; [Escalas (2007)](https://academic.oup.com/jcr/article/33/4/421/1790292); [Holbrook & Hirschman (1982)](https://colab.ws/articles/10.1086%2F208906)。 |

## `genprompt-control`

### 条件定位

`genprompt-control` 保留 `v17` 的两阶段结构，但把逻辑明确拆成两层：

1. generator 负责“先把商品事实与目标取向融合成商品专属 prompt”；
2. wrapper 负责“再用理论定义、执行边界与真实摄影要求把最终图钉死在目标 route 上”。

这套条件的核心不是多写字，而是把 grounding、route control、realism control 分成两个阶段，让每一层只做一类决定。

### 文件

- `prompts/product_oriented_ad_image_prompt_generator.genprompt-control.txt`
- `prompts/symbolic_oriented_ad_image_prompt_generator.genprompt-control.txt`
- `prompts/experiential_oriented_ad_image_prompt_generator.genprompt-control.txt`
- `prompts/product_oriented_ad_image_prompt.genprompt-control.txt`
- `prompts/symbolic_oriented_ad_image_prompt.genprompt-control.txt`
- `prompts/experiential_oriented_ad_image_prompt.genprompt-control.txt`

### 为什么 generator 与 wrapper 要分开

- generator 更适合承载“商品专属事实抽取”“类别特定 cue selection”“镜头与场景骨架选择”，因为这些内容需要先根据 source image 和 metadata 做一次定制推断。
- wrapper 更适合承载“理论 route 的 dominance 要求”“跨类污染抑制”“不得新增文字或虚假 claim”“真实摄影失败规则”，因为这些是所有商品共享的实验控制边界。

如果把两类工作写在一个 prompt 里，模型容易在“理解商品”与“执行操纵”之间相互覆盖；两阶段设计正是为了减少这个问题。

### Generator evidence map

| Generator block | 为什么放在 generator | 依据 |
| --- | --- | --- |
| inspect source image first | 商品专属事实应先从白底图中提取。 | [academic] grounded generation 传统；[GLIGEN](https://arxiv.org/abs/2301.07093), [ControlNet](https://arxiv.org/abs/2302.05543), [T2I-Adapter](https://arxiv.org/abs/2302.08453)。 |
| use metadata as supporting context | metadata 帮助判断品类、价格带和购买语境，但不应覆盖 visible facts。 | [academic] 本项目 `v11` 以后形成的 source-image-first 逻辑。 |
| choose orientation-specific display route | 每个商品需要一个具体的 functional / symbolic / experiential 执行骨架。 | [academic] Park 三定义；focused prompt control 文献如 [Prompt-to-Prompt](https://arxiv.org/abs/2208.01626), [Attend-and-Excite](https://arxiv.org/abs/2301.13826)。 |
| require high-quality prompt structure | 把 prompt 写成“主体 + 场景 + 风格 + 镜头 + 光线 + 细节”，提升后续图像一致性。 | [engineering] [Alibaba Cloud text-to-image prompt guide](https://www.alibabacloud.com/help/doc-detail/2865312.html)。 |
| realism failure-prevention terms | 在进入 image model 前先消除 cutout、plastic、uncanny 等常见失败模式。 | [engineering] Alibaba Cloud guide; [academic] faithful / grounded generation 传统。 |

### Wrapper evidence map

| Wrapper block | 为什么放在 wrapper | 依据 |
| --- | --- | --- |
| Part 1 generated prompt injection | 把商品专属 plan 作为最终图的 grounding。 | [academic] grounded composition 逻辑。 |
| Part 2 Park definition block | 第二次强调 dominant construct，避免 generator 只生成“好看 prompt”。 | [academic] [Park et al. (1986)](https://journals.sagepub.com/doi/10.1177/002224298605000401)。 |
| route-specific reasoning requirements | 明确功能证据、象征意义或 felt experience 的主导性。 | [academic] Park; [Keller (1993)](https://journals.sagepub.com/doi/10.1177/002224299305700101); 各 orientation 对应消费者研究。 |
| photographic quality requirements | 统一真实摄影标准，减少“生成器写得好但图像看起来像 AI mockup”的问题。 | [engineering] Alibaba Cloud guide；[academic] [Li & Xie (2020)](https://doi.org/10.1177/0022243719881113)。 |
| strict requirements and contamination suppression | 明确什么不能成为 dominant message。 | [academic] discriminant validity 逻辑；[Dang et al. (2026)](https://doi.org/10.1177/00222437251373042) 对图文构成和一致性的提醒。 |

### Orientation-specific 说明

- Product generator 强调多维 functional evidence，是为了避免只生成“高级静物 + 一句功能暗示”。
- Symbolic generator 强调 symbolic territory + symbolic visual device，是为了让 meaning 先被选定，再被视觉化。
- Experiential generator 强调 felt route + experiential device，是为了让体验不退化成 generic lifestyle scene。
- 三个 wrapper 都重复“不要只是把原白底图换个光”，因为两阶段流程最常见的失败就是 generator 给了新场景，但 final image 仍停留在轻微重拍。

## 使用建议

| 研究目的 | 推荐条件 |
| --- | --- |
| 想测试理论定义本身是否足以形成三类差异 | `definition-only` |
| 想保持 definition-first，同时加入最少执行控制 | `visual-control` |
| 想最大化商品 grounding、取向专属性和真实感控制 | `genprompt-control` |

## 引用口径提醒

- 本文档中的 `academic` 标签用于说明理论依据、消费者机制依据或 controllable generation 论文依据。
- 本文档中的 `engineering` 标签用于说明 prompt engineering 指南、镜头词表、negative prompt 经验和真实摄影质感约束。
- `genprompt-control` 中出现的 Alibaba Cloud 指南是工程参考，不应在论文里误写为广告理论文献。
