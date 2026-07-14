# CHI 2027 protocol: Theory-grounded GenAI advertising images

## Status, purpose, and non-negotiable design choices

**Status:** implementation-ready protocol for preregistration, IRB review, stimulus production, and a Chinese-language online consumer study. It is a design document, not evidence that the stated hypotheses are true.

**Research question.** When a white-background product reference is transformed by GenAI into a Product-oriented, Experiential-oriented, or Symbolic-oriented advertising image, which visual strategy is most effective for products that differ in (a) utilitarian versus hedonic orientation and (b) symbolic affordance? Through which consumer responses does this occur, and what changes when viewers learn that the image was made with generative AI?

**Design commitments.**

1. The product taxonomy is `2 product orientation (utilitarian/hedonic) x 2 symbolic affordance (low/high)`. A cell is a *set of products*, never a single product.
2. `symbolic` in the existing CSV is treated as a provisional **product-category hypothesis**. It is not a treatment and it must not determine whether a logo is visible.
3. All final stimuli are unbranded: remove brand names, logos, prices, promotions, and any readable in-image text in every condition. This prevents brand equity, existing identity associations, and price from being mistaken for symbolic affordance or visual strategy.
4. The three GenAI strategies are mutually exclusive only as **dominant readings**. They are not claims that a product has only one kind of value. The study tests whether one intended reading is made more salient than the others.
5. The target population is adult Chinese online consumers. The manuscript, preregistration, item labels, and analyses are written in English; participants receive Chinese materials. Every Chinese item below is a context-specific translation/adaptation that requires translation validation before confirmatory use.

The conceptual roots are Park, Jaworski, and MacInnis's functional/symbolic/experiential brand-concept framework [R1], Homburg et al.'s product-design dimensions [R2], and visual mental-simulation research [R6, R7]. The current v16 prompts are an implementation starting point, not the final experimental stimuli.

## 1. Stimulus universe and audit trail

### 1.1 Candidate products

`data/experiment/Experiment-Test0709.csv` currently contains 15 candidates. It is a useful starting pool: utilitarian-high-symbolic (`n=4`), utilitarian-low-symbolic (`n=3`), hedonic-high-symbolic (`n=5`), and hedonic-low-symbolic (`n=3`). The final pool must retain at least three validated exemplars per cell (12 or more total). If a current cell fails validation, replace it from the larger catalog rather than retaining an unsuitable item for balance.

The four cells are defined as follows.

| Cell | Construct definition | Required pretest pattern |
| --- | --- | --- |
| U-LS | primarily practical/problem-solving; weak identity-signalling affordance | utilitarian > hedonic; symbolic affordance low |
| U-HS | primarily practical/problem-solving; meaningful identity/role/group affordance | utilitarian > hedonic; symbolic affordance high |
| H-LS | primarily pleasure, stimulation, or enjoyment; weak identity-signalling affordance | hedonic > utilitarian; symbolic affordance low |
| H-HS | primarily pleasure/stimulation; meaningful identity/role/group affordance | hedonic > utilitarian; symbolic affordance high |

This deliberately allows U-HS and H-HS products: Bhat and Reddy found functional and symbolic positioning to be separable rather than opposite [R4].

### 1.2 Reproducible stimulus manifest

Before any outcome data are collected, create a versioned, read-only `stimulus_manifest.csv` with one row per generated image. Required fields are: `product_id`, pretest cell, source-image hash, de-branding status, orientation, complete prompt text, prompt version, model/provider/version, generation date, API parameters, output hash, candidate number, automated QC result, human-QC result, and final inclusion status. Preserve all rejected candidates and the reason for exclusion.

For each product x orientation, generate at least three candidates under a fixed image model and wrapper. Apply a blind technical QC for source-product identity, forbidden text, invented claims, and visible artifacts. In archived generation order, select the **first** candidate that passes QC; do not select on ad attitude, purchase intention, manipulation-check results, or any participant outcome. The target is exactly 36 final images: `12 products x 3 strategies x 1 image`.

All three prompt conditions must share the following controls: square format, identical source-product reference, no readable text, no invented performance claims, no price, no brand cue, and comparable product prominence. The only intentional difference is the theory-grounded visual strategy.

| Strategy | Intended dominant reading | Prompt implementation boundary | Theory |
| --- | --- | --- | --- |
| Product-oriented | What consumption problem the product helps solve and how it can be understood or used | product-centred, inspectable product/task relations; no unsupported benefit claims | functional brand concept [R1]; functionality/usability [R2] |
| Experiential-oriented | What engaging with the product may feel like | product-grounded consumption episode, close-to-user/participant-centred view; no status/identity as the dominant meaning | experiential brand concept [R1]; imagery and embodied simulation [R6, R7] |
| Symbolic-oriented | What the product communicates about a person, role, or group | product-identity relation through design/display/context; no generic luxury/status stereotype | symbolic brand concept [R1]; symbolic positioning [R4] |

