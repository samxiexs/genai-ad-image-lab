# Symbolic-oriented Advertising Image Prompt v4 中文说明

你正在为消费者广告实验生成受控刺激材料。

请把提供的白底商品图作为源商品，并保持商品身份不变，包括可见形状、颜色、材质、包装、logo 和物理结构。

商品元数据：

- 标题：{ori_title}
- 品牌：{creative_id_brand}
- 类目：{level_one_category_name}
- 价格：{creative_id_price}
- 促销：{creative_id_promotion}

Brand concept definition：
生成 Symbolic-oriented 图像，表达 symbolic brand concept。Symbolic 指商品与自我提升、角色位置、群体归属、ego-identification 或理想自我形象等内部需求相连。

Input-grounded facts：
只使用商品元数据和源图提供的事实。不要虚构未经支持的商品属性、声明、奖项、认证、用户人群或新的可读广告文字。

Concept-image linkage：
只表达定义中给出的 symbolic needs：自我提升、角色位置、群体归属、ego-identification 或理想自我形象。

Generalization discipline：
使用能够跨商品品类泛化的宽泛、品类合适的视觉线索。优先使用可辩护的 concept cues，不堆砌虚构微观场景或未经支持的受众刻板印象。
