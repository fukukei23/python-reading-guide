# 05-02 コード読解クイズ（15問）

> 実際のコードを見て「何をしているか」を答えるクイズです。
> まず自分で答えてから、下の解答を見てください。

---

## 第1部：コードの目的を読む（5問）

### Q1 — この関数は何をしていますか？

```python
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total
```

---

### Q2 — この関数は何をしていますか？

```python
def find_user(users, target_name):
    for user in users:
        if user["name"] == target_name:
            return user
    return None
```

---

### Q3 — このコードは何をしていますか？

```python
data = [3, 1, 4, 1, 5, 9, 2, 6]
filtered = [x for x in data if x > 3]
```

---

### Q4 — この関数は何をしていますか？

```python
def format_price(amount):
    return f"¥{amount:,}"
```

`format_price(19800)` を呼び出すと何が返りますか？

---

### Q5 — このコードは何をしていますか？

```python
with open("data.txt", "r") as f:
    content = f.read()
```

---

## 第2部：バグを見つける（5問）

### Q6 — このコードの問題点は何ですか？

```python
numbers = [1, 2, 3]
print(numbers[3])
```

---

### Q7 — このコードの問題点は何ですか？

```python
def divide(a, b):
    return a / b

result = divide(10, 0)
```

---

### Q8 — このコードの問題点は何ですか？

```python
user = {"name": "鈴木"}
print(user["age"])
```

---

### Q9 — このコードの問題点は何ですか？

```python
if score = 100:
    print("満点!")
```

---

### Q10 — このコードの問題点は何ですか？

```python
for i in range(5)
    print(i)
```

---

## 第3部：出力を予想する（5問）

### Q11

```python
def mystery(x):
    if x <= 0:
        return 0
    return x + mystery(x - 1)

print(mystery(3))
```

出力は何ですか？

---

### Q12

```python
items = ["a", "b", "c", "d", "e"]
result = items[1:4]
print(result)
```

出力は何ですか？

---

### Q13

```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```

出力は何ですか？

---

### Q14

```python
def func(a, *args):
    return len(args)

print(func(1, 2, 3, 4))
```

出力は何ですか？

---

### Q15

```python
class Counter:
    count = 0

    def increment(self):
        Counter.count += 1
        return Counter.count

c1 = Counter()
c2 = Counter()
c1.increment()
c1.increment()
c2.increment()
print(Counter.count)
```

出力は何ですか？

---

## 解答

<details>
<summary>解答を表示（クリックして開く）</summary>

**Q1**: リストの中の数値をすべて合計して返す関数。`prices` の各要素を `total` に足し込んでいる。

**Q2**: ユーザーのリストから、指定した名前のユーザーを探して返す関数。見つからなければ `None` を返す。

**Q3**: `data` の中から「3より大きい数」だけを取り出して新しいリスト `filtered` を作っている。結果は `[4, 5, 9, 6]`。これは「リスト内包表記」という書き方。

**Q4**: `¥19,800` が返る。`f"¥{amount:,}"` の `:,` は「3桁ごとにカンマを入れる」という書式指定。

**Q5**: `data.txt` というファイルを読み込みモード（`"r"`）で開き、中身をすべて `content` に保存している。`with` を使うと、処理が終わったら自動でファイルが閉じられる。

**Q6**: `IndexError` が起きる。リストの添字は 0 から始まるので、3要素のリストでは `[0]`, `[1]`, `[2]` までしかアクセスできない。`[3]` は範囲外。

**Q7**: `ZeroDivisionError` が起きる。0で割ることはできない。`b` が0でないかチェックが必要。

**Q8**: `KeyError` が起きる。辞書に `"age"` というキーが存在しない。`user.get("age", "不明")` のように書くと安全。

**Q9**: `SyntaxError` が起きる。比較には `==` を使うべき。`=` は代入なので、`if` の条件には使えない。正しくは `if score == 100:`。

**Q10**: `SyntaxError` が起きる。`range(5)` の後に `:`（コロン）がない。正しくは `for i in range(5):`。

**Q11**: `6`。`mystery(3)` = 3 + `mystery(2)` = 3 + 2 + `mystery(1)` = 3 + 2 + 1 + `mystery(0)` = 3 + 2 + 1 + 0 = 6。このような関数を「再帰関数」と呼ぶ。

**Q12**: `['b', 'c', 'd']`。スライス `[1:4]` は「インデックス1から3まで」を取り出す（4は含まない）。

**Q13**: `4`。`y = x` はコピーではなく「同じリストを指す」。なので `y.append(4)` で `x` も変更される。リストの長さは4になる。

**Q14**: `3`。`*args` は「残りの引数をすべてまとめる」構文。`a` に 1 が入り、`args` は `(2, 3, 4)` になる。`len(args)` は3。

**Q15**: `3`。`count` はクラス変数（すべてのインスタンスで共有）。`c1` で2回、`c2` で1回増やしたので、合計3。

</details>
