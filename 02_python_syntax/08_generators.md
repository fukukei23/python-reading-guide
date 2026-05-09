# 8. yield — 1つずつ値を出す

## ざっくり言うと
`yield` は関数の中で**値を1つずつ出す**命令です。
`return` が「全部まとめて返す」なのに対し、`yield` は「1つ出して、また続きから始める」ことができます。

## コード例

### 例1: 基本的なジェネレータ
```python
def count_up():
    yield 1
    yield 2
    yield 3

for num in count_up():
    print(num)
# → 1
# → 2
# → 3
```

### 例2: 無限に数を出す
```python
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

gen = even_numbers()
print(next(gen))  # → 0
print(next(gen))  # → 2
print(next(gen))  # → 4
```

### 例3: 大きなデータを扱う
```python
def read_lines(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()  # 1行ずつ出す

# ファイルが大きくてもメモリを節約できる
for line in read_lines("big_data.txt"):
    print(line)
```

## 読み方ガイド

1. `yield` を使う関数は**ジェネレータ**になる
2. `yield 値` で値を1つ出す（関数は一時停止する）
3. `next()` で次の値を取り出す
4. `for` ループでも取り出せる
5. `return` との違い: returnは関数を終了、yieldは一時停止

## よくあるパターン

- 大きなファイルを1行ずつ読む
- 無限に続く数列を作る
- メモリを節約しながらデータを処理する

## 確認問題

**問1**: 次のコードの出力は？
```python
def gen():
    yield "A"
    yield "B"

g = gen()
print(next(g))
print(next(g))
```

**問2**: `yield` と `return` の違いを説明してください。

**問3**: ジェネレータはどんなときに便利か？

---
→ 前: [07_lambda.md](07_lambda.md)
→ 次: [09_slicing.md](09_slicing.md)