### 1.3 Separate validation sample and acceptance rules

Run a Chinese online **stimulus-screening pilot** before the main experiment (`N = 180` valid adults). Every participant evaluates all 36 final images (`12 products x 3 strategies`). Present the 12 product blocks in random order; at the start of each block, show the de-branded source reference, then show its three strategy images in random order. Raters do not see strategy labels.

To keep a full-sample 36-image task feasible, use a short screening form for every image rather than the full V1--V5 battery: (S1) a forced choice of its dominant meaning -- functional product/problem information, lived use/consumption experience, or identity/role/group meaning; (S2) “This image still depicts the same product as the reference product” (1--7); and (S3) “This image looks like a coherent, plausible advertisement” (1--7). Participants may optionally flag readable added text, invented functions, or a material product mismatch. These three questions provide 108 required responses per participant, which is deliberately the upper limit for this screening pilot.

The pilot is a feasibility and manipulation-fidelity screen, not evidence that any advertising strategy improves consumer outcomes. A final image is retained only if:

- its intended route is selected by at least 50% of participants and its 95% confidence interval excludes the 33.3% chance level;
- product fidelity and visual quality each average at least 4.5/7;
- no confirmed added text, invented function, or material product mismatch is found after technical and participant-flag review; and
- within a product, the maximum difference in mean visual quality across the three strategy images is no more than 0.60 points.

If one image fails, revise the prompt only for that product/strategy, preserve the rejected image and reason in the manifest, and validate its replacement using the same short form with a fresh targeted sample (`N = 60`). Multimodal-model checks may flag obvious identity drift or text, but human ratings are the acceptance authority. Cross-model evaluation is supplementary because LLM judges are not a substitute for consumer construct validity [R20].

## 2. Construct register and bilingual survey instrument

### 2.1 Administration and scoring rules

Unless specified otherwise, participants answer on a 1--7 agreement scale (`1 = Strongly disagree / 非常不同意`; `7 = Strongly agree / 非常同意`). Within a construct, randomize item order, score only the direction specified in the construct row, average only if at least two-thirds of items are present, and report omega and a preregistered CFA. Do not delete items after seeing condition effects. Item wording is an **advertisement/product-context adaptation**, not a verbatim reproduction of a proprietary scale; it must be piloted in Chinese.

For each multi-item construct that is administered in full: test the product-classification factors in the classification pretest, image-validation factors in the validation sample, and outcome factors in Study 1; confirm when the sample permits with a held-out split. Report factor loadings, omega, AVE, and discriminant validity. For the preregistered two-item Study 1 short outcomes, report the item correlation and both item-level estimates as a robustness check. The single-item M1--M3 process indicators are not subjected to CFA or reliability claims. If an adapted multi-item scale fails the preregistered CFA, report item-level results as exploratory and do not substitute a post-hoc composite.

### Table 1. Product pretest and stimulus-validation measures

