# 18. 演算子（==, !=, and, or, in等）

## ざっくり言うと
値を比べたり、条件を組み合わせたりする記号のことです。「AとBは同じか？」「AまたはB」といった条件を書くときに使います。

## コード例

### 例1：ECサイトの割引判定
```python
def get_discount(member_level, purchase_amount):
    if member_level == "gold" and purchase_amount >= 5000:
        return 0.10    # 10%割引
    elif member_level == "silver" or purchase_amount >= 10000:
        return 0.05    # 5%割引
    else:
        return 0.0     # 割引なし

print(get_discount("gold", 6000))    # 0.1
print(get_discount("bronze", 12000)) # 0.05
```

### 例2：在庫フィルター
```python
products = [
    {"name": "りんご", "stock": 5, "category": "果物"},
    {"name": "牛乳", "stock": 0, "category": "飲料"},
    {"name": "パン", "stock": 3, "category": "食品"},
    {"name": "みかん", "stock": 10, "category": "果物"},
]

available = [p for p in products if p["stock"] > 0]
fruits = [p for p in products if p["category"] == "果物"]
out_of_stock = [p for p in products if p["stock"] == 0]

print(f"在庫あり: {len(available)}商品")
print(f"売り切れ: {[p['name'] for p in out_of_stock]}")
```

## 読み方ガイド
```python
if member_level == "gold":        # member_level が "gold" と等しいか？
if purchase_amount >= 5000:       # 金額が5000以上か？
if member_level != "bronze":      # "bronze" ではないか？
if name in ["田中", "佐藤"]:       # リストの中に name が含まれているか？
if cond_a and cond_b:             # A かつ B の両方か？
if cond_a or cond_b:              # A または B のどちらかか？
if not is_expired:                # is_expired ではない（否定）か？
```

## よくあるパターン

**パターン1：Noneチェック**
```python
if result is None:           # 値が存在しないとき
    print("データが見つかりません")

if result is not None:       # 値が存在するとき
    print(f"結果: {result}")
```

**パターン2：文字列の含みチェック**
```python
if "エラー" in message:        # message に "エラー" が含まれているか
    alert_admin(message)
```

**パターン3：三項演算子（1行で条件分岐）**
```python
status = "在庫あり" if stock > 0 else "売り切れ"
# stock > 0 なら "在庫あり"、そうでなければ "売り切れ"
```

## 確認問題

**問1** 以下のコードを実行したとき、何が表示されるか答えてください。
```python
role = "admin"
active = True

if role == "admin" and active:
    print("管理者メニューを表示")
else:
    print("アクセス拒否")
```

**問2** 以下のコードで、変数 `result` には何が入るか答えてください。
```python
price = 800
result = "送料無料" if price >= 1000 else "送料500円"
```

**問3** `==` と `is` の違いを説明してください。（ヒント: 値の比較 vs 同じオブジェクトかの比較）

---
→ 前: [17. コンテキストマネージャ（with文）](17_context_managers.md)
→ 次: [19. 文字列操作（string operations）](19_string_operations.md)
