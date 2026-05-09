# 04-03 LLMルーターを読む

> 出典: **NexusCore**（マルチエージェントAIフレームワーク）
> 内容: タスクの難しさに応じて、どのAIモデルを使うか決める仕組み

---

## コード全体

```python
def route_task(self, task: Task) -> LLMProvider:
    complexity = self.analyze_complexity(task)
    if complexity.score > 0.8:
        return self.providers["sonnet"]
    elif complexity.score > 0.4:
        return self.providers["glm"]
    else:
        return self.providers["minimax"]
```

---

## 1行ずつ読む

### `def route_task(self, task: Task) -> LLMProvider:`

| 項目 | 説明 |
|------|------|
| `def` | 関数の定義 |
| `route_task` | 関数名。「route＝道筋を決める」 |
| `self` | 自分自身（インスタンス） |
| `task: Task` | 引数。Task型の「タスク」を受け取る |
| `-> LLMProvider` | 戻り値の型。LLMProvider（AIモデルの提供元）を返す |

**使っている概念**: クラスメソッド、型ヒント（02_python_syntax）

**一言で**: 「タスクを受け取って、最適なAIモデルを返す関数」

---

### `complexity = self.analyze_complexity(task)`

| 項目 | 説明 |
|------|------|
| `self.analyze_complexity(task)` | タスクを分析して「難しさ」を評価する |
| `complexity` | 分析結果を保存 |

**一言で**: 「タスクがどれくらい難しいかを分析する」

---

### `if complexity.score > 0.8:` / `return self.providers["sonnet"]`

| 項目 | 説明 |
|------|------|
| `complexity.score` | 難しさのスコア（0.0 〜 1.0） |
| `> 0.8` | 0.8より大きい＝「とても難しい」 |
| `self.providers["sonnet"]` | 辞書から "sonnet" を取り出す |

**使っている概念**: 条件分岐、辞書のアクセス（01_basics）

**一言で**: 「スコアが0.8を超える（かなり難しい）なら、高性能なSonnetを使う」

---

### `elif complexity.score > 0.4:` / `return self.providers["glm"]`

| 項目 | 説明 |
|------|------|
| `elif` | 「そうでなく、もし〜なら」（else if の略） |
| `> 0.4` | 0.4より大きい＝「普通の難しさ」 |
| `"glm"` | GLMモデル |

**一言で**: 「スコアが0.4〜0.8なら、中程度のGLMを使う」

---

### `else:` / `return self.providers["minimax"]`

| 項目 | 説明 |
|------|------|
| `else` | どの条件にも当てはまらない場合 |
| `"minimax"` | MiniMaxモデル（軽量・高速） |

**一言で**: 「スコアが0.4以下なら、軽量なMiniMaxを使う」

---

## 処理の流れ（まとめ）

```
タスクを受け取る
  → 難しさを分析（スコア: 0.0〜1.0）
  → スコアに応じてAIモデルを選ぶ
     0.8超え → Sonnet（高性能）
     0.4超え → GLM（中程度）
     それ以下 → MiniMax（軽量）
```

---

## スコアとモデルの関係

このコードは、実際の **LLMルーティング** をシンプルに実装しています。

```
難しい ←————————————————————→ 簡単
 0.8      0.4       0.0
  |        |          |
Sonnet    GLM      MiniMax
(高性能)  (中程度)  (高速・安価)
```

**なぜこんなことをするのか？**

- 高性能なAIモデルはお金がかかる
- 簡単な質問に高性能モデルを使うのは無駄
- 難易度に合わせてモデルを選ぶと **コストを抑えつつ品質を保てる**

---

## 使われている概念のまとめ

| コード内の書き方 | 使っている概念 | 参照箇所 |
|-----------------|---------------|---------|
| `if` / `elif` / `else` | 条件分岐 | 01_basics |
| `self.providers["key"]` | 辞書のアクセス | 01_basics |
| `task: Task` | 型ヒント | 02_python_syntax |
| `self.method()` | メソッド呼び出し | 01_basics |
| `> 0.8` / `> 0.4` | 比較演算子 | 01_basics |

---

## 練習問題

> このコードを3文で説明してください。