| ID / role | Construct and source basis | English participant item (adapted) | Chinese participant item | Items and scoring |
| --- | --- | --- | --- | --- |
| P1 / product classification | **Utilitarian orientation**; adapted to product category from the HED/UT framework [R3] | “This type of product is mainly useful for accomplishing practical tasks.”; “This type of product helps solve everyday consumption problems.”; “The practical performance of this type of product matters most.” | “这类产品主要用于完成实际任务。”；“这类产品有助于解决日常消费中的实际问题。”；“这类产品最重要的是其实用表现。” | 3 items; mean. Expected higher in U cells. |
| P2 / product classification | **Hedonic orientation**; HED/UT framework [R3] | “This type of product is mainly chosen for enjoyment.”; “Using this type of product can be pleasurable or stimulating.”; “The experience of this type of product matters most.” | “这类产品主要是为了获得愉悦而选择的。”；“使用这类产品能够带来愉悦或刺激。”；“这类产品最重要的是使用体验。” | 3 items; mean. Expected higher in H cells. |
| P3 / product classification | **Symbolic affordance**; symbolic positioning and personality-expression dimension [R1, R4] | “Choosing this type of product can express something about its user.”; “This type of product can be connected with a desired role, lifestyle, or group.”; “Others may infer something about a user from this type of product.”; “This type of product can help people present a desired self-image.” | “选择这类产品能够表达使用者的一些特征。”；“这类产品可以与理想的角色、生活方式或群体联系起来。”；“他人可能会从这类产品推断使用者的某些特征。”；“这类产品可以帮助人们呈现理想的自我形象。” | 4 items; mean. Expected higher in HS cells. |
| P4 / matching control | Familiarity; adapted from consumer product-presentation studies [R12] | “I am familiar with this type of product.” | “我熟悉这类产品。” | 1 item; matching check, not a primary covariate. |
| P5 / matching control | Expected price level; price is a product-evaluation cue [R11] | “I expect this type of product to be expensive.” | “我预计这类产品价格较高。” | 1 item; matching check. |
| V1 / stimulus manipulation | **Functional/Product-oriented reading**; functional concept [R1] and product diagnosticity [R11] | “This image primarily helps me understand what practical problem the product addresses.” | “这张图片主要帮助我理解该产品解决什么实际问题。” | 1 item; compare the three route means. |
| V2 / stimulus manipulation | **Experiential reading**; experiential concept [R1], imagery [R6], and sensory/behavioral experience [R13] | “This image primarily conveys what engaging with the product may feel like.” | “这张图片主要传达与该产品互动时可能是什么感受。” | 1 item; compare the three route means. |
| V3 / stimulus manipulation | **Symbolic reading**; symbolic concept [R1, R4] | “This image primarily conveys what the product says about a person, role, or group.” | “这张图片主要传达该产品体现了某个人、角色或群体的什么特征。” | 1 item; compare the three route means. |
| V4 / stimulus quality | Product fidelity; grounded generation evaluation [R20, R21] | “The advertised product appears to be the same product as the reference product.”; “The image preserves the product’s recognizable design.” | “广告中的产品看起来与参考产品是同一产品。”；“该图片保留了产品可识别的设计特征。” | 2 items; mean; eligibility only. |
| V5 / stimulus quality | Perceived visual quality, adapted from human-preference dimensions for text-to-image generation [R21] | “The image is visually coherent.”; “The image looks like a plausible advertisement.” | “该图片在视觉上是连贯的。”；“该图片看起来像一则可信的广告。” | 2 items; mean; balance check, not an outcome. |

### Table 2. Main-study outcomes, mechanisms, and controls

