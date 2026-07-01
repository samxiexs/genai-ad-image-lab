#!/usr/bin/env python3
"""Select four 120-product groups with explicit brand-salience controls.

The selection follows the revised advisor requirement:

- symbolic groups should foreground recognizable brands;
- non-symbolic groups should avoid recognizable or salient brand cues.

Outputs are deterministic CSV files under data/experiment/.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
import math
from pathlib import Path
import re
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
RAW_CATALOG = REPO_ROOT / "data/raw/white_bg_product_catalog.csv"
OLD_FOUR_GROUPS = REPO_ROOT / "data/experiment/white_bg_product_catalog_v10_four_groups_120_each_diverse.csv"
OLD_REPRESENTATIVE = REPO_ROOT / "data/experiment/white_bg_product_catalog_v10_explanation_representative_12.csv"
OUTPUT_DIR = REPO_ROOT / "data/experiment"
OUTPUT_STEM = "white_bg_product_catalog_v15_teacher_brand_rule_120_each"
TARGET_PER_GROUP = 120

BASE_COLUMNS = [
    "id",
    "material_id",
    "ori_title",
    "creative_id_image",
    "creative_id_brand",
    "creative_id_price",
    "creative_id_promotion",
    "level_one_category_name",
    "is_white_image",
]

KNOWN_BRAND_TERMS = [
    "Apple",
    "苹果",
    "Huawei",
    "华为",
    "Sony",
    "索尼",
    "Canon",
    "佳能",
    "Nikon",
    "尼康",
    "Fujifilm",
    "富士",
    "DJI",
    "大疆",
    "Lenovo",
    "联想",
    "ThinkPad",
    "Asus",
    "华硕",
    "Xiaomi",
    "小米",
    "MIUI",
    "米家",
    "Nike",
    "耐克",
    "Adidas",
    "阿迪达斯",
    "New Balance",
    "Puma",
    "彪马",
    "ASICS",
    "亚瑟士",
    "Converse",
    "匡威",
    "Vans",
    "Yamaha",
    "雅马哈",
    "Fender",
    "芬德",
    "Gibson",
    "GoPro",
    "Bose",
    "JBL",
    "Marshall",
    "Garmin",
    "佳明",
    "Dyson",
    "戴森",
    "Philips",
    "飞利浦",
    "Braun",
    "博朗",
    "TREK",
    "崔克",
    "Giant",
    "捷安特",
    "Specialized",
    "闪电",
    "Brompton",
    "Rapha",
    "CHANEL",
    "香奈儿",
    "Dior",
    "迪奥",
    "Gucci",
    "古驰",
    "Prada",
    "普拉达",
    "COACH",
    "蔻驰",
    "Armani",
    "阿玛尼",
    "YSL",
    "圣罗兰",
    "Lancome",
    "兰蔻",
    "Estee",
    "雅诗兰黛",
    "SK-II",
    "MAC",
    "Jo Malone",
    "祖玛珑",
    "BYREDO",
    "DIPTYQUE",
    "Chopard",
    "萧邦",
    "Tiffany",
    "Cartier",
    "卡地亚",
    "Chow Tai Fook",
    "周大福",
    "Chow Sang Sang",
    "周生生",
    "Chow Tai Seng",
    "周大生",
    "潮宏基",
    "老凤祥",
    "Baccarat",
    "巴卡拉",
    "Wedgwood",
    "Royal Copenhagen",
    "Georg Jensen",
    "Le Creuset",
    "Staub",
    "Zwilling",
    "双立人",
    "Rolex",
    "劳力士",
    "Omega",
    "欧米茄",
    "Breitling",
    "百年灵",
    "Ferragamo",
    "菲拉格慕",
    "LOEWE",
    "罗意威",
    "Jimmy Choo",
    "Jil Sander",
    "Christian Louboutin",
    "路铂廷",
    "De Beers",
    "戴比尔斯",
    "APM Monaco",
    "Swarovski",
    "施华洛世奇",
    "BOSS",
    "Hugo Boss",
    "Haier",
    "海尔",
    "Toshiba",
    "东芝",
    "Midea",
    "美的",
    "Gree",
    "格力",
    "Hisense",
    "海信",
    "Panasonic",
    "松下",
]

KNOWN_BRAND_RE = re.compile(
    "|".join(re.escape(term) for term in sorted(set(KNOWN_BRAND_TERMS), key=len, reverse=True)),
    re.IGNORECASE,
)
STRONG_BRAND_SIGNAL_RE = re.compile(
    "官方旗舰|旗舰店|联名|明星同款|经典款|奢|高端|高级感|轻奢|大牌|名牌|网红|国家宝藏|限量|礼物|送女友|送男友|情人节|七夕"
)
BRAND_SPLIT_RE = re.compile(r"[/\s（）()\[\]【】,，;；|｜]+")
HEDONIC_CLEANING_CATEGORY_ALLOWED_RE = re.compile(
    "香薰|香氛|香水|香味|香氛蜡烛|蜡烛|精油|沐浴|身体乳|洗发|护发|发膜|护手霜"
)
HEDONIC_AUDIO_CATEGORY_ALLOWED_RE = re.compile(
    "耳机|音箱|音响|蓝牙|唱片|麦克风|播放器|影音|音乐|K歌|投影"
)
HEDONIC_FLOWER_CATEGORY_ALLOWED_RE = re.compile(
    "鲜花|花束|花瓶|玫瑰|绿植|盆栽|多肉|仿真花|干花|插花|花艺|植物"
)
HEDONIC_TOY_CATEGORY_ALLOWED_RE = re.compile(
    "玩具|积木|模型|公仔|娃|手办|拼图|卡牌|桌游|游戏|盲盒|毛绒|动漫"
)
HEDONIC_HOME_DECOR_CATEGORY_ALLOWED_RE = re.compile(
    "摆件|装饰|花瓶|挂画|香薰|香氛|蜡烛|抱枕|地毯|灯|艺术|画|花艺"
)
HEDONIC_PET_CATEGORY_ALLOWED_RE = re.compile(
    "零食|猫粮|狗粮|罐头|冻干|饼干|玩具|猫窝|狗窝|猫抓|宠物服"
)


@dataclass(frozen=True)
class GroupConfig:
    key: str
    label_cn: str
    expected_route: str
    consumption_axis: str
    symbolic_axis: str
    brand_visibility_target: str
    categories: frozenset[str]
    require_known_brand: bool
    max_per_category: int = 8
    max_per_brand: int = 4


GROUPS = [
    GroupConfig(
        key="utilitarian_symbolic",
        label_cn="实用+symbolic",
        expected_route="symbolic",
        consumption_axis="utilitarian",
        symbolic_axis="symbolic",
        brand_visibility_target="prominent_recognizable_brand",
        categories=frozenset(
            [
                "乐器/吉他/钢琴/配件",
                "平板电脑/MID",
                "影音电器",
                "户外/登山/野营/旅行用品",
                "手机",
                "数码相机/单反相机/摄像机",
                "智能设备",
                "电脑硬件/显示器/电脑周边",
                "笔记本电脑",
                "自行车/骑行装备/零配件",
                "运动/瑜伽/健身/球迷用品",
                "3C数码配件",
                "运动鞋new",
                "电玩/配件/游戏/攻略",
                "电动车/配件/交通工具",
                "大家电",
                "厨房电器",
                "生活电器",
                "个人护理/保健/按摩器材",
            ]
        ),
        require_known_brand=True,
    ),
    GroupConfig(
        key="hedonic_symbolic",
        label_cn="享乐+symbolic",
        expected_route="symbolic",
        consumption_axis="hedonic",
        symbolic_axis="symbolic",
        brand_visibility_target="prominent_recognizable_brand",
        categories=frozenset(
            [
                "女鞋",
                "手表",
                "女装/女士精品",
                "家居饰品",
                "珠宝/钻石/翡翠",
                "箱包皮具/热销女包/男包",
                "黄金",
                "床上用品",
                "彩妆/香水/美妆工具",
                "男装",
                "餐饮具",
                "饰品/流行首饰/时尚饰品新",
                "流行男鞋",
                "女士内衣/男士内衣/家居服",
                "洗护清洁剂/卫生巾/纸/香薰",
                "美容护肤/美体/精油",
                "美容美体仪器",
                "服饰配件/皮带/帽子/围巾",
            ]
        ),
        require_known_brand=True,
    ),
    GroupConfig(
        key="strict_utilitarian_no_symbolic",
        label_cn="实用无symbolic",
        expected_route="functional",
        consumption_axis="utilitarian",
        symbolic_axis="non_symbolic",
        brand_visibility_target="deemphasize_or_hide_brand",
        categories=frozenset(
            [
                "个人护理/保健/按摩器材",
                "住宅家具",
                "办公设备/耗材/相关服务",
                "医疗器械",
                "厨房/烹饪用具",
                "厨房电器",
                "大家电",
                "婴童尿裤",
                "婴童用品",
                "家庭/个人清洁工具",
                "居家日用",
                "收纳整理",
                "文具电教/文化用品/商务用品",
                "汽车零部件/养护/美容/维保",
                "洗护清洁剂/卫生巾/纸/香薰",
                "五金/工具",
                "生活电器",
                "家装主材",
                "基础建材",
            ]
        ),
        require_known_brand=False,
    ),
    GroupConfig(
        key="hedonic_no_symbolic",
        label_cn="享乐无symbolic",
        expected_route="experiential",
        consumption_axis="hedonic",
        symbolic_axis="non_symbolic",
        brand_visibility_target="deemphasize_or_hide_brand",
        categories=frozenset(
            [
                "咖啡/麦片/冲饮",
                "家居饰品",
                "彩妆/香水/美妆工具",
                "影音电器",
                "模玩/动漫/周边/娃圈三坑/桌游",
                "水产肉类/新鲜蔬果/熟食",
                "洗护清洁剂/卫生巾/纸/香薰",
                "玩具/童车/益智/积木/模型",
                "电玩/配件/游戏/攻略",
                "美发护发/假发",
                "茶",
                "酒类",
                "零食/坚果/特产",
                "餐饮具",
                "床上用品",
                "鲜花速递/花卉仿真/绿植园艺",
                "宠物/宠物食品及用品",
                "奶粉/辅食/营养品/零食",
                "书籍/杂志/报纸",
            ]
        ),
        require_known_brand=False,
    ),
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def clean(value: str | None) -> str:
    return " ".join(str(value or "").split())


def parse_price(value: str | None) -> float:
    text = clean(value)
    match = re.search(r"\d+(?:\.\d+)?", text)
    return float(match.group(0)) if match else 0.0


def brand_tokens(brand: str) -> list[str]:
    tokens = []
    for token in BRAND_SPLIT_RE.split(clean(brand)):
        token = token.strip()
        if len(token) < 2:
            continue
        if token.startswith("#") or re.fullmatch(r"\d+", token):
            continue
        if re.search("官方|旗舰店|专营店|企业店|outlet店", token, flags=re.IGNORECASE):
            continue
        if token.lower() in {"null", "none", "nan", "官方", "官方旗舰店", "旗舰店", "无品牌"}:
            continue
        tokens.append(token)
    return tokens


def canonical_brand(brand: str) -> str:
    tokens = brand_tokens(brand)
    if not tokens:
        return "unknown"
    return tokens[0].upper()


def brand_title_match(row: dict[str, str]) -> bool:
    title = clean(row.get("ori_title")).lower()
    for token in brand_tokens(row.get("creative_id_brand", "")):
        if token.lower() in title:
            return True
    return False


def known_brand_hit(row: dict[str, str]) -> bool:
    haystack = f"{clean(row.get('creative_id_brand'))} {clean(row.get('ori_title'))}"
    return KNOWN_BRAND_RE.search(haystack) is not None


def strong_brand_signal(row: dict[str, str]) -> bool:
    haystack = f"{clean(row.get('creative_id_brand'))} {clean(row.get('ori_title'))}"
    return STRONG_BRAND_SIGNAL_RE.search(haystack) is not None


def source_membership(
    old_rows: Iterable[dict[str, str]],
    rep_rows: Iterable[dict[str, str]],
) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    old_by_id = {row["id"]: row for row in old_rows}
    rep_by_id = {row["id"]: row for row in rep_rows}
    return old_by_id, rep_by_id


def row_score(
    row: dict[str, str],
    group: GroupConfig,
    old_by_id: dict[str, dict[str, str]],
    rep_by_id: dict[str, dict[str, str]],
    brand_frequency: dict[str, int],
) -> float:
    price = parse_price(row.get("creative_id_price"))
    known = known_brand_hit(row)
    match = brand_title_match(row)
    strong = strong_brand_signal(row)
    brand_key = canonical_brand(row.get("creative_id_brand", ""))
    score = 0.0

    if group.require_known_brand:
        score += 1000 if known else -1000
        score += 120 if KNOWN_BRAND_RE.search(clean(row.get("creative_id_brand"))) else 0
        score += 80 if KNOWN_BRAND_RE.search(clean(row.get("ori_title"))) else 0
        score += 60 if match else 0
        score += min(90.0, math.log1p(max(price, 1.0)) * 12)
        score += 35 if strong else 0
        old = old_by_id.get(row["id"])
        if old and old.get("candidate_group") == group.key:
            score += 55 + parse_price(old.get("candidate_score")) * 0.5
        rep = rep_by_id.get(row["id"])
        if rep and rep.get("representative_group") == group.key:
            score += 160
    else:
        score += 800 if not known else -800
        score += 220 if not strong else -280
        score += 120 if not match else -130
        freq = brand_frequency.get(brand_key, 0)
        if brand_key == "unknown":
            score += 80
        elif freq <= 10:
            score += 80
        elif freq <= 30:
            score += 55
        elif freq <= 60:
            score += 30
        else:
            score -= 35
        score += max(0.0, 95 - math.log1p(max(price, 1.0)) * 13)
        old = old_by_id.get(row["id"])
        if old and old.get("candidate_group") == group.key and not known and not strong:
            score += 35 + parse_price(old.get("candidate_score")) * 0.15
        rep = rep_by_id.get(row["id"])
        if rep and rep.get("representative_group") == group.key and not known and not strong:
            score += 60

    return score


def eligible(row: dict[str, str], group: GroupConfig) -> bool:
    if row.get("is_white_image") != "1":
        return False
    if row.get("level_one_category_name") not in group.categories:
        return False
    if group.require_known_brand:
        return known_brand_hit(row)
    if group.key == "hedonic_no_symbolic" and not hedonic_no_symbolic_title_ok(row):
        return False
    return not known_brand_hit(row) and not strong_brand_signal(row)


def hedonic_no_symbolic_title_ok(row: dict[str, str]) -> bool:
    category = row.get("level_one_category_name", "")
    title = clean(row.get("ori_title"))
    if category == "洗护清洁剂/卫生巾/纸/香薰":
        return HEDONIC_CLEANING_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "影音电器":
        return HEDONIC_AUDIO_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "鲜花速递/花卉仿真/绿植园艺":
        return HEDONIC_FLOWER_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "玩具/童车/益智/积木/模型":
        return HEDONIC_TOY_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "模玩/动漫/周边/娃圈三坑/桌游":
        return HEDONIC_TOY_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "家居饰品":
        return HEDONIC_HOME_DECOR_CATEGORY_ALLOWED_RE.search(title) is not None
    if category == "宠物/宠物食品及用品":
        return HEDONIC_PET_CATEGORY_ALLOWED_RE.search(title) is not None
    return True


def select_group(
    rows: list[dict[str, str]],
    group: GroupConfig,
    old_by_id: dict[str, dict[str, str]],
    rep_by_id: dict[str, dict[str, str]],
    brand_frequency: dict[str, int],
    used_ids: set[str],
) -> list[dict[str, str]]:
    candidates = [
        row
        for row in rows
        if row["id"] not in used_ids and eligible(row, group)
    ]
    scored = [
        (row_score(row, group, old_by_id, rep_by_id, brand_frequency), row)
        for row in candidates
    ]
    scored.sort(
        key=lambda item: (
            -item[0],
            item[1].get("level_one_category_name", ""),
            canonical_brand(item[1].get("creative_id_brand", "")),
            item[1].get("id", ""),
        )
    )

    for category_cap in [group.max_per_category, 10, 12, 16, 25, TARGET_PER_GROUP]:
        for brand_cap in [group.max_per_brand, 6, 8, 12, TARGET_PER_GROUP]:
            selected: list[dict[str, str]] = []
            category_counts: dict[str, int] = {}
            brand_counts: dict[str, int] = {}
            for score, row in scored:
                category = row.get("level_one_category_name", "")
                brand_key = canonical_brand(row.get("creative_id_brand", ""))
                if category_counts.get(category, 0) >= category_cap:
                    continue
                if brand_counts.get(brand_key, 0) >= brand_cap:
                    continue
                selected.append(enrich_row(row, group, score, len(selected) + 1, old_by_id, rep_by_id, brand_frequency))
                category_counts[category] = category_counts.get(category, 0) + 1
                brand_counts[brand_key] = brand_counts.get(brand_key, 0) + 1
                if len(selected) == TARGET_PER_GROUP:
                    return selected
    raise RuntimeError(f"Could not select {TARGET_PER_GROUP} rows for {group.key}; eligible={len(candidates)}")


def selection_reason(row: dict[str, str], group: GroupConfig, old_by_id: dict[str, dict[str, str]], rep_by_id: dict[str, dict[str, str]]) -> str:
    category = row.get("level_one_category_name", "")
    if group.require_known_brand:
        reason = (
            f"{group.label_cn}；{category}；命中知名品牌词库，适合凸显商标/品牌识别；"
            "用于最大化 symbolic 影响。"
        )
    else:
        reason = (
            f"{group.label_cn}；{category}；排除知名品牌和强品牌/联名/礼物线索，"
            "后续生成应弱化或隐去商标。"
        )
    if row["id"] in rep_by_id:
        reason += "；来自原 representative_12。"
    elif row["id"] in old_by_id:
        reason += "；来自原 v10 四组候选表。"
    else:
        reason += "；从完整商品集补充。"
    return reason


def enrich_row(
    row: dict[str, str],
    group: GroupConfig,
    score: float,
    rank: int,
    old_by_id: dict[str, dict[str, str]],
    rep_by_id: dict[str, dict[str, str]],
    brand_frequency: dict[str, int],
) -> dict[str, str]:
    brand_key = canonical_brand(row.get("creative_id_brand", ""))
    old = old_by_id.get(row["id"])
    rep = rep_by_id.get(row["id"])
    enriched = {column: row.get(column, "") for column in BASE_COLUMNS}
    enriched.update(
        {
            "candidate_group": group.key,
            "candidate_group_cn": group.label_cn,
            "symbolic": "true" if group.symbolic_axis == "symbolic" else "false",
            "expected_best_image_route": group.expected_route,
            "consumption_axis": group.consumption_axis,
            "symbolic_axis": group.symbolic_axis,
            "brand_visibility_target": group.brand_visibility_target,
            "brand_salience_rule": "known_brand_required" if group.require_known_brand else "known_brand_excluded",
            "brand_known_hit": "1" if known_brand_hit(row) else "0",
            "brand_title_match": "1" if brand_title_match(row) else "0",
            "title_strong_brand_signal": "1" if strong_brand_signal(row) else "0",
            "canonical_brand": brand_key,
            "brand_frequency_in_full_catalog": str(brand_frequency.get(brand_key, 0)),
            "candidate_score": str(int(round(score))),
            "selection_rank_within_group": str(rank),
            "selection_reason": selection_reason(row, group, old_by_id, rep_by_id),
            "source_table": "full_catalog_v15_teacher_brand_rule",
            "source_previous_v10_group": old.get("candidate_group", "") if old else "",
            "source_previous_representative_group": rep.get("representative_group", "") if rep else "",
        }
    )
    return enriched


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def count_by(rows: list[dict[str, str]], column: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        key = row.get(column, "")
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def write_summary(path: Path, combined: list[dict[str, str]], group_paths: dict[str, Path]) -> None:
    lines = [
        "# V15 teacher brand-rule product selection",
        "",
        "This file audits the deterministic 4 x 120 product selection.",
        "",
        "Selection rule:",
        "",
        "- symbolic groups require a recognizable brand hit and favor visible brand/title matches.",
        "- non-symbolic groups exclude recognizable brands and strong brand-signaling title terms.",
        "- all groups cap category and brand concentration before relaxing caps only if needed.",
        "",
        "Outputs:",
        "",
        f"- combined: `{OUTPUT_DIR / (OUTPUT_STEM + '.csv')}`",
    ]
    for group, group_path in group_paths.items():
        lines.append(f"- {group}: `{group_path}`")
    lines.extend(["", "Group counts:", ""])
    for group in GROUPS:
        sub = [row for row in combined if row["candidate_group"] == group.key]
        known_count = sum(row["brand_known_hit"] == "1" for row in sub)
        title_match_count = sum(row["brand_title_match"] == "1" for row in sub)
        strong_count = sum(row["title_strong_brand_signal"] == "1" for row in sub)
        symbolic_counts = count_by(sub, "symbolic")
        lines.extend(
            [
                f"## {group.key}",
                "",
                f"- rows: {len(sub)}",
                f"- symbolic values: {symbolic_counts}",
                f"- known-brand hits: {known_count}",
                f"- brand-title matches: {title_match_count}",
                f"- strong title brand signals: {strong_count}",
                f"- categories: {len(count_by(sub, 'level_one_category_name'))}",
                f"- brands: {len(count_by(sub, 'canonical_brand'))}",
                "",
                "Top categories:",
                "",
            ]
        )
        for category, count in list(count_by(sub, "level_one_category_name").items())[:20]:
            lines.append(f"- {category}: {count}")
        lines.extend(["", "Top brands:", ""])
        for brand, count in list(count_by(sub, "canonical_brand").items())[:20]:
            lines.append(f"- {brand}: {count}")
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    raw_rows = read_csv(RAW_CATALOG)
    raw_rows = [row for row in raw_rows if row.get("is_white_image") == "1"]
    old_rows = read_csv(OLD_FOUR_GROUPS)
    rep_rows = read_csv(OLD_REPRESENTATIVE)
    old_by_id, rep_by_id = source_membership(old_rows, rep_rows)
    brand_frequency: dict[str, int] = {}
    for row in raw_rows:
        brand_key = canonical_brand(row.get("creative_id_brand", ""))
        brand_frequency[brand_key] = brand_frequency.get(brand_key, 0) + 1

    combined: list[dict[str, str]] = []
    group_paths: dict[str, Path] = {}
    used_ids: set[str] = set()
    output_columns = BASE_COLUMNS + [
        "candidate_group",
        "candidate_group_cn",
        "symbolic",
        "expected_best_image_route",
        "consumption_axis",
        "symbolic_axis",
        "brand_visibility_target",
        "brand_salience_rule",
        "brand_known_hit",
        "brand_title_match",
        "title_strong_brand_signal",
        "canonical_brand",
        "brand_frequency_in_full_catalog",
        "candidate_score",
        "selection_rank_within_group",
        "selection_reason",
        "source_table",
        "source_previous_v10_group",
        "source_previous_representative_group",
    ]

    for group in GROUPS:
        selected = select_group(raw_rows, group, old_by_id, rep_by_id, brand_frequency, used_ids)
        used_ids.update(row["id"] for row in selected)
        combined.extend(selected)
        group_path = OUTPUT_DIR / f"{OUTPUT_STEM}_{group.key}.csv"
        group_paths[group.key] = group_path
        write_csv(group_path, selected, output_columns)

    combined_path = OUTPUT_DIR / f"{OUTPUT_STEM}.csv"
    summary_path = OUTPUT_DIR / f"{OUTPUT_STEM}_summary.md"
    write_csv(combined_path, combined, output_columns)
    write_summary(summary_path, combined, group_paths)
    print(f"WROTE {combined_path}")
    print(f"WROTE {summary_path}")
    for group_path in group_paths.values():
        print(f"WROTE {group_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
