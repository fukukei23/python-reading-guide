# 05-03 エラー読解クイズ（10問）

> エラーメッセージを見て「何が起きているか」を答えるクイズです。
> 03_error_messages の内容を復習しましょう。

---

## Q1

```
Traceback (most recent call last):
  File "app.py", line 15, in <module>
    result = 100 / 0
ZeroDivisionError: division by zero
```

**これは何をしていますか？** エラーの原因と、どう直せばいいかを答えてください。

---

## Q2

```
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    print(user_name)
NameError: name 'user_name' is not defined
```

**これは何をしていますか？**

---

## Q3

```
Traceback (most recent call last):
  File "shop.py", line 22, in <module>
    item = items[5]
IndexError: list index out of range
```

**これは何をしていますか？**

---

## Q4

```
Traceback (most recent call last):
  File "config.py", line 10, in <module>
    db_port = config["port"]
KeyError: 'port'
```

**これは何をしていますか？**

---

## Q5

```
Traceback (most recent call last):
  File "calc.py", line 5, in <module>
    result = "数量: " + 3
TypeError: can only concatenate str (not "int") to str
```

**これは何をっていますか？**

---

## Q6

```
Traceback (most recent call last):
  File "data.py", line 12, in load_data
    with open("data.csv", "r") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
```

**これは何をしていますか？**

---

## Q7

```
Traceback (most recent call last):
  File "app.py", line 30, in <module>
    if score = 100:
SyntaxError: invalid syntax
```

**これは何をしていますか？**

---

## Q8

```
Traceback (most recent call last):
  File "api.py", line 45, in fetch_user
    response = requests.get(url)
AttributeError: module 'requests' has no attribute 'get'
```

**これは何をしていますか？**

---

## Q9

```
Traceback (most recent call last):
  File "bot.py", line 20, in handle_message
    age = int(user_input)
ValueError: invalid literal for int() with base 10: '二十歳'
```

**これは何をしていますか？**

---

## Q10

```
Traceback (most recent call last):
  File "app.py", line 10, in <module>
    from utils import helper
ImportError: cannot import name 'helper' from 'utils'
```

**これは何をしていますか？**

---

## 解答

<details>
<summary>解答を表示（クリックして開く）</summary>

**Q1**:
- **エラー**: `ZeroDivisionError`（ゼロ除算エラー）
- **原因**: 0で割ろうとしている。`100 / 0` は数学的にもプログラミング的にも不可能
- **直し方**: 割る数が0でないか確認する。`if b != 0: result = 100 / b`

**Q2**:
- **エラー**: `NameError`（名前エラー）
- **原因**: `user_name` という変数が定義されていないのに使おうとしている
- **直し方**: 変数を事前に定義するか、スペルミスを直す。例: `user_name = "山田"` を先に書く

**Q3**:
- **エラー**: `IndexError`（インデックスエラー）
- **原因**: リスト `items` の範囲を超えて `[5]` にアクセスしようとしている
- **直し方**: リストの長さを確認する。`if len(items) > 5: item = items[5]`

**Q4**:
- **エラー**: `KeyError`（キーエラー）
- **原因**: 辞書 `config` に `"port"` というキーが存在しない
- **直し方**: `config.get("port", デフォルト値)` を使うか、キーのスペルを確認する

**Q5**:
- **エラー**: `TypeError`（型エラー）
- **原因**: 文字列と整数を `+` で繋ごうとしている。Pythonでは型が違うと繋げない
- **直し方**: 数値を文字列に変換する: `result = "数量: " + str(3)` または f文字列: `f"数量: {3}"`

**Q6**:
- **エラー**: `FileNotFoundError`（ファイル未検出エラー）
- **原因**: `data.csv` というファイルが存在しないのに開こうとしている
- **直し方**: ファイル名を確認する、ファイルが正しい場所にあるか確認する、または `try/except` で対応する

**Q7**:
- **エラー**: `SyntaxError`（文法エラー）
- **原因**: `=`（代入）を `if` の条件に使っている。比較には `==` を使う必要がある
- **直し方**: `if score == 100:` に修正する

**Q8**:
- **エラー**: `AttributeError`（属性エラー）
- **原因**: `requests` モジュールに `get` という属性（関数）がない。インポートに問題がある可能性が高い
- **直し方**: `import requests` が正しくできているか確認。別の名前のモジュールと衝突していないかも確認

**Q9**:
- **エラー**: `ValueError`（値エラー）
- **原因**: `int()` で文字列 `"二十歳"` を数値に変換しようとしているが、数字ではないので変換できない
- **直し方**: ユーザー入力が数値かどうかを先に確認する。`try/except` で `ValueError` をキャッチする

**Q10**:
- **エラー**: `ImportError`（インポートエラー）
- **原因**: `utils` モジュールから `helper` をインポートしようとしたが、`helper` が存在しない
- **直し方**: `utils.py` の中に `helper` が定義されているか確認する。名前のスペルミスの可能性もある

---

## エラーメッセージ読解のコツ（まとめ）

エラーメッセージは **下から上** に読みましょう。

```
1. 一番下の行 → エラーの種類とメッセージ（何が起きたか）
2. その上の行 → どのファイルのどの行で起きたか（どこで起きたか）
3. Traceback全体 → 処理の呼び出し順序（どうやってそこにたどり着いたか）
```

| エラー名 | 意味 | よくある原因 |
|---------|------|------------|
| `SyntaxError` | 文法エラー | `:` 忘れ、`=` と `==` の間違い |
| `NameError` | 名前エラー | 未定義の変数を使った |
| `TypeError` | 型エラー | 型の違うデータを演算した |
| `ValueError` | 値エラー | 変換できない値を変換しようとした |
| `IndexError` | 範囲エラー | リストの範囲外にアクセスした |
| `KeyError` | キーエラー | 辞書にないキーを指定した |
| `AttributeError` | 属性エラー | 存在しないメソッドやプロパティを呼んだ |
| `FileNotFoundError` | ファイルエラー | 存在しないファイルを開いた |
| `ImportError` | インポートエラー | 存在しないモジュールや関数をインポートした |

</details>
