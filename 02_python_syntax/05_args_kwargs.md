# 5. *args / **kwargs — いくつでも引数を受け取る

## ざっくり言くと
関数を作るとき、**引数の数を決めなくていい**書き方です。
- `*args` — いくつでも「普通の引数」を受け取る（タプルになる）
- `**kwargs` — いくつでも「名前つき引数」を受け取る（辞書になる）

## コード例

### 例1: *args の基本
```python
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))       # → 6
print(add_all(10, 20, 30, 40)) # → 100
```

### 例2: **kwargs の基本
```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="たろう", age=25, city="東京")
# → name: たろう
# → age: 25
# → city: 東京
```

### 例3: 両方組み合わせる
```python
def mix(a, b, *args, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")

mix(1, 2, 3, 4, x=10, y=20)
# → a=1, b=2
# → args=(3, 4)
# → kwargs={'x': 10, 'y': 20}
```

## 読み方ガイド

1. `*` は「余った普通の引数をまとめる」
2. `**` は「余った名前つき引数をまとめる」
3. `args` と `kwargs` は名前なので変更可能だが、**慣例としてこの名前を使う**
4. 並び順: `普通の引数 → *args → **kwargs`

## よくあるパターン

- ログ出力関数でメッセージを自由に受け取る
- 親クラスの関数に引数をそのまま渡す
- デコレータでどんな関数にも対応する

## 確認問題

**問1**: 次の関数呼び出しで `args` の値は？
```python
def test(*args):
    print(args)

test("a", "b", "c")
```

**問2**: 次の関数呼び出しで `kwargs` の値は？
```python
def greet(**kwargs):
    print(kwargs)

greet(name="花子", mood="元気")
```

**問3**: 次のコードはエラーになる。なぜ？
```python
def wrong(**kwargs, *args):
    pass
```

---
→ 前: [04_with_statement.md](04_with_statement.md)
→ 次: [06_init_self.md](06_init_self.md)