| ID / role | Construct and source basis | English participant item (adapted) | Chinese participant item | Items and scoring |
| --- | --- | --- | --- | --- |
| Y1 / co-primary outcome | **Attitude toward the advertisement (Aad)** [R8, R9] | “Overall, I have a favorable opinion of this advertisement.”; “I find this advertisement appealing.”; “I react positively to this advertisement.” | “总体而言，我对这则广告持正面看法。”；“我觉得这则广告有吸引力。”；“我对这则广告的反应是积极的。” | Item bank has 3 items. Study 1 nine-image short form uses the first 2, mean; pilot the two-item correlation. Co-primary; Holm-adjust with Y2. |
| Y2 / co-primary outcome | **Purchase consideration**; purchase-intention framework [R10] | “I would consider this product if I needed this type of product.”; “I would be willing to learn more before deciding whether to buy it.”; “This advertisement makes me more likely to consider purchasing the product.” | “如果我需要这类产品，我会考虑它。”；“在决定是否购买前，我愿意进一步了解它。”；“这则广告提高了我考虑购买该产品的可能性。” | Item bank has 3 items. Study 1 nine-image short form uses items 1 and 3, mean; pilot the two-item correlation. Co-primary; Holm-adjust with Y1. |
| M1 / proposed Product route | **Perceived diagnosticity**; consumer product evaluation [R11, R12] | “This image gives me useful information for evaluating the product.”; “This image helps me understand how the product could be used.”; “This image helps me judge whether the product would suit my needs.” | “这张图片为我评估该产品提供了有用信息。”；“这张图片帮助我理解该产品可能如何使用。”；“这张图片帮助我判断该产品是否适合我的需要。” | Item bank has 3 items. Study 1 nine-image short form uses item 1 only as a process indicator; no scale reliability or causal-mediation claim. |
| M2 / proposed Experiential route | **Mental simulation / anticipated experience**; imagery, visual-depiction, and brand-experience research [R6, R7, R13] | “While viewing the image, I could imagine myself using or consuming the product.”; “The image made the product-use experience easy to picture.”; “The image gave me a concrete sense of what engagement with the product could feel like.” | “观看图片时，我能想象自己在使用或消费该产品。”；“这张图片让我很容易想象产品的使用体验。”；“这张图片让我具体感到与该产品互动可能是什么体验。” | Item bank has 3 items. Study 1 nine-image short form uses item 1 only as a process indicator; no scale reliability or causal-mediation claim. |
| M3 / proposed Symbolic route | **Product--self connection**; self-brand connection and symbolic consumption [R4, R5] | “This product could fit the kind of person I want to be.”; “Using this product could help express something meaningful about me.”; “I can see a connection between this product and a desired identity, role, or group.” | “该产品可能契合我想成为的那类人。”；“使用该产品可能有助于表达对我有意义的某些特征。”；“我能看到该产品与理想身份、角色或群体之间的联系。” | Item bank has 3 items. Study 1 nine-image short form uses item 3 only as a process indicator; no scale reliability or causal-mediation claim. |
| C1 / manipulation check | Dominant route reading | “Which aspect did this image emphasize most?” Response options: “what practical problem the product addresses”; “what using or consuming it may feel like”; “what it says about a person, role, or group.” | “这张图片最突出的是哪一方面？”选项：“产品解决什么实际问题”；“使用或消费它可能是什么感受”；“它体现某个人、角色或群体的什么特征”。 | One forced-choice item after each image. Validation study retains V1--V3 route ratings; Study 1 uses this low-burden check. |
| C2 / provenance inference | **Inferred AI authorship**; source-inference item adapted from AI-mediated-content evaluation [R18] | “Before being told anything about its origin, how likely did you think this image was made with generative AI?” | “在获知来源之前，您认为这张图片由生成式 AI 制作的可能性有多大？” | 1 = Very unlikely / 极不可能 to 7 = Very likely / 极有可能. Exploratory outcome. |
| C3 / control | Category familiarity; product-presentation research treats prior familiarity as a relevant boundary/control [R12] | “Before this study, how familiar were you with this type of product?” | “在参加本研究前，您对这类产品有多熟悉？” | 1 = Not at all / 完全不熟悉 to 7 = Extremely / 非常熟悉. Descriptive and sensitivity covariate only. |
| C4 / control | General attitude to AI; short Chinese adaptation of the positive and negative GAAIS dimensions [R15] | **Positive:** “AI can bring important benefits to society.”; “I would be comfortable using AI in everyday life.”; “AI can improve the quality of services people receive.” **Negative:** “I feel uneasy about AI becoming widespread.”; “AI creates risks that outweigh its benefits.”; “I tend to distrust AI-supported decisions.” | **正向：**“AI 能为社会带来重要益处。”；“我愿意在日常生活中使用 AI。”；“AI 能改善人们获得服务的质量。” **负向：**“AI 的广泛使用让我感到不安。”；“AI 带来的风险大于其益处。”；“我倾向于不信任 AI 辅助的决策。” | 3 positive + 3 negative items; two separate means, no reverse-coded grand mean. Sensitivity controls only; test the two-factor CFA in Chinese. |
| D1 / Study 2 outcome | **Trust in the advertisement**; advertising-pretesting trust/credibility tradition [R9, R16] | “I regard this advertisement as trustworthy.”; “I consider the information conveyed by this advertisement credible.”; “I would rely on this advertisement when forming an initial impression of the product.” | “我认为这则广告值得信赖。”；“我认为这则广告传达的信息可信。”；“在形成对该产品的初步印象时，我愿意参考这则广告。” | Item bank has 3 items. Study 2 uses items 1--2, mean, before and after the disclosure/control message; pilot their correlation and report item-level robustness. |
| D2 / Study 2 outcome | **Perceived authenticity of the advertisement**; adapted from brand-authenticity research and GenAI-brand evidence [R17, R19] | “This advertisement feels genuine rather than fabricated.”; “The way this product is presented feels authentic.”; “This advertisement seems true to a plausible product-use context.” | “这则广告给人的感觉是真实的，而非拼凑出来的。”；“该产品的呈现方式让我觉得可信真实。”；“这则广告与合理的产品使用情境相符。” | Item bank has 3 items. Study 2 uses items 1--2, mean, before and after; pilot their correlation and report item-level robustness. |
| D3 / Study 2 process | **Attitudinal persuasion knowledge**; persuasion-knowledge model [R14] | “The way this advertisement was made seems appropriate.”; “The production method behind this advertisement seems fair to viewers.”; “Knowing how this advertisement was made changes how critically I evaluate it.” | “这则广告的制作方式是恰当的。”；“这则广告背后的制作方式对观看者是公平的。”；“了解广告的制作方式会改变我对它进行批判性评价的程度。” | 3 items; report separately; the third is not reverse-coded. Mechanism-exploratory. |
| D4 / disclosure manipulation check | Disclosure recall; provenance-disclosure studies [R16, R18] | “What did the message say about how the image was made?” | “提示信息如何说明该图片的制作方式？” | Multiple choice: generative AI / no source information / human photographer / do not remember. Exclude only from a preregistered per-protocol sensitivity analysis, not the ITT primary analysis. |

