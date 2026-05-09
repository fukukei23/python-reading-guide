# 05-01 基礎概念クイズ（20問）

> 01_basics と 02_python_syntax の内容からの出題です。
> まず自分で答えてから、下の解答を見てください。

---

## 第1部：変数とデータ型（5問）

### Q1

```python
name = "田中"
age = 25
```

`name` と `age` はそれぞれ何型ですか？

---

### Q2

```python
x = 10
y = 3
result = x / y
```

`result` の値はいくつですか？

---

### Q3

```python
is_active = True
count = 0
name = ""
```

この中で「偽（Falseと同じ扱い）」なのはどれですか？

---

### Q4

```python
colors = ["赤", "青", "黄"]
```

`colors[1]` の値は何ですか？

---

### Q5

```python
person = {"name": "佐藤", "age": 30}
```

`person["name"]` の値は何ですか？

---

## 第2部：条件分岐と繰り返し（5問）

### Q6

```python
score = 75
if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
else:
    grade = "C"
```

`grade` の値は何ですか？

---

### Q7

```python
for i in range(3):
    print(i)
```

出力される数字をすべて答えてください。

---

### Q8

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
```

`total` の値はいくつですか？

---

### Q9

```python
x = 5
if x > 3 and x < 10:
    result = "OK"
else:
    result = "NG"
```

`result` の値は何ですか？

---

### Q10

```python
count = 0
while count < 3:
    count += 1
```

ループが終わった後、`count` の値はいくつですか？

---

## 第3部：関数（5問）

### Q11

```python
def greet(name):
    return f"こんにちは、{name}さん"
```

`greet("山田")` を呼び出すと、何が返りますか？

---

### Q12

```python
def add(a, b=10):
    return a + b
```

`add(5)` を呼び出すと、何が返りますか？

---

### Q13

```python
def check(age):
    if age >= 20:
        return "成人"
    return "未成年"
```

`check(18)` を呼び出すと、何が返りますか？

---

### Q14

```python
def process(items: list) -> int:
    return len(items)
```

`process(["A", "B", "C"])` を呼び出すと、何が返りますか？

---

### Q15

```python
def multiply(x, y):
    result = x * y
    return result
```

この関数の戻り値は何型になりますか？（引数が両方とも整数の場合）

---

## 第4部：クラスとエラー処理（5問）

### Q16

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name}が吠えました"
```

```python
pochi = Dog("ポチ")
pochi.bark()
```

`pochi.bark()` は何を返しますか？

---

### Q17

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = "エラー"
```

`result` の値は何ですか？

---

### Q18

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

このクラスのインスタンスを作るには、何を渡す必要がありますか？

---

### Q19

```python
def safe_get(data, key):
    try:
        return data[key]
    except KeyError:
        return None
```

`safe_get({"a": 1}, "b")` を呼び出すと、何が返りますか？

---

### Q20

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

`Calculator.add(3, 7)` は何を返しますか？

---

## 解答

<details>
<summary>解答を表示（クリックして開く）</summary>

**Q1**: `name` は文字列型（str）、`age` は整数型（int）

**Q2**: `3.3333...`（小数）。Python 3 では `/` は常に小数の結果を返す

**Q3**: `is_active` は `True`（真）。`count = 0` は偽。`name = ""` は偽。よって `count` と `name` の2つ

**Q4**: `"青"`。リストの添字は0から始まるので、`[1]` は2番目

**Q5**: `"佐藤"`。辞書はキーで値にアクセスする

**Q6**: `"B"`。75は80以上ではないが、60以上なので `elif` の条件に当てはまる

**Q7**: `0`、`1`、`2`（改行区切りで出力）。`range(3)` は0, 1, 2

**Q8**: `6`。偶数は2と4だけ。2 + 4 = 6

**Q9**: `"OK"`。5は3より大きく、10より小さいので条件を満たす

**Q10**: `3`。0→1→2→3で、3 < 3 が偽になってループ終了

**Q11**: `"こんにちは、山田さん"`。f文字列で `name` に "山田" が入る

**Q12**: `15`。`b` のデフォルト値は10。5 + 10 = 15

**Q13**: `"未成年"`。18は20未満なので、最初の `if` を通過し `return "未成年"` が実行される

**Q14**: `3`。リストの要素数は3つ。`len()` で整数が返る

**Q15**: 整数型（int）。整数同士の掛け算の結果は整数

**Q16**: `"ポチが吠えました"`。`self.name` に "ポチ" が保存されている

**Q17**: `"エラー"`。0で割ると `ZeroDivisionError` が起き、except に飛ぶ

**Q18**: `name`（名前）と `age`（年齢）の2つ。`__init__` の引数に `self` 以外の2つがある

**Q19**: `None`。キー `"b"` が存在しないので `KeyError` が起き、`None` が返る

**Q20**: `10`。`@staticmethod` があるので、インスタンスを作らなくても直接呼び出せる

</details>
