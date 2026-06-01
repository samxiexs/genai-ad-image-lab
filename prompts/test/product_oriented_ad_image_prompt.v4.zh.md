# Product-oriented Advertising Image Prompt v4 中文说明

你正在为消费者广告实验生成受控刺激材料。

请把提供的白底商品图作为源商品，并保持商品身份不变，包括可见形状、颜色、材质、包装、logo 和物理结构。

商品元数据：

- 标题：{ori_title}
- 品牌：{creative_id_brand}
- 类目：{level_one_category_name}
- 价格：{creative_id_price}
- 促销：{creative_id_promotion}

Brand concept definition：
Brand concept 是基于消费者需求而选择的品牌意义。生成 Product-oriented 图像，表达 functional brand concept。Functional 指商品与外部产生的消费需求相连，例如解决当前问题、预防潜在问题、降低阻力或支持实践任务。

Input-grounded facts：
只使用商品元数据和源图提供的事实。不要虚构未经支持的商品属性、声明、奖项、认证、用户人群或新的可读广告文字。

Concept-image linkage：
只表达定义中给出的 functional need：外部产生的消费需求和实践问题解决。

Generalization discipline：
使用能够跨商品品类泛化的宽泛、品类合适的视觉线索。优先使用可辩护的 concept cues，不堆砌虚构微观场景。
