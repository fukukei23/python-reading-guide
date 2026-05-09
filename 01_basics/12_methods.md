# 12. メソッド（method） — オブジェクトの関数

## ざっくり言うと
メソッドは「オブジェクトが持つ動作」のことです。たとえば「ショッピングカート」に「商品を追加する」「合計を計算する」という動作を持たせることができます。

## コード例

### 例1：ショッピングカートのメソッド
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def total(self):
        return sum(item["price"] for item in self.items)

cart = ShoppingCart()
cart.add_item("ノート", 300)
cart.add_item("ペン", 150)
print(cart.total())
```

### 例2：AIエージェントのメソッド
```python
class AIAgent:
    def __init__(self, name):
        self.name = name
        self.history = []

    def ask(self, question):
        self.history.append(question)
        return f"{self.name}が回答中: {question}について調べます"

    def show_history(self):
        for q in self.history:
            print(f" - {q}")

agent = AIAgent("アシスタント")
agent.ask("Pythonとは？")
agent.show_history()
```

## 読み方ガイド
```python
def add_item(self, name, price):       # 「商品を追加」という動作を定義
    self.items.append(...)             # 自分（カート）の商品リストに追加
```
- `def` = 関数（メソッド）を定義するキーワード
- `(self, name, price)` = self + 受け取る情報（引数）
- `cart.add_item("ノート", 300)` = 「cartというカート」に「ノート300円」を追加する命令

## よくあるパターン

**パターン1：値を取得するメソッド（getter的な役割）**
```python
def get_status(self):
    return f"注文数: {len(self.items)}個"
```

**パターン2：条件によって動作を変えるメソッド**
```python
def apply_discount(self, rate):
    if rate > 0.5:
        print("割引率が高すぎます")
        return
    for item in self.items:
        item["price"] = int(item["price"] * (1 - rate))
```

**パターン3：特別なメソッド `__str__`（文字列表現）**
```python
def __str__(self):
    return f"カート({len(self.items)}商品)"
```

## 確認問題

**問1** 以下のコードで、`agent.ask("天気は？")` を実行すると何が起きるか説明してください。
```python
class AIAgent:
    def __init__(self, name):
        self.name = name
        self.history = []

    def ask(self, question):
        self.history.append(question)
        return f"{self.name}: {question}の回答です"

agent = AIAgent("bot")
result = agent.ask("天気は？")
```

**問2** 以下のコードを実行したとき、何が表示されるか答えてください。
```python
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def show(self):
        print(f"現在: {self.count}")

c = Counter()
c.increment()
c.increment()
c.increment()
c.show()
```

**問3** メソッドの第1引数に必ず書く `self` は何のためにあるか、自分の言葉で説明してください。

---
→ 前: [11. クラス（class）](11_classes.md)
→ 次: [13. エラー処理（try/except）](13_try_except.md)
