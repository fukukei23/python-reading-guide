# 04-01 PipelineService を読む

> 出典: **atelier-kyo-manager**（物販管理システム）
> 内容: 商品の画像を一括処理する「パイプライン」サービス

---

## コード全体

```python
class PipelineService:
    def __init__(self, db_session=None):
        self.db = db_session or db.session
        self.notification_service = NotificationService()

    def run_pipeline(self, product_id: int) -> BatchResult:
        product = self.db.query(Product).get(product_id)
        if not product:
            raise ValueError(f"Product {product_id} not found")
        images = self.image_service.process(product.images)
        product.update_images(images)
        self.db.commit()
        self.notification_service.notify(product)
        return BatchResult(success=True, count=len(images))
```

---

## 1行ずつ読む

### `class PipelineService:`

| 項目 | 説明 |
|------|------|
| `class` | 「設計図」を作るキーワード（02_python_syntax 参照） |
| `PipelineService` | クラスの名前。「パイプライン＝一連の処理を順番に実行する仕組み」 |
| `:` | ブロックの開始 |

**一言で**: 「PipelineServiceという名前の設計図を定義しています」

---

### `def __init__(self, db_session=None):`

| 項目 | 説明 |
|------|------|
| `def` | 関数の定義 |
| `__init__` | 初期化メソッド。インスタンスが作られた瞬間に実行される |
| `self` | 「自分自身」。インスタンスのこと |
| `db_session=None` | 引数。何も渡されなかったら `None`（何もない）になる |

**一言で**: 「インスタンスを作るときの準備。データベース接続を受け取る」

---

### `self.db = db_session or db.session`

| 項目 | 説明 |
|------|------|
| `self.db` | インスタンスの中に `db` という箱を作る |
| `or` | 「左がダメなら右」。`db_session` があればそれ、なければ `db.session` |
| `db.session` | 外部から渡されなかった場合の「デフォルトのDB接続」 |

**使っている概念**: 変数、代入、`or` 演算子（01_basics）

**一言で**: 「データベース接続を保存する。渡されたらそれ、渡されなかったらデフォルト」

---

### `self.notification_service = NotificationService()`

| 項目 | 説明 |
|------|------|
| `NotificationService()` | 別のクラスからインスタンスを作っている |
| `self.notification_service` | 通知サービスをインスタンスに保存 |

**使っている概念**: クラスのインスタンス化（01_basics）

**一言で**: 「通知を送るためのサービスも準備しておく」

---

### `def run_pipeline(self, product_id: int) -> BatchResult:`

| 項目 | 説明 |
|------|------|
| `product_id: int` | 引数。「商品ID」という整数を受け取る |
| `-> BatchResult` | 戻り値の型。「この関数は BatchResult を返す」という宣言 |

**使っている概念**: 型ヒント（02_python_syntax）

**一言で**: 「商品IDを受け取って、処理結果を返す関数」

---

### `product = self.db.query(Product).get(product_id)`

| 項目 | 説明 |
|------|------|
| `self.db.query(Product)` | データベースからProduct（商品）を探す |
| `.get(product_id)` | 指定したIDの商品を取得 |

**一言で**: 「データベースから商品を1つ取り出す」

---

### `if not product:` / `raise ValueError(...)`

| 項目 | 説明 |
|------|------|
| `if not product` | 商品が見つからなかった場合 |
| `raise ValueError(...)` | 「値がおかしい」というエラーを意図的に発生させる |
| `f"Product {product_id} not found"` | f文字列。IDをメッセージに埋め込む |

**使っている概念**: 条件分岐、例外（01_basics）、f文字列（02_python_syntax）

**一言で**: 「商品がなかったら、エラーを出して処理を止める」

---

### `images = self.image_service.process(product.images)`

**一言で**: 「商品の画像データを、画像処理サービスに渡して加工する」

---

### `product.update_images(images)` / `self.db.commit()`

| 項目 | 説明 |
|------|------|
| `update_images` | 商品の画像を新しいものに差し替え |
| `commit()` | 変更をデータベースに確定（保存）する |

**一言で**: 「加工した画像を商品に反映し、データベースに保存」

---

### `self.notification_service.notify(product)`

**一言で**: 「処理が終わったことを通知する（メールやSlackなど）」

---

### `return BatchResult(success=True, count=len(images))`

| 項目 | 説明 |
|------|------|
| `BatchResult(success=True, count=len(images))` | 結果オブジェクトを作る |
| `len(images)` | 画像の数を数える |

**一言で**: 「成功したことと、処理した画像の数を報告して終わり」

---

## 処理の流れ（まとめ）

```
商品IDを受け取る
  → DBから商品を探す
  → なかったらエラー
  → 画像を加工する
  → 加工結果を保存する
  → 通知を送る
  → 結果を返す
```

---

## 練習問題

> このコードを3文で説明してください。
