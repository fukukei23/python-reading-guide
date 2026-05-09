# 4. with文 — 自動で閉じる

## ざっくり言うと
`with` を使うと、ファイルなどを開いたあと**自動で閉じてくれます**。
「開けたら閉める」を忘れないための仕組みです。

## コード例

### 例1: ファイルを読む
```python
# withを使う（おすすめ）
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# ← ここで自動的にファイルが閉じられる

# withを使わない（古い書き方）
f = open("data.txt", "r")
content = f.read()
f.close()  # ← 閉じるのを忘れがち
```

### 例2: ファイルに書く
```python
with open("output.txt", "w") as f:
    f.write("こんにちは\n")
    f.write("Pythonの世界へ\n")
# ← 自動で閉じられて保存される
```

### 例3: 複数のファイルを同時に
```python
with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
    for line in fin:
        fout.write(line)
```

## 読み方ガイド

1. `with` の後に「開くもの」を書く
2. `as 変数名` で名前をつける
3. **インデントの中**で作業する
4. インデントを出たら**自動で閉じられる**

`with open("ファイル名", "モード") as f:`
- `"r"` = 読み込み（read）
- `"w"` = 書き込み（write）
- `"a"` = 追記（append）

## よくあるパターン

- ファイルの読み書き — 一番よく使う
- データベース接続 — `with db.connect() as conn:`
- ロックの取得 — `with lock:`

## 確認問題

**問1**: `with` を抜けたあと、`f.read()` を呼ぶとどうなる？
```python
with open("test.txt", "r") as f:
    text = f.read()
print(f.read())  # ここは？
```

**問2**: 次のコードの `"w"` は何を意味する？
```python
with open("log.txt", "w") as f:
    f.write("エラー発生")
```

**問3**: `with` を使わない場合の問題点は何？

---
→ 前: [03_list_comprehension.md](03_list_comprehension.md)
→ 次: [05_args_kwargs.md](05_args_kwargs.md)
