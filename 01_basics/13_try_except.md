# 13. エラー処理（try/except）

## ざっくり言うと
プログラムがエラーで止まらないようにする仕組みです。「もしここで失敗したら、こう対応する」という保険のようなものです。車のシートベルトのような役割です。

## コード例

### 例1：ECサイトの決済処理
```python
def process_payment(order_id, amount):
    try:
        if amount <= 0:
            raise ValueError("金額が0以下です")
        print(f"注文{order_id}: ¥{amount}を決済しました")
    except ValueError as e:
        print(f"エラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")
    finally:
        print("決済処理を終了します")

process_payment("A001", 1500)
process_payment("A002", -100)
```

### 例2：APIからのデータ取得
```python
import json

def load_user_config(filepath):
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("設定ファイルが見つかりません。初期設定を使います")
        return {"theme": "light", "lang": "ja"}
    except json.JSONDecodeError:
        print("設定ファイルが壊れています")
        return {"theme": "light", "lang": "ja"}
```

## 読み方ガイド
```python
try:                           # 「試しにやってみる」ブロック
    result = risky_operation() # 失敗するかもしれない処理
except ValueError as e:       # ValueErrorが出たらここに来る
    print(f"エラー: {e}")      # エラー内容を e で受け取れる
except Exception as e:        # その他のエラーも全部拾う
    print(f"不明なエラー: {e}")
finally:                       # 成功・失敗に関わらず必ず実行
    cleanup()
```
- `try` = 「試しに実行する」範囲の開始
- `except` = 「もしエラーが起きたら」の対処法
- `finally` = 成功しても失敗しても必ず最後に実行される

## よくあるパターン

**パターン1：データベース接続のエラー処理**
```python
try:
    db.connect()
    db.execute("INSERT INTO orders ...")
except ConnectionError:
    print("データベースに接続できません")
finally:
    db.close()
```

**パターン2：ユーザー入力の検証**
```python
try:
    age = int(user_input)
except ValueError:
    print("数値を入力してください")
```

## 確認問題

**問1** 以下のコードを実行したとき、何が表示されるか順番に答えてください。
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("ゼロで割ることはできません")
finally:
    print("計算終了")
```

**問2** 以下のコードで `load_user_config("missing.json")` を実行したとき、何が返るか答えてください。（例2を参照）

**問3** `finally` ブロックはいつ実行されるか、次の2つのケースで説明してください：
- 成功したとき
- エラーが起きたとき

---
→ 前: [12. メソッド（method）](12_methods.md)
→ 次: [14. 非同期（async/await）](14_async_await.md)
