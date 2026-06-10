# 三类商品 15 样本抽样建议

这个版本不再沿用简单的 `hedonic vs utilitarian` 二分，而是改为更贴合你研究问题的三类商品结构：

1. `strict_utilitarian`
2. `experiential_hedonic`
3. `mixed_symbolic`

这样做的目的不是改名本身，而是把原来被混在一起的 `hedonic` 拆开：

- 一类是更偏感官、情绪和沉浸体验的商品
- 另一类是同时带有功能价值和身份表达价值的商品

这更适合检验三类图片生成方式：

- `functional image`
- `experiential image`
- `symbolic image`

## 推荐抽样结构

- `strict_utilitarian`: 5 个
- `experiential_hedonic`: 5 个
- `mixed_symbolic`: 5 个

总计：

- `15 products x 3 image concepts = 45 images`

## 已抽样的 15 个商品

| Group | 具体种类 | ID | 商品 | 一级类目 | 预期最匹配图片路线 | 备注 |
|---|---|---:|---|---|---|---|
| strict_utilitarian | 小家电-烧水壶 | 1552914 | 美的电热水壶 | 厨房电器 | functional | 典型任务完成型商品 |
| strict_utilitarian | 健康监测-电子血压计 | 39727 | 鱼跃电子血压计 | 医疗器械 | functional | 典型问题解决型商品 |
| strict_utilitarian | 日用消耗品-抽纸 | 1539090 | 维达抽纸 | 洗护清洁剂/卫生巾/纸/香薰 | functional | 虽然一级类目混杂，但这个具体商品很纯实用 |
| strict_utilitarian | 办公设备-打印机 | 65159 | 惠普打印机 | 办公设备/耗材/相关服务 | functional | 核心是效率和连接能力 |
| strict_utilitarian | 大家电-洗烘套装 | 497385 | 海尔洗烘套装 | 大家电 | functional | 高度依赖性能和耐用性评价 |
| experiential_hedonic | 香氛-香水 | 98323 | Tom Ford 白麝香香水 | 彩妆/香水/美妆工具 | experiential | 有一定品牌象征性，但在现有池子里仍是较好的体验型样本 |
| experiential_hedonic | 饮品-黑咖啡 | 1544271 | 雀巢深黑即溶咖啡 | 咖啡/麦片/冲饮 | experiential | 更适合表现香气、氛围和仪式感 |
| experiential_hedonic | 休闲食品-巧克力饼干 | 496173 | 好吃点巧克力味饼干 | 零食/坚果/特产 | experiential | 口感与即时愉悦感强 |
| experiential_hedonic | 花艺-永生玫瑰花束 | 1233054 | Joyflower 永生玫瑰花束 | 鲜花速递/花卉仿真/绿植园艺 | experiential | 主要依赖视觉审美和情绪唤起 |
| experiential_hedonic | 创意玩具-拼插积木 | 1235015 | 乐高迪士尼城堡 | 玩具/童车/益智/积木/模型 | experiential | 更偏创造乐趣与沉浸体验 |
| mixed_symbolic | 消费电子-智能手机 | 1562757 | Apple iPhone 16 | 手机 | symbolic | 功能强，同时身份信号也强 |
| mixed_symbolic | 可穿戴设备-智能手表 | 1562462 | 华为 WATCH GT5 | 智能设备 | symbolic | 功能与佩戴形象并存 |
| mixed_symbolic | 影像设备-Vlog相机 | 13862 | Sony ZV-E10L | 数码相机/单反相机/摄像机 | symbolic | 能被拉向功能、体验或身份表达三条路线 |
| mixed_symbolic | 穿戴-复古运动鞋 | 1561087 | Onitsuka Tiger TOKUTEN | 运动鞋new | symbolic | 公共展示性强，适合测 symbolic 图像优势 |
| mixed_symbolic | 户外装备-冲锋衣 | 1542589 | KAILAS 凯乐石冲锋衣 | 户外/登山/野营/旅行用品 | symbolic | 同时承载性能与生活方式表达 |

## 一级类目的使用原则

`level_one_category_name` 适合做第一轮初筛，但不适合直接当最终标签。因为很多一级类目内部本身就混装了不同动机的商品。

### 可以优先视作 strict utilitarian 候选

