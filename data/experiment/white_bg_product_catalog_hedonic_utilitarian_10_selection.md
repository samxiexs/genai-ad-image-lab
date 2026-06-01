# Hedonic vs. Utilitarian 10-Product Subset

This file documents a manually curated 10-product subset from `data/raw/white_bg_product_catalog.csv` for a clean hedonic-versus-utilitarian product-type manipulation.

## Selection rules

- Total `n = 10`, with `5 hedonic + 5 utilitarian`.
- `level_one_category_name` does not repeat across the 10 selected rows.
- Preference was given to well-known brands and face-valid, typical products.
- Ambiguous categories such as smartphones were not prioritized because they can simultaneously signal strong functional and symbolic value.

## Final selected products

| Product type | ID | Brand | Product | `level_one_category_name` | Why it was selected |
|---|---:|---|---|---|---|
| Hedonic | 1233975 | 周大福传承 | 足金黄金吊坠项链 | 黄金 | Typical jewelry item; evaluation is mainly driven by symbolic, aesthetic, and gift value. |
| Hedonic | 98323 | Tom Ford/汤姆福特 | 白麝香香水 | 彩妆/香水/美妆工具 | Typical fragrance item; evaluation is mainly driven by sensory pleasure, affect, and self-expression. |
| Hedonic | 497364 | COACH/蔻驰 | 老花迷你水桶包 | 箱包皮具/热销女包/男包 | Typical fashion bag; evaluation is mainly driven by style, status signaling, and symbolic value. |
| Hedonic | 1537759 | Jimmy Choo | 闪粉尖头婚鞋单鞋 | 女鞋 | Typical aesthetic/fashion footwear; evaluation is mainly driven by appearance and occasion-based self-presentation. |
| Hedonic | 496613 | Ganni | 印花吊带蛋糕裙 | 女装/女士精品 | Typical fashion apparel item; evaluation is mainly driven by aesthetic appeal, lifestyle fit, and self-image. |
| Utilitarian | 1552914 | Midea/美的 | 电热水壶 | 厨房电器 | Typical practical household appliance; evaluation is mainly driven by safety, convenience, and task completion. |
| Utilitarian | 39727 | 鱼跃 | 电子血压计 | 医疗器械 | Typical health-monitoring device; evaluation is mainly driven by accuracy, reliability, and problem solving. |
| Utilitarian | 1539090 | Vinda/维达 | 抽纸纸巾整箱装 | 洗护清洁剂/卫生巾/纸/香薰 | Typical daily necessity; evaluation is mainly driven by necessity, usefulness, and convenience. |
| Utilitarian | 65159 | HP/惠普 | 彩色激光多功能打印机 | 办公设备/耗材/相关服务 | Typical office equipment; evaluation is mainly driven by efficiency, connectivity, and task completion. |
| Utilitarian | 497385 | Haier/海尔 | 洗烘套装滚筒洗衣机 | 大家电 | Typical major appliance; evaluation is mainly driven by cleaning performance, capacity, and durability. |

## Notes

- This subset is optimized for **face-valid product-type distinction**, not for perfect equivalence on price, gender targeting, or luxury level.
- The hedonic set intentionally leans toward fashion, adornment, and sensory/lifestyle products because they map most clearly onto the hedonic definition.
- The utilitarian set intentionally leans toward household, health, office, and necessity products because they map most clearly onto the utilitarian definition.
- If you later need an even more conservative subset, the easiest refinement is to replace any borderline fashion item with another luxury jewelry or fragrance item, or replace any borderline appliance with a more necessity-based medical or cleaning product.
