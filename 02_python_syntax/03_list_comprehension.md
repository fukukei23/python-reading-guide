# 3. リスト内包表記 — 短くリストを作る

## ざっくり言うと
`for` ループでリストを作る処理を、**1行で**書ける書き方です。
「リストの中に計算を詰め込む」というイメージです。

## コード例

### 例1: 基本的な使い方
```python
# 通常のfor文
numbers = []
for x in range(5):
    numbers.append(x * 2)
# numbers = [0, 2, 4, 6, 8]

# リスト内包表記（同じ結果）
numbers = [x * 2 for x in range(5)]
```

### 例2: 条件つき（ifで絞り込む）
```python
scores = [45, 80, 30, 90, 55]

# 60点以上だけを集める
passed = [s for s in scores if s >= 60]
# passed = [80, 90]
```

### 例3: 文字列のリストを加工
```python
fruits = ["apple", "banana", "cherry"]

upper_fruits = [f.upper() for f in fruits]
# upper_fruits = ["APPLE", "BANANA", "CHERRY"]
```

## 読み方ガイド

1. `[ ]` の中に書く — 結果はリストになる
2. **左側**に「各要素をどうするか」を書く
3. **真ん中**に `for 変数 in 元のリスト` を書く
4. **右側**に `if 条件` をつけると絞り込みができる

読む順序: `for` → `if` → 左側の式

## よくあるパターン

- `[x for x in list]` — そのままコピー
- `[f(x) for x in list]` — 関数を適用
- `[x for x in list if x > 0]` — 条件で絞る
- `[int(s) for s in str_list]` — 型変換

## 確認問題

**問1**: 次のリスト内包表記の結果は？
```python
result = [x + 1 for x in [1, 2, 3]]
```

**問2**: 次のコードと同じ結果になるリスト内包表記を書いてください。
```python
result = []
for word in ["cat", "dog", "bird"]:
    result.append(len(word))
```

**問3**: 次の結果は？
```python
nums = [1, 2, 3, 4, 5, 6]
even = [n for n in nums if n % 2 == 0]
```

---
→ 前: [02_fstring.md](02_fstring.md)
→ 次: [04_with_statement.md](04_with_statement.md)
