# 研究条件化 Prompt 方案：四格结构

注：这个文件名保留了历史命名，但文档内容已经按你现在确认的四格逻辑重写。

## 核心原则

当前研究条件不应再被理解成“三个并列理论条件”。更准确的结构是：

- `definition-only` 是基础理论核。
- `visual control` 是附加的 visual execution / manipulation-fidelity 组件。
- `generated prompt` 是附加的 prompt decomposition / manipulation-fidelity 组件。

因此，真正的四格条件是：

| 条件 | canonical version name | canonical alias family | 逻辑 |
| --- | --- | --- | --- |
| 基线 | `definition-only` | `def-*` | 直接使用确认好的理论定义 prompt |
| `def + vc` | `definition-control` | `dc-*` | 在确认好的 `def-*` 上追加 visual-control 段 |
| `def -> generated prompt` | `definition-genprompt` | `dg-*` | 先把 `def-*` 转成 product-specific generated prompt，再直接生图 |
| `def -> generated prompt -> vc wrapper` | `definition-control-genprompt` | `dcg-*` | 先把 `def-*` 转成 generated prompt，再嵌入 `dc-*` wrapper |

兼容版本名说明：

- `visual-control` 继续保留，但现在应当等价于 `definition-control`。
- `genprompt-control` 继续保留，但现在应当等价于 `definition-control-genprompt`。

## 现在的文件组织原则

- 研究条件的运行入口应当走 `prompts/aliases/*.txt`。
- 历史旧版 prompt 应当走 `prompts/test/*.txt`。
- 不再要求 `prompts/` 根目录保留可运行的未归档 prompt 文件。

## `definition-only`

### 定位

`definition-only` 是确认过的理论基线。它承载的是 Product-oriented / Symbolic-oriented / Experiential-oriented 三类操纵最核心的 Park 定义，不再在这个条件里混入额外 visual-control 或 wrapper-control 逻辑。

### 文件

- `prompts/aliases/def-product.txt`
- `prompts/aliases/def-symbolic.txt`
- `prompts/aliases/def-experiential.txt`

### 理论来源

这部分的直接广告理论来源仍然是：

- Park, Jaworski, and MacInnis (1986)
- 辅助写作可用 Keller (1993)、Holbrook & Hirschman (1982)、Aaker (1997) 等

但这些是广告取向理论，不是下面那些 control 段的依据。

## `definition-control`

### 定位

`definition-control` 不是新广告理论，而是：

- 保留确认过的 `def-*`
- 只追加一小段 visual-control block

也就是：在不改动基础理论定义的前提下，补上最必要的 source-product preservation、unsupported-content suppression、no-new-readable-text、realistic photographic integration、以及 orientation-specific execution cue。

### 文件

- `prompts/aliases/dc-product.txt`
- `prompts/aliases/dc-symbolic.txt`
- `prompts/aliases/dc-experiential.txt`

### 为什么这些新增段可以成立

| 新增段 | 作用 | 理论/文献性质 | 可用 CCF 文献支持 |
| --- | --- | --- | --- |
| preserve source product identity | 保持操纵只改变取向，不改变商品身份 | manipulation-fidelity control | [GLIGEN, CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Li_GLIGEN_Open-Set_Grounded_Text-to-Image_Generation_CVPR_2023_paper.html); [ControlNet, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) |
| do not invent unsupported claims/functions | 防止商品事实被模型随意虚构 | manipulation-fidelity control | GLIGEN; ControlNet |
| do not add new readable text | 避免额外 ad copy 成为操纵主体 | manipulation-fidelity / execution control | [TIFA, ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Hu_TIFA_Accurate_and_Interpretable_Text-to-Image_Faithfulness_Evaluation_with_Question_Answering_ICCV_2023_paper.html) 可支持“可解释 prompt-image faithfulness”要求；[MPS, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Learning_Multi-Dimensional_Human_Preference_for_Text-to-Image_Generation_CVPR_2024_paper.html) 可支持 semantic alignment / detail quality 维度 |
| realistic photographic integration | 降低 cutout / synthetic composite 噪声 | execution control | MPS; [Rich Human Feedback for Text-to-Image Generation, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Liang_Rich_Human_Feedback_for_Text-to-Image_Generation_CVPR_2024_paper.html) |
| orientation-specific execution cue | 让 Product / Symbolic / Experiential 的主阅读路径更稳定 | manipulation-fidelity control | TIFA; ControlNet |

### 这里最重要的写法提醒

这些段落最多只能被写成：

- visual execution control
- manipulation fidelity control
- prompt-to-image alignment control