## 3. Translation, adaptation, and measurement validation

The English adaptations are first drafted by a bilingual researcher familiar with consumer research. A second bilingual translator independently produces Chinese; a third translator, blind to the English wording, back-translates Chinese into English. A reconciliation panel records disagreements and keeps a translation log. This follows the translation/back-translation principle in Brislin [R22].

Run 20--30 cognitive interviews with Chinese target participants before the validation study. Ask what each item means, whether “symbolic,” “authentic,” and “generative AI” are understood, and whether any wording sounds like a demand cue. Revise only for comprehension, document all revisions, then freeze wording before collecting confirmatory validation or outcome data.

For the Chinese implementation, do not claim that any adapted measure is a validated Chinese version merely because the English original is validated. Report: translation procedure, pilot reliability, CFA, measurement invariance only if a cross-language comparison is actually run, and all deviations from the proposed item set.

## 4. Study 0: product classification and stimulus validation

### 4.1 Product-classification pretest

**Question.** Do the selected products instantiate the intended four product cells independently of brand, price, and the research team's intuition?

**Sample and allocation.** Recruit `N = 480` valid Chinese adults from a quality-controlled online panel. Use a balanced incomplete-block assignment: each participant rates five of the 15 candidates, yielding approximately 160 ratings per candidate. Require age 18+, Chinese fluency, and no prior participation in any study in this project.

**Procedure.** Show a de-branded product reference and neutral category description. Do not show an ad image. Participants complete P1--P5. Randomize candidate order and scale order.

**Cell-selection rule.** Select at least three products per cell using preregistered contrasts: intended orientation must exceed the other orientation by at least 0.75 points and standardized `d >= .60`; high- versus low-symbolic cells must differ by `d >= .80` on P3. Within each intended cell, products should not show an extreme outlier in familiarity or expected price. These are eligibility targets, not null-hypothesis tests; report every candidate's means and selection status.

### 4.2 Image-validation study

Use the process in Section 1.3. Every participant evaluates all 36 images using the short S1--S3 screening form; a source reference is shown at the beginning of each three-image product block and no strategy label is shown. Retain image-level ratings, the fixed candidate-selection rule, and all rejected images as an artifact.

## 5. Study 1: visual-strategy × product-attribute fit

### 5.1 Research questions and predictions

- **H1 (functional fit):** the Product-oriented advantage over the mean of the other strategies increases for utilitarian versus hedonic products and is expected to coincide with higher perceived diagnosticity (M1).
- **H2 (experiential fit):** the Experiential-oriented advantage increases for hedonic versus utilitarian products and is expected to coincide with higher mental simulation (M2).
- **H3 (symbolic fit):** the Symbolic-oriented advantage increases for high- versus low-symbolic-affordance products and is expected to coincide with higher product--self connection (M3).
- **H4 (integrated fit):** the `strategy x utilitarian/hedonic x symbolic-affordance` interaction is confirmatory but directional simple-effect rankings that are not implied by H1--H3 are exploratory. This avoids pretending that a U-HS or H-HS product has one theoretically mandatory image.
- **RQ1:** Does strategy influence inferred AI authorship before provenance is disclosed?

The three strategy effects are tested on the same two co-primary outcomes (Y1, Y2), with Holm adjustment over those outcomes. M1--M3 are prespecified mechanism measures, not additional primary endpoints.

### 5.2 Experimental design and sample

Study 1 uses a mixed `3 strategy (within participant) x 3 product exemplars (within participant) x 2 utilitarian/hedonic (between participant) x 2 symbolic affordance (between participant)` design. Each participant is randomly assigned to one product-attribute cell, then evaluates all three product exemplars retained in that cell. For each exemplar, the participant sees its Product-oriented, Experiential-oriented, and Symbolic-oriented image, for nine image evaluations in total. Thus, strategy and concrete-product comparisons are both made within person, whereas product type remains a between-participant attribute.

| Assignment | Valid participants | What each participant does |
| --- | ---: | --- |
| U-LS product cell | 60 | evaluates `3 products x 3 strategies = 9` images |
| U-HS product cell | 60 | evaluates `3 products x 3 strategies = 9` images |
| H-LS product cell | 60 | evaluates `3 products x 3 strategies = 9` images |
| H-HS product cell | 60 | evaluates `3 products x 3 strategies = 9` images |
| **Study 1 total** | **240** | **nine image evaluations per participant** |

