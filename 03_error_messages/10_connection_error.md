# 10. ConnectionError: つながらない

## ざっくり言うと
プログラムが「相手のサーバーに接続できません」と言っているエラーです。
**ネットワークが切れている**、**サーバーが動いていない**、**URLが間違っている**などが原因です。

## エラー例

### 例1: サーバーに接続できない
```python
>>> import requests
>>> requests.get("http://localhost:9999/api")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
requests.exceptions.ConnectionError:
  HTTPConnectionPool(host='localhost', port=9999):
  Max retries exceeded with url: /api
  (Caused by NewConnectionError(
    'urllib3.connection.HTTPConnection object at 0x...>:
    Failed to establish a new connection:
    [Errno 111] Connection refused'))
```

### 例2: ネットワークが切れている
```python
>>> import urllib.request
>>> urllib.request.urlopen("http://example.com")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
urllib.error.URLError: <urlopen error [Errno 8]
  Name or service not known>
```

### 例3: データベース接続失敗
```python
>>> import psycopg2
>>> psycopg2.connect(host="wrong-host", dbname="mydb")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
psycopg2.OperationalError: could not connect to server:
  Connection refused
  Is the server running on host "wrong-host" and accepting
  TCP/IP connections on port 5432?
```

## トレースバックの読み方

```
requests.exceptions.ConnectionError:
  HTTPConnectionPool(host='localhost', port=9999):
  ↑                              ↑              ↑
エラーの種類              接続先ホスト      ポート番号

  Failed to establish a new connection:
  [Errno 111] Connection refused
       ↑                ↑
   エラー番号        「接続を拒否された」
```

**ポイント**:
- `Connection refused` = サーバーが動いていない
- `Name or service not known` = ホスト名が間違っている
- `Is the server running` = サーバーが起動しているか確認して

## 対処法

1. **サーバーが動いているか**確認する
2. **URL / ホスト名 / ポート番号**が正しいか確認する
3. **ネットワーク接続**を確認する
4. **リトライ**する（一時的な問題の可能性）
   ```python
   import time
   import requests

   for attempt in range(3):
       try:
           response = requests.get(url)
           break
       except requests.ConnectionError:
           print(f"接続失敗。{attempt + 1}回目のリトライ...")
           time.sleep(3)
   ```

## 確認問題

**問1**: `Connection refused` は何が原因として考えられる？

**問2**: 次のエラーから読み取れる情報は？
```
HTTPConnectionPool(host='api.example.com', port=8080):
```

**問3**: ConnectionError が出たときにまず確認することを3つ挙げてください。

---
→ 前: [09_timeout_error.md](09_timeout_error.md)
→ 次: なし
