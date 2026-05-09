# 7. lambda — 1行関数

## ざっくり言うと
`lambda` は**名前のない小さな関数**を1行で作る書き方です。
「ラムダ」と読みます。簡単な処理をその場で書きたいときに使います。

## コード例

### 例1: 基本的な使い方
```python
# 通常の関数
def double(x):
    return x * 2

# lambda（同じことを1行で）
double = lambda x: x * 2

print(double(5))  # → 10
```

### 例2: sort() と組み合わせる
```python
students = [
    {"name": "たろう", "score": 80},
    {"name": "花子", "score": 95},
    {"name": "次郎", "score": 70},
]

# scoreで並べ替える
students.sort(key=lambda s: s["score"], reverse=True)
# 花子(95), たろう(80), 次郎(70) の順になる
```

### 例3: map() と組み合わせる
```python
numbers = [1, 2, 3, 4, 5]

# すべて2倍にする
doubled = list(map(lambda x: x * 2, numbers))
# doubled = [2, 4, 6, 8, 10]
```

## 読み方ガイド

1. `lambda 引数: 戻り値` の形で書く
2. `return` は書かない（`:` の右が戻り値）
3. 引数は複数でもOK: `lambda x, y: x + y`
4. 複雑な処理には向かない（`def` を使う）

## よくあるパターン

- `sort(key=lambda ...)` — 並べ替えの基準を指定
- `map(lambda ..., list)` — 全要素に処理を適用
- `filter(lambda ..., list)` — 条件で絞り込む

## 確認問題

**問1**: 次の lambda と同じ処理の関数を `def` で書いてください。
```python
add = lambda a, b: a + b
```

**問2**: 次のコードの結果は？
```python
words = ["banana", "apple", "cherry"]
words.sort(key=lambda w: len(w))
print(words)
```

**問3**: `lambda x: x > 0` は何をする lambda か？

---
→ 前: [06_init_self.md](06_init_self.md)
→ 次: [08_generators.md](08_generators.md)