The provisional 240-person target yields 60 independent ratings for every `concrete product x strategy` image and 180 image-level ratings for every `product type x strategy` combination (three products x 60 participants). The nine image ratings within a participant are correlated and must never be treated as nine independent people. This reduction is justified by fully crossing the three exemplars and three strategies within each participant; it is not a substitute for power analysis. Before recruitment, confirm the final number by simulation using the actual twelve products, pilot-estimated repeated-measure correlations, alpha `.05`, the smallest H1--H3 strategy-by-product-attribute contrast, and anticipated exclusions. The target is acceptable only if that simulation reaches the preregistered power criterion (recommended: 80% for this resource-constrained main study); otherwise increase the per-cell sample. Product exemplars remain a sampled source of variation, so simulation and mixed modelling remain necessary [R23]. The raw white-background source-image baseline is omitted from the core study; if it is later needed, run it as a separate calibration study rather than adding a fourth repeated exposure here.

### 5.3 Procedure

1. Consent; age, language, duplicate-participation, and display-size eligibility checks.
2. Randomly assign the participant to one product cell. The participant sees all three preselected exemplars in that cell and all three strategies for each exemplar (`3 x 3 = 9` trials).
3. Use a pre-generated constrained randomisation list: no two trials from the same source product are adjacent; product and strategy positions are approximately balanced over the nine positions within each cell; and no Product/Experiential/Symbolic labels are shown. Images are never displayed side by side. Require at least 6 seconds per image; participants may inspect it longer.
4. Immediately after each image, collect the Study 1 short form: two Y1 items, two Y2 items, one preselected indicator each for M1/M2/M3, one forced-choice C1 dominant-route item, and C2. Do not mention AI before these image-level measures.
5. After all nine images, collect product familiarity for each of the three exemplars (C3), C4, one instructed-response attention check, demographics, and a non-leading open response asking what the participant thought the study was examining. The response is coded blind to condition as a diagnostic of hypothesis guessing; it is not an exclusion rule.
6. Debrief truthfully that all nine images were generated with AI from de-branded product references and were designed to emphasize different visual meanings.

### 5.4 Exclusions and integrity

The intention-to-treat (ITT) sample excludes only: consent withdrawal; duplicate platform ID/device fingerprint; ineligible age/language response; failed instructed-response attention check; technically incomplete image delivery; or completion faster than one-third of the pilot median. Do not exclude based on condition, outcome level, inferred AI authorship, product liking, or failure to guess the study hypothesis. Run a preregistered sensitivity analysis including all non-duplicate completed responses.

### 5.5 Analysis

Fit confirmatory mixed models separately for Y1 and Y2 using effect coding:

```text
Y ~ strategy * product_orientation * symbolic_affordance
    + presentation_position
    + (1 | participant) + (1 | product_exemplar)
```

`strategy` and `product_exemplar` are within-participant factors; `product_orientation` and `symbolic_affordance` are Study 0 product-cell attributes. `presentation_position` controls the first through ninth exposure. Include no post-treatment process indicator as a covariate in the primary-outcome model. Use planned contrasts for H1--H3; report coefficients, 95% CIs, standardized effect sizes, cell means, and all interaction estimates. Pre-register exploratory `strategy x presentation_position` tests as diagnostics for order, fatigue, or emerging hypothesis-guessing effects. Because there is one generated image per product x strategy, inference is to this preregistered stimulus set and prompt pipeline; it does not estimate variance across alternative renderings of the same prompt.

M1--M3 are single-item, theory-grounded process indicators in the nine-image version. Estimate preregistered multilevel strategy differences and report their association with Y1/Y2 as **mechanism-consistent process evidence**, not causal mediation and not psychometrically validated multi-item scales. Sensitivity models add product familiarity and general AI attitude; their inclusion does not replace the primary model.

## 6. Study 2: causal effect of AI disclosure after image exposure

### 6.1 Why a post-exposure randomized disclosure design

Khatiwada et al.'s CHI news study first measured content evaluations without source disclosure, then elicited reflections after LLM disclosure [R18]. That ordering is useful because early labels can alter initial content judgments. However, a simple pre/post comparison cannot distinguish disclosure from repetition or reflection. Study 2 therefore adds a randomized, equal-time reflection control.

### 6.2 Design and sample

Use the validated GenAI images only in a mixed `3 strategy (within participant) x 3 product exemplars (within participant) x 2 product orientation (between participant) x 2 symbolic affordance (between participant) x 2 post-exposure message (between participant)` design. `Time` (before versus after disclosure/reflection) is also within participant. Each participant completes both measurement phases for the same `3 products x 3 strategies = 9` images from one product-type cell.

