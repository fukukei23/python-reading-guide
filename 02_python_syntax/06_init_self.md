# 6. __init__ と self — 初期設定

## ざっくり言うと
- `__init__` はクラスからオブジェクトを作るときの**「初期設定」**メソッド
- `self` は**「自分自身」**を指す言葉。自分のデータにアクセスするために使う

## コード例

### 例1: 基本的なクラス
```python
class Dog:
    def __init__(self, name, age):
        self.name = name   # self.name = 自分の名前
        self.age = age     # self.age = 自分の年齢

    def bark(self):
        print(f"{self.name}がワンと吠えました！")

pochi = Dog("ポチ", 3)
pochi.bark()  # → ポチがワンと吠えました！
```

### 例2: 複数のオブジェクトを作る
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):
        if self.score >= 60:
            return "合格"
        else:
            return "不合格"

s1 = Student("たろう", 80)
s2 = Student("花子", 45)

print(s1.result())  # → 合格
print(s2.result())  # → 不合格
```

### 例3: __init__ なしのクラス
```python
class Greeter:
    def hello(self):
        print("こんにちは！")

g = Greeter()
g.hello()  # → こんにちは！
# __init__ がなくても動く（初期設定が不要な場合）
```

## 読み方ガイド

1. `__init__` は **initialize（初期化）** の略
2. `self` はメソッドの**第1引数**として必ず書く
3. `self.変数名` でデータを保存する（インスタンス変数）
4. `__init__` は `クラス名()` を呼んだときに**自動で実行**される

## よくあるパターン

- データを保持するオブジェクトを作る（User, Product など）
- 初期値を設定する（`self.count = 0`）
- 接続や設定を読み込む

## 確認問題

**問1**: `self` を書かないとどうなる？
```python
class Bad:
    def __init__(name, age):   # self がない
        self.name = name
```

**問2**: 次のコードで `pochi.age` の値は？
```python
pochi = Dog("ポチ", 5)
```

**問3**: `__init__` はいつ実行される？

---
→ 前: [05_args_kwargs.md](05_args_kwargs.md)
→ 次: [07_lambda.md](07_lambda.md)