不要把它们包装成新的广告理论。

## `definition-genprompt`

### 定位

`definition-genprompt` 的目标是单独隔离“先把理论定义改写成 product-specific generated prompt”这个组件，而不额外再套 visual-control wrapper。

也就是说它做的是：

1. 读取确认好的 `def-*`
2. 结合 source image 和 metadata，生成一个更具体的 image-generation prompt
3. 直接把这个生成结果送去生图

### 文件

- `prompts/aliases/dg-product-gen.txt`
- `prompts/aliases/dg-product.txt`
- `prompts/aliases/dg-symbolic-gen.txt`
- `prompts/aliases/dg-symbolic.txt`
- `prompts/aliases/dg-experiential-gen.txt`
- `prompts/aliases/dg-experiential.txt`

### 为什么 generator 段可以成立

| 新增段 | 作用 | 理论/文献性质 | 可用 CCF 文献支持 |
| --- | --- | --- | --- |
| “convert the confirmed def prompt into a final image-generation prompt” | 把理论定义转成 product-specific prompt | prompt rewriting / prompt optimization | [Tailored Visions, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/papers/Chen_Tailored_Visions_Enhancing_Text-to-Image_Generation_with_Personalized_Prompt_Rewriting_CVPR_2024_paper.pdf); [Dynamic Prompt Optimizing, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Mo_Dynamic_Prompt_Optimizing_for_Text-to-Image_Generation_CVPR_2024_paper.html) |
| use source image + metadata to specialize the prompt | 让生成出的 prompt grounded 在具体商品上 | manipulation-fidelity control | GLIGEN; ControlNet; [Prompt Augmentation for Self-supervised Text-guided Image Manipulation, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Bodur_Prompt_Augmentation_for_Self-supervised_Text-guided_Image_Manipulation_CVPR_2024_paper.html) |
| keep same dominant construct as base definition-only prompt | 确保生成步骤没有偷换理论操纵 | manipulation-fidelity control | TIFA |
| pass-through final prompt | 故意隔离 generated-prompt 组件本身 | engineering isolation | 这是方法设计，不是广告理论 |

### 如何在论文里写

这一格最稳的写法是：

- it isolates the prompt-generation component
- it does not introduce the additional visual-control wrapper
- it tests whether rewriting a confirmed definition-only prompt into a product-specific prompt already improves manipulability / specificity

## `definition-control-genprompt`

### 定位

`definition-control-genprompt` 是最终完整版：

1. 先从确认过的 `def-*` 生成 product-specific prompt
2. 再把这个生成结果嵌入 `dc-*` wrapper
3. 最终由 `dc-*` 里的 visual-control block 兜住 fidelity 和 contamination control

### 文件

- `prompts/aliases/dcg-product-gen.txt`
- `prompts/aliases/dcg-product.txt`
- `prompts/aliases/dcg-symbolic-gen.txt`
- `prompts/aliases/dcg-symbolic.txt`
- `prompts/aliases/dcg-experiential-gen.txt`
- `prompts/aliases/dcg-experiential.txt`

### 为什么 wrapper 段可以成立

| 新增段 | 作用 | 理论/文献性质 | 可用 CCF 文献支持 |
| --- | --- | --- | --- |
| Part 1 generated prompt injection | 把 def-based generated prompt 作为 product-specific plan | prompt decomposition | Tailored Visions; Dynamic Prompt Optimizing |
| Part 2 dc wrapper restatement | 再次强调理论定义 + visual-control constraints | manipulation-fidelity control | TIFA; MPS |
| “If Part 1 and Part 2 conflict, follow Part 2” | 显式让 fidelity control 覆盖生成漂移 | self-correction / correction layer | [Self-correcting LLM-controlled Diffusion Models, CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Self-correcting_LLM-controlled_Diffusion_Models_CVPR_2024_paper.html) |

### 这里最需要区分的口径

- 这一格不是“第三种广告理论条件”。
- 它是完整的 def-based prompt decomposition + visual-control 条件。
- 它的新增依据来自 CCF 视觉生成 / controllable generation 文献，而不是来自 Park 的广告理论本体。

## 最后一句话怎么概括

最清楚的论文方法写法应当是：

- `definition-only` = theoretical baseline
- `definition-control` = theoretical baseline + visual execution control
- `definition-genprompt` = theoretical baseline + generated prompt component
- `definition-control-genprompt` = theoretical baseline + both components

也就是：

- 三类广告取向仍然只有一套理论来源
- 你后来加的 control 段，应该老老实实写成 controllability / fidelity / execution 组件
- 不能再把 engineering control 包装成新的广告理论