| Assignment | Valid participants | What each participant does |
| --- | ---: | --- |
| U-LS x AI disclosure | 30 | completes pre/post D1/D2 ratings for all 9 images in the cell |
| U-LS x neutral reflection | 30 | completes two D1/D2 rounds for all 9 images in the cell |
| U-HS x AI disclosure | 30 | completes pre/post D1/D2 ratings for all 9 images in the cell |
| U-HS x neutral reflection | 30 | completes two D1/D2 rounds for all 9 images in the cell |
| H-LS x AI disclosure | 30 | completes pre/post D1/D2 ratings for all 9 images in the cell |
| H-LS x neutral reflection | 30 | completes two D1/D2 rounds for all 9 images in the cell |
| H-HS x AI disclosure | 30 | completes pre/post D1/D2 ratings for all 9 images in the cell |
| H-HS x neutral reflection | 30 | completes two D1/D2 rounds for all 9 images in the cell |
| **Study 2 total** |  | **240** |

At the provisional `N=240`, every `product type x post-exposure message` cell has 30 independent participants; every concrete `product x strategy` image within that cell has 30 paired pre/post ratings in each message condition. The primary disclosure test pools over product cells and tests `time x disclosure` and `time x disclosure x strategy`, exploiting each participant's within-person comparison across the three strategies. `Time x disclosure x strategy x product-attribute` moderation is exploratory. As in Study 1, confirm the final number by simulation using the pilot's repeated-measure correlation, disclosure effect size, and anticipated exclusions. Increase the per-cell sample if either the primary `time x disclosure` or strategy-moderation test fails to reach preregistered 80% power.

### 6.3 Exact messages

After the pre-message measures, randomly assign one message. Both screens have the same layout, minimum reading time, and a “continue” action.

**AI-disclosure message**

> **English:** The nine advertisement images you just evaluated were created with a generative-AI system from de-branded product reference images and research-defined visual instructions. They are research stimuli, not commercial product claims.
>
> **Chinese:** 您刚才评价的九张广告图片均由生成式 AI 系统基于去品牌化的产品参考图和研究定义的视觉指令生成。它们是研究材料，并不构成商业产品承诺。

**Equal-time neutral-reflection control**

> **English:** Please take a moment to look again at the advertisement images you just evaluated. The next questions ask for your current impressions of them.
>
> **Chinese:** 请花一点时间再次查看您刚才评价的广告图片。接下来的问题将询问您目前对它们的印象。

All participants are truthfully told in the debrief that the GenAI images were made with generative AI. The control does not receive a false human-authorship claim.

### 6.4 Procedure and outcomes

1. Complete consent and eligibility checks as in Study 1. Randomly assign a participant to one product-type cell; the participant evaluates all `3 products x 3 strategies = 9` images in that cell.
2. **Pre-message phase:** present the nine images one at a time in the same constrained-randomisation manner as Study 1. After each image, collect the preregistered two-item short forms of D1/D2 and C2. Do not mention AI.
3. Randomize the AI disclosure or equal-time neutral reflection once, after the first nine-image evaluation and before the second.
4. **Post-message phase:** present the same nine images again using a different constrained randomisation order. After each, recollect the two-item D1/D2 short forms. Do not recollect Y1/Y2, because repeated purchase questions may themselves prompt deliberation; if retained, they are preregistered exploratory single-item outcomes only.
5. Collect D3/D4, C3 familiarity for the three product exemplars, C4, attention, demographics, then disclose the truth.

The primary Study 2 outcomes are changes in D1 (advertisement trust) and D2 (perceived authenticity). To make 18 image exposures feasible, Study 2 uses preregistered two-item D1/D2 short forms; it does not claim these are the full three-item scales and does not treat repeated Y1/Y2 as confirmatory outcomes.

### 6.5 Analysis

Use a mixed model for each primary outcome:

```text
Y ~ time * disclosure * strategy
    + product_orientation + symbolic_affordance + phase_position
    + (1 | participant) + (1 | product_exemplar)
```

`time x disclosure` estimates the causal effect of being told the image is AI-generated above and beyond revisiting it. `time x disclosure x strategy` tests whether that effect differs for Product-, Experiential-, and Symbolic-oriented images. `phase_position` controls the first through ninth image in each phase; the second phase uses an independent constrained order. Report pre-message balance, difference-in-differences estimates, 95% CIs, and Holm-adjusted tests across D1/D2. D3 is exploratory process evidence; it is not conditioned on in the primary outcome model.

## 7. Preregistration, data quality, and ethics

Preregister Study 0 selection rules, all fixed effects/contrasts, primary outcomes, sample-size simulation, exclusion rules, treatment messages, and the distinction between confirmatory and exploratory analyses before viewing outcome data. Time-stamp prompts, manifests, surveys, and analysis scripts.

