# Aliases 文件说明

这个文件用于解释 `prompts/aliases/` 里真正应该怎么理解四类条件。

## 先说结论

你确认无误、不能乱动的是 6 个 `def-` 文件：

- `def-product.txt/.md`
- `def-symbolic.txt/.md`
- `def-experiential.txt/.md`

其余三类都应当以这套 `def-*` 为基底来派生，而不是直接照搬旧的 v8 / v17 长 prompt。

## 四类条件的正确逻辑

1. `definition-only`
   - 对应 `def-*`
   - 这是理论基线

2. `definition-control`
   - 对应 `dc-*`
   - 做法：在确认过的 `def-*` 上追加 visual-control 段

3. `definition-genprompt`
   - 对应 `dg-*`
   - 做法：先把确认过的 `def-*` 转成 product-specific image-generation prompt，再直接拿生成出来的 prompt 去生图

4. `definition-control-genprompt`
   - 对应 `dcg-*`
   - 做法：先把确认过的 `def-*` 转成 product-specific image-generation prompt，再把这个生成结果嵌入到 `dc-*` wrapper 中

## 当前建议只把这些当 canonical

| Family | Condition | 作用 |
| --- | --- | --- |
| `def-*` | `definition-only` | 理论定义直出 |
| `dc-*` | `definition-control` | `def + visual control` |
| `dg-*` | `definition-genprompt` | `def -> generated prompt -> image` |
| `dcg-*` | `definition-control-genprompt` | `def -> generated prompt -> dc wrapper -> image` |

## 兼容项怎么理解

- `visual-control` 这个旧版本名还可以继续在脚本里用，但它现在应该等价于 `definition-control`。
- `genprompt-control` 这个旧版本名还可以继续在脚本里用，但它现在应该等价于 `definition-control-genprompt`。
- `vc-*` / `gpc-*` 这些旧 alias 文件现在只保留成兼容入口，不是建议继续扩展的 canonical family。

## 运行时最推荐的写法

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-only
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-genprompt
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt
```

如果你想手动指定某个 alias 文件，再加上对应 orientation：

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control --orientation Product-oriented --prompt-file prompts/aliases/dc-product.txt
```

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-genprompt --orientation Product-oriented --base-prompt-file prompts/aliases/dg-product-gen.txt --prompt-file prompts/aliases/dg-product.txt
```

```bash
python3 scripts/generate_images/generate_from_csv.py --prompt-version definition-control-genprompt --orientation Product-oriented --base-prompt-file prompts/aliases/dcg-product-gen.txt --prompt-file prompts/aliases/dcg-product.txt
```
