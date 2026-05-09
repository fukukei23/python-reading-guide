# 6. リスト（list / array）

## ざっくり言うと
リストは「順番のある箱の並び」です。買い物リストのように、複数のデータを1つのまとまりとして扱えます。

## コード例

### 例1：基本的なリスト
```python
colors = ["赤", "青", "緑"]
print(colors[0])
print(len(colors))
```

### 例2：要素の追加と削除
```python
cart = []
cart.append("ノートPC")
cart.append("マウス")
cart.remove("マウス")
```

### 例3：実務例（注文データ）
```python
# NexusCore 風
order_ids = ["ORD001", "ORD002", "ORD003"]

for order_id in order_ids:
    print("処理中: " + order_id)

print("全" + str(len(order_ids)) + "件の注文を処理しました")
```

## 読み方ガイド

| 行 | 読み方 |
|---|---|
| `colors = ["赤", "青", "緑"]` | 3つの文字を並べたリストを作る |
| `colors[0]` | 1番目の要素（"赤"）を取り出す |
| `len(colors)` | リストの長さ（要素数）を返す |
| `cart.append("ノートPC")` | cart の末尾に要素を追加する |
| `cart.remove("マウス")` | cart から "マウス" を削除する |

- 番号は **0から** 始まる（1番目 = [0]、2番目 = [1]）
- `[ ]`（角カッコ）で囲む
- `len()` で長さを調べる

## よくあるパターン

**パターン1：スライス（一部を取り出す）**
```python
products = ["A", "B", "C", "D", "E"]
top3 = products[0:3]    # ["A", "B", "C"]
```

**パターン2：リストの中身を確認**
```python
# atelier-kyo-manager 風
available_dates = ["4/1", "4/3", "4/5"]

if "4/3" in available_dates:
    print("4/3は予約可能です")
```

**パターン3：リストを組み立てる**
```python
# reserve-optimizer 風
results = []
for score in [80, 55, 90]:
    if score >= 60:
        results.append(score)

print(results)    # [80, 90]
```

## 確認問題

**問1** 以下のコードで `x` に入る値は何ですか？
```python
animals = ["犬", "猫", "鳥", "魚"]
x = animals[2]
```

**問2** 以下のコードを実行した後、`cart` の中身はどうなりますか？
```python
cart = ["りんご", "バナナ"]
cart.append("みかん")
cart.remove("バナナ")
```

**問3** 以下のコードは何を表示しますか？
```python
numbers = [10, 20, 30, 40]
print(len(numbers))
print(numbers[1])
```

---
→ 次: [07. 辞書（dictionary）](07_dictionaries.md)
