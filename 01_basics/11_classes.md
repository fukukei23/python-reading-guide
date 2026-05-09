# 11. クラス（class） — 設計図

## ざっくり言うと
クラスは「ものの設計図」です。たとえば「商品」という設計図を作れば、それをもとに「りんご」「みかん」などの商品をたくさん作れます。

## コード例

### 例1：ECサイトの商品クラス
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name}: ¥{self.price}")

apple = Product("りんご", 150)
apple.display()
```

### 例2：LINEボットのユーザークラス
```python
class LineUser:
    def __init__(self, user_id, display_name):
        self.user_id = user_id
        self.display_name = display_name
        self.message_count = 0

    def send_message(self, text):
        self.message_count += 1
        print(f"{self.display_name}へ送信: {text}")

user = LineUser("U1234", "田中さん")
user.send_message("こんにちは！")
```

## 読み方ガイド
```python
class Product:                          # 「Product」という設計図を定義する
    def __init__(self, name, price):    # 新しい商品を作るときの準備（初期設定）
        self.name = name                # この商品の「名前」を設定する
        self.price = price              # この商品の「値段」を設定する
```
- `class` = 設計図の名前を決めるキーワード
- `__init__` = インスタンス（実体）が作られるときに自動で呼ばれる特別な関数
- `self` = 「自分自身」を指す言葉。`self.name`は「この商品の名前」の意味

## よくあるパターン

**パターン1：データベースのレコードを表す**
```python
class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
        self.status = "pending"
```

**パターン2：クラスを継承する（設計図を元に詳しい設計図を作る）**
```python
class DigitalProduct(Product):          # Productの設計図を引き継ぐ
    def __init__(self, name, price, download_url):
        super().__init__(name, price)   # 元の初期設定を呼ぶ
        self.download_url = download_url
```

## 確認問題

**問1** 以下のコードは何をしているか、日本語で説明してください。
```python
class Customer:
    def __init__(self, email):
        self.email = email
        self.points = 0
```

**問2** 以下のコードを実行したとき、何が表示されるか答えてください。
```python
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, value):
        self.result += value

calc = Calculator()
calc.add(5)
calc.add(3)
print(calc.result)
```

**問3** `self` は何を指しているか、例2のコードを使って説明してください。

---
→ 前: [10. 辞書（dict）](10_dicts.md)
→ 次: [12. メソッド（method）](12_methods.md)