Obtain institutional ethics approval before recruitment. Consent must state that participants will see advertising-like research images, may encounter AI-generated materials, may withdraw without penalty, and that no purchase is required. Avoid categories involving health, financial risk, children, alcohol, or luxury/status stereotypes unless separately approved. No participant should be told that an AI image is human-made. Compensate at or above the panel's local fair-pay guidance.

Release, subject to image and retail-source rights: de-branded source images where permitted, full prompt text, output hashes, selection rubric, stimulus manifest, survey instrument, anonymized data, preregistration, and analysis code. If source images cannot be redistributed, release their hashes and a reproducible description of the rights restriction.

## 8. Traceability matrix

| Element | Operationalization in this protocol | Evidence basis |
| --- | --- | --- |
| Three visual strategies | Dominant functional, experiential, or symbolic reading of an otherwise controlled product image | Park et al. [R1]; Homburg et al. [R2] |
| Utilitarian/hedonic product classification | P1/P2 product-category pretest, not researcher labels | Voss et al. [R3] |
| Symbolic affordance | P3 identity/role/group/presentation pretest | Park et al. [R1]; Bhat & Reddy [R4] |
| Experiential visual route | Participant-centred, product-grounded consumption depiction; M2 | MacInnis & Price [R6]; Elder & Krishna [R7] |
| Symbolic mechanism | M3 product--self connection | Escalas [R5] |
| Main ad outcomes | Y1 Aad and Y2 purchase consideration | MacKenzie et al. [R8]; Spears & Singh [R10] |
| AI provenance | initial uninformed source inference, then truthful disclosure versus equal-time reflection | Khatiwada et al. [R18]; Koning & Voorveld [R16] |
| Trust/authenticity after disclosure | D1/D2 repeated outcomes | MacKenzie & Lutz [R9]; Morhart et al. [R17]; Brüns & Meißner [R19] |
| Stimulus sampling and power | multiple product exemplars; within-participant strategy comparison; mixed model and simulation | Westfall et al. [R23] |
| Translation | bilingual adaptation, back-translation, cognitive interviews, CFA | Brislin [R22] |

## References

**Peer-reviewed theoretical, measurement, and design sources**

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
- **[R19]** Brüns, J. D., & Meißner, M. (2024). Do you create your content yourself? Using generative artificial intelligence for social media content creation diminishes perceived brand authenticity. *Journal of Retailing and Consumer Services, 79*, 103790. https://doi.org/10.1016/j.jretconser.2024.103790
- **[R20]** Liu, V., & Chilton, L. B. (2022). Design guidelines for prompt engineering text-to-image generative models. In *Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3491102.3501825
- **[R21]** Hu, Y., Liu, B., Kasai, J., Wang, Y., Ostendorf, M., Krishna, R., & Smith, N. A. (2023). TIFA: Accurate and interpretable text-to-image faithfulness evaluation with question answering. In *Proceedings of ICCV 2023*, 20406--20417. https://doi.org/10.1109/ICCV51070.2023.01875
- **[R22]** Brislin, R. W. (1970). Back-translation for cross-cultural research. *Journal of Cross-Cultural Psychology, 1*(3), 185--216. https://doi.org/10.1177/135910457000100301
- **[R23]** Westfall, J., Kenny, D. A., & Judd, C. M. (2014). Statistical power and optimal design in experiments in which samples of participants respond to samples of stimuli. *Journal of Experimental Psychology: General, 143*(5), 2020--2045. https://doi.org/10.1037/xge0000014

**Supplied study used as a methodological analogue**

- **[R18]** Khatiwada, P., Pappu, V., Bagozzi, B. E., & Mauriello, M. L. (2026). *When AI rewrites the news: How sentiment, framing, and LLM disclosure shape perceptions*. In *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. Supplied project PDF: [`local_only/When AI Rewrites the News How Sentiment, Framing, and LLM Disclosure Shape Perceptions.pdf`](../local_only/When%20AI%20Rewrites%20the%20News%20How%20Sentiment%2C%20Framing%2C%20and%20LLM%20Disclosure%20Shape%20Perceptions.pdf).

### Evidence-status note

All core construct and scale sources above are peer-reviewed publications. R20--R21 are peer-reviewed computational/HCI sources used only for stimulus-generation and fidelity-evaluation practice, not as the sole basis for consumer constructs. No arXiv-only paper is used as the sole authority for a primary outcome, mediator, or manipulation check. DOI links were verified against publisher or index records while this protocol was prepared; investigators should recheck access and citation metadata at submission time.