- `医疗器械`
- `OTC药品/国际医药`
- `厨房电器`
- `大家电`
- `生活电器`
- `办公设备/耗材/相关服务`
- `五金/工具`
- `家庭/个人清洁工具`
- `收纳整理`
- `网络设备/网络相关`
- `电脑硬件/显示器/电脑周边`
- `闪存卡/U盘/存储/移动硬盘`
- `文具电教/文化用品/商务用品`

这些类目里的商品大多更容易触发：

- “这个东西能帮我解决什么问题？”

### 可以优先视作 experiential hedonic 候选

- `彩妆/香水/美妆工具`
  - 仅限香水等感官主导商品，不建议把口红、美妆工具直接等同于体验型
- `咖啡/麦片/冲饮`
  - 更适合选咖啡、风味饮品，不适合选奶粉、营养粉
- `零食/坚果/特产`
- `鲜花速递/花卉仿真/绿植园艺`
  - 更适合选花束、摆件花艺，不适合选肥料、菜苗
- `玩具/童车/益智/积木/模型`
  - 更适合选乐高、创意玩具，不适合选爬行垫等偏实用婴童用品
- `茶`
  - 更适合选日常品饮和仪式感商品，不适合选强保健导向商品
- `模玩/动漫/周边/娃圈三坑/桌游`

这些类目里的理想商品更容易触发：

- “这个商品让我有什么感觉？”

### 可以优先视作 mixed_symbolic 候选

- `手机`
- `智能设备`
- `手表`
- `数码相机/单反相机/摄像机`
- `运动鞋new`
- `户外/登山/野营/旅行用品`
- `箱包皮具/热销女包/男包`
- `黄金`
- `珠宝/钻石/翡翠`
- `女鞋`
- `女装/女士精品`
- `男装`
- `服饰配件/皮带/帽子/围巾`
- `ZIPPO/瑞士军刀/眼镜`
- `美容护肤/美体/精油`
- `美容美体仪器`

这些类目里的典型商品更容易触发：

- “它能做什么”
- “它让我感觉怎样”
- “它让我看起来像谁”

也就是说，这类商品最适合比较 `functional`、`experiential`、`symbolic` 三条图片路线如何把同一个商品拉向不同意义。

## 不建议直接按一级类目机械分组的类目

- `彩妆/香水/美妆工具`
  - 香水偏体验，口红偏象征，美妆工具偏功能
- `洗护清洁剂/卫生巾/纸/香薰`
  - 纸巾偏实用，香薰偏体验
- `户外/登山/野营/旅行用品`
  - 登山杖偏实用，冲锋衣和背包更偏 mixed
- `美容护肤/美体/精油`
  - 防晒偏功能，精油偏体验，高端护肤偏 mixed
- `玩具/童车/益智/积木/模型`
  - 积木偏体验，爬行垫和婴儿用品可能更偏实用

## 最终判定规则

建议每个商品都按三个维度做人工评分：

| 维度 | 判断问题 |
|---|---|
| Functional score | 消费者是否主要看它解决什么问题？ |
| Experiential score | 消费者是否主要看它带来什么感受？ |
| Symbolic score | 消费者是否主要看它表达什么身份或生活方式？ |

然后再按下面的规则定最终标签：

| 类型 | 判定逻辑 |
|---|---|
| strict_utilitarian | Functional 高，Experiential 和 Symbolic 都低 |
| experiential_hedonic | Experiential 高，Functional 低，Symbolic 不宜过高 |
| mixed_symbolic | Symbolic 高，同时 Functional 或 Experiential 不低 |

## 这版样本相对你旧版的关键变化

- 原来的 `utilitarian` 5 个基本保留
- 原来的 `hedonic` 被拆开
- `黄金`、`包`、`婚鞋`、`连衣裙` 这类更偏展示和身份表达的商品，不再和香水放在同一类
- 新增 `手机`、`智能手表`、`相机`、`运动鞋`、`冲锋衣` 作为 mixed 核心样本

## 后续如果你要继续收紧样本

可以优先做两类微调：

1. 如果担心 `Tom Ford` 品牌过强，可以把香水换成更弱身份信号的香氛商品。
2. 如果担心 `永生花束` 带礼物属性太强，可以替换成更纯感官导向的香薰、咖啡或茶。
