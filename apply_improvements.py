#!/usr/bin/env python3
"""Apply 8 improvements to all 30 interactive HTML files.

A1: Code-side Japanese comments (always visible)
A2: "Where is this used?" usage badge
A3: Progress persistence via localStorage
B1: Sidebar navigation
B2: Keyboard shortcuts (→, ←, R)
C1: "Didn't understand" help button
C2: Code comparison view
C3: Dark/light mode toggle
"""

import os
import re
import json

BASE = os.path.dirname(os.path.abspath(__file__))

# ── Lesson list for sidebar ──────────────────────────────────────
BASICS = [
    ('01_variables.html', '1. 変数'),
    ('02_functions.html', '2. 関数'),
    ('03_parameters.html', '3. 引数'),
    ('04_conditionals.html', '4. 条件分岐'),
    ('05_loops.html', '5. 繰り返し'),
    ('06_lists.html', '6. リスト'),
    ('07_dictionaries.html', '7. 辞書'),
    ('08_strings_numbers.html', '8. 文字列と数値'),
    ('09_boolean_none.html', '9. 真偽値とNone'),
    ('10_imports.html', '10. インポート'),
    ('11_classes.html', '11. クラス'),
    ('12_methods.html', '12. メソッド'),
    ('13_try_except.html', '13. 例外処理'),
    ('14_async_await.html', '14. 非同期'),
    ('15_type_hints.html', '15. 型ヒント'),
    ('16_decorators.html', '16. デコレータ'),
    ('17_context_managers.html', '17. コンテキスト'),
    ('18_operators.html', '18. 演算子'),
    ('19_string_operations.html', '19. 文字列操作'),
    ('20_file_io.html', '20. ファイル入出力'),
]

SYNTAX = [
    ('01_indentation.html', '1. インデント'),
    ('02_fstring.html', '2. f文字列'),
    ('03_list_comprehension.html', '3. リスト内包表記'),
    ('04_with_statement.html', '4. with文'),
    ('05_args_kwargs.html', '5. *args/**kwargs'),
    ('06_init_self.html', '6. __init__とself'),
    ('07_lambda.html', '7. ラムダ'),
    ('08_generators.html', '8. ジェネレータ'),
    ('09_slicing.html', '9. スライス'),
    ('10_exceptions_custom.html', '10. カスタム例外'),
]

# ── A2: Usage badges per file ─────────────────────────────────────
USAGE_BADGES = {
    '01_variables.html': 'ECサイトの価格計算で「price = 1980」のように商品価格を保存',
    '02_functions.html': 'NexusCoreでエージェントの初期化処理を関数にまとめて再利用',
    '03_parameters.html': 'LINE Botで「ユーザー名」と「メッセージ」を引数で受け取って返信',
    '04_conditionals.html': '在庫管理で「在庫が0以下なら発注」という条件分岐',
    '05_loops.html': '物販管理で商品リストの全アイテムを順番に価格チェック',
    '06_lists.html': 'スクレイピング結果をリストにまとめて一括処理',
    '07_dictionaries.html': '商品データを「名前→価格」の辞書で素早く検索',
    '08_strings_numbers.html': '価格表示で「¥1,980」のように数値を文字列に整形',
    '09_boolean_none.html': '「ログイン済みかどうか」をTrue/Falseで判定',
    '10_imports.html': 'datetimeモジュールをインポートして日付計算',
    '11_classes.html': 'NexusCoreのエージェントをクラスで定義（名前・役割・状態を持つ）',
    '12_methods.html': '商品オブジェクトに「割引計算」メソッドを追加',
    '13_try_except.html': 'API呼び出し失敗時にプログラムが落ちないよう保護',
    '14_async_await.html': '複数サイトの同時スクレイピングで待ち時間を短縮',
    '15_type_hints.html': 'チーム開発で「この関数は文字列を返す」ことを明示',
    '16_decorators.html': '「実行時間を測る」機能をデコレータで共通化',
    '17_context_managers.html': 'ファイルを開いて使い終わったら自動で閉じる',
    '18_operators.html': '価格の比較（割引前＞割引後）や論理演算（在庫あり AND 価格OK）',
    '19_string_operations.html': '商品名の空白除去や「¥」マークの追加・削除',
    '20_file_io.html': '在庫データをCSVファイルに保存・読み込み',
    '01_indentation.html': 'Pythonでブロック（処理のまとまり）をインデントで表す',
    '02_fstring.html': '「こんにちは、田中さん」のように変数を文字列に埋め込む',
    '03_list_comprehension.html': '商品リストから「価格＞1000円」だけを新しいリストに抽出',
    '04_with_statement.html': 'ファイルやDB接続を確実にクローズするパターン',
    '05_args_kwargs.html': '関数に「任意の数の引数」を渡せるようにする',
    '06_init_self.html': 'クラスの初期設定（コンストラクタ）の書き方',
    '07_lambda.html': 'ソート時の「並び替えキー」を1行で指定',
    '08_generators.html': '大量データをメモリ節約しながら1件ずつ処理',
    '09_slicing.html': '文字列やリストの「最初から3番目まで」を取り出す',
    '10_exceptions_custom.html': '独自のエラーメッセージを作って分かりやすくする',
}

# ── C1: Help text per file ────────────────────────────────────────
HELP_TEXT = {
    '01_variables.html': '変数は「箱」です。箱に名前を付けて、好きなものを入れられます。\nたとえば price = 1980 なら、「price」という名前の箱に1980という数字を入れます。\nあとで price と書けば、いつでも1980を取り出せます。\n箱の中身は後から変えられるので「変数（変わる数）」と呼びます。',
    '02_functions.html': '関数は「作業の手順をまとめたもの」です。\nたとえば「料金を計算する」という手順を関数にしておけば、\n何度でも calc_price(1980) と呼び出すだけで計算結果が得られます。\n何度も同じコードを書かなくて済むのがメリットです。',
    '03_parameters.html': '引数（ひきすう）は「関数に渡すデータ」です。\n関数を呼ぶときにカッコの中に値を書くと、関数の中でその値が使えます。\nたとえば greet("田中") と呼べば、関数の中で name = "田中" として使えます。',
    '04_conditionals.html': 'if文は「もし〜なら」という条件分岐です。\n条件が成り立つ（True）ならifの中身を実行し、\n成り立たない（False）ならelseの中身を実行します。\n日常生活の「雨が降ったら傘を持っていく」と同じ考え方です。',
    '05_loops.html': 'for文は「指定した回数だけ繰り返す」仕組みです。\nrange(5) なら5回繰り返します。リストの要素を1つずつ取り出すこともできます。\n「同じ作業を何度もする」ときに使います。',
    '06_lists.html': 'リストは「複数のデータを順番に並べたもの」です。\nカンマ区切りで要素を並べて [ ] で囲みます。\nshopping = ["りんご", "みかん", "バナナ"] のように、\n関連するデータを1つにまとめて管理できます。',
    '07_dictionaries.html': '辞書は「名前→値」のペアをまとめたものです。\n{"名前": "田中", "年齢": 25} のように、キーと値を : で繋ぎます。\nperson["名前"] と書けば "田中" がすぐ取り出せます。\nリストとの違い：リストは番号で取り出す、辞書は名前で取り出す。',
    '08_strings_numbers.html': '文字列は " " で囲んだテキスト、数値はそのまま数字を書きます。\n"1980" は文字列（テキストとしての1980）、1980 は数値（計算できる1980）。\n文字列同士は + で繋げますが、計算はできません。',
    '09_boolean_none.html': 'True は「はい」、False は「いいえ」です。\nNone は「何もない」ことを表す特別な値です。\nis_logged_in = True なら「ログイン済み」、\nresult = None なら「結果はまだ何もない」という意味になります。',
    '10_imports.html': 'importは「他人が作った機能を借りてくる」ことです。\nimport datetime と書けば、日付計算の機能が使えるようになります。\nPythonには便利な機能がたくさん用意されていて、importで呼び出せます。',
    '11_classes.html': 'クラスは「設計図」です。設計図から実物（インスタンス）を作れます。\n「車」という設計図があれば、色や名前の違う車を何台でも作れます。\n設計図に「走る」「止まる」などの動作も定義できます。',
    '12_methods.html': 'メソッドは「クラスの中で定義した関数」です。\nオブジェクト.メソッド名() とドットで繋いで呼び出します。\ncar.run() なら「車オブジェクトに走れと命令する」イメージです。',
    '13_try_except.html': 'try-exceptは「エラーが起きてもプログラムを止めない」仕組みです。\ntryの中でエラーが起きたら、exceptの中身が実行されます。\n「もしうまくいかなかったら、こうする」という保険です。',
    '14_async_await.html': 'async/awaitは「待っている間に別の作業をする」仕組みです。\nレストランで注文してから料理が来るまでスマホを見るのと同じ。\n「待ち時間を無駄にしない」ための書き方です。',
    '15_type_hints.html': '型ヒントは「この変数には何が入るか」をコメント的に書くものです。\ndef greet(name: str) -> str: なら「nameは文字列、返り値も文字列」という意味。\n実行には影響しませんが、コードを読む人にとって分かりやすくなります。',
    '16_decorators.html': 'デコレータは「関数に機能を追加するラッパー」です。\n@timer と関数の上に書くだけで、その関数の実行時間が測れるようになります。\n関数の中身を変えずに機能を追加できるのがポイントです。',
    '17_context_managers.html': 'with文は「開始と終了をセットで管理」する仕組みです。\nwith open(...) as f: と書けば、ファイルは必ず最後に閉じられます。\n「使い終わったら必ず片付ける」を自動化する仕組みです。',
    '18_operators.html': '演算子は「計算や比較の記号」です。\n+ - * / は計算、== != > < は比較、and or not は論理です。\n数学で使う記号とほぼ同じなので、あまり心配いりません。',
    '19_string_operations.html': '文字列操作は「テキストを切り貼りする」機能です。\n"hello".upper() で "HELLO" に、"  hello  ".strip() で空白を削除。\n商品名やユーザー入力の整形によく使います。',
    '20_file_io.html': 'ファイル入出力は「データをファイルに保存・読み込みする」機能です。\nopen()でファイルを開き、write()で書き込み、read()で読み込みます。\nプログラムを終了してもデータが残るようにする仕組みです。',
    '01_indentation.html': 'インデント（字下げ）はPythonのブロック（まとまり）を表します。\n他の言語は { } で囲みますが、Pythonはインデントだけで表します。\n4つのスペースが标准です。Tabキーではなくスペースを使います。',
    '02_fstring.html': 'f文字列は f"..." の中に {変数名} と書くだけで変数を埋め込めます。\nf"こんにちは、{name}さん" なら name の値がそのまま入ります。\n文字列の連結（+）よりシンプルに書けます。',
    '03_list_comprehension.html': 'リスト内包表記は「リストを1行で作る」書き方です。\n[x*2 for x in range(5)] で [0, 2, 4, 6, 8] が作れます。\nfor文で書くより短く書けますが、まずはfor文を理解してからでOKです。',
    '04_with_statement.html': 'with文は「開けたら閉じる」を自動でやってくれます。\nwith open("file.txt") as f: と書けば、処理が終わったら自動で閉じられます。\n「閉じ忘れ」を防ぐための安全な書き方です。',
    '05_args_kwargs.html': '*args は「任意の数の引数」、**kwargs は「任意の名前付き引数」です。\ndef func(*args) なら func(1,2,3) のようにいくつでも渡せます。\n「何個来るか分からない」時に便利な書き方です。',
    '06_init_self.html': '__init__ は「インスタンス作成時に自動で呼ばれる初期設定メソッド」です。\nself は「自分自身（そのインスタンス）」を指す特別な変数です。\nself.name = name で「このインスタンスのname属性にnameを保存」します。',
    '07_lambda.html': 'lambdaは「名前のない1行関数」です。\nlambda x: x * 2 は def double(x): return x * 2 と同じ。\n短い処理をその場で書きたい時に使います。',
    '08_generators.html': 'ジェネレータは「1つずつ値を作って返す」関数です。\nyield で値を返し、次に呼ばれたら続きから再開します。\n大量のデータを一度にメモリに載せないための仕組みです。',
    '09_slicing.html': 'スライスは [開始:終了] で一部を取り出す機能です。\n[1:4] ならインデックス1から3まで（4は含まない）。\n[:3] なら最初から3つ、[2:] なら3番目から最後まで取り出せます。',
    '10_exceptions_custom.html': 'カスタム例外は「自分で定義したエラー」です。\nclass MyError(Exception): と書けば独自のエラー型が作れます。\n「何が悪かったか」を具体的に伝えるために使います。',
}

# ── C2: Comparison view (only specific lessons) ──────────────────
COMPARISONS = {
    '04_conditionals.html': {
        'title': 'if vs if-elif-else',
        'left': {'label': 'if-else（2パターン）', 'code': 'if score >= 60:\n    print("合格")\nelse:\n    print("不合格")'},
        'right': {'label': 'if-elif-else（3パターン以上）', 'code': 'if score >= 80:\n    print("優")\nelif score >= 60:\n    print("良")\nelse:\n    print("不可")'},
    },
    '05_loops.html': {
        'title': 'for vs while',
        'left': {'label': 'for（回数が分かっている時）', 'code': 'for i in range(5):\n    print(f"{i}回目")'},
        'right': {'label': 'while（条件が満たされるまで）', 'code': 'count = 0\nwhile count < 5:\n    print(f"{count}回目")\n    count += 1'},
    },
    '06_lists.html': {
        'title': 'リスト vs 辞書',
        'left': {'label': 'リスト（順番が大事）', 'code': 'fruits = ["りんご", "みかん", "バナナ"]\nprint(fruits[0])  # りんご'},
        'right': {'label': '辞書（名前が大事）', 'code': 'prices = {"りんご": 150, "みかん": 100}\nprint(prices["りんご"])  # 150'},
    },
    '08_strings_numbers.html': {
        'title': '文字列 vs 数値',
        'left': {'label': '文字列の「+」（繋ぐ）', 'code': '"1980" + "円"\n# 結果: "1980円"'},
        'right': {'label': '数値の「+」（足す）', 'code': '1980 + 20\n# 結果: 2000'},
    },
    '16_decorators.html': {
        'title': 'デコレータあり vs なし',
        'left': {'label': 'デコレータなし（手動呼び出し）', 'code': 'def greet(name):\n    print(f"こんにちは、{name}")\n\ngreet("田中")  # 手動で呼ぶ'},
        'right': {'label': 'デコレータあり（機能追加）', 'code': '@timer\ndef greet(name):\n    print(f"こんにちは、{name}")\n\ngreet("田中")  # 実行時間も表示'},
    },
    '01_indentation.html': {
        'title': 'Python vs 他の言語',
        'left': {'label': 'Python（インデントでブロック）', 'code': 'if x > 0:\n    print("正の数")\n    print("です")'},
        'right': {'label': 'JavaScript（{}でブロック）', 'code': 'if (x > 0) {\n    console.log("正の数");\n    console.log("です");\n}'},
    },
}

# ── CSS block to inject ───────────────────────────────────────────
CSS_BLOCK = """
/* === A1: Line comments === */
.code-line { display: flex; align-items: center; min-height: 38px; }
.line-comment {
  font-family: var(--font-ui); font-size: 12px; color: var(--fg-dim);
  margin-left: 16px; display: flex; align-items: center;
  white-space: normal; flex: 1; min-width: 0; opacity: 0.8;
}
.code-line.active .line-comment { opacity: 1; }

/* === A2: Usage badge === */
.usage-badge {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(52,211,153,0.08); border: 1px solid rgba(52,211,153,0.25);
  border-radius: 20px; padding: 6px 14px; margin-top: 12px;
  font-size: 13px; color: #6ee7b7; line-height: 1.4;
}
.usage-badge .badge-icon { font-size: 14px; }

/* === B1: Sidebar === */
.sidebar-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,0.5);
  z-index: 200; opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
.sidebar-overlay.open { opacity: 1; pointer-events: auto; }
.sidebar {
  position: fixed; top: 0; left: 0; bottom: 0; width: 300px;
  background: var(--bg-raised); border-right: 1px solid var(--border);
  z-index: 201; transform: translateX(-100%); transition: transform 0.3s ease;
  overflow-y: auto; padding: 24px 16px;
}
.sidebar.open { transform: translateX(0); }
.sidebar-title { font-size: 15px; color: var(--fg-bright); margin-bottom: 16px; font-weight: 700; display: flex; justify-content: space-between; align-items: center; }
.sidebar-section { margin-bottom: 14px; }
.sidebar-heading { font-size: 11px; color: var(--fg-dim); font-weight: 700; letter-spacing: 0.08em; margin-bottom: 4px; padding: 0 8px; }
.sidebar-link {
  display: flex; align-items: center; gap: 6px;
  padding: 6px 8px; border-radius: 5px;
  font-size: 13px; color: var(--fg-dim); text-decoration: none; transition: all 0.2s;
}
.sidebar-link:hover { background: rgba(255,255,255,0.05); color: var(--fg); }
.sidebar-link.current { background: var(--accent-dim); color: var(--accent); font-weight: 600; }
.sidebar-link .check { color: var(--success); font-size: 11px; display: none; }
.sidebar-link.visited .check { display: inline; }
.sidebar-close {
  background: none; border: none; color: var(--fg-dim); cursor: pointer;
  font-size: 20px; padding: 0 4px; line-height: 1;
}
.sidebar-close:hover { color: var(--fg); }
.btn-hamburger {
  background: none; border: none; cursor: pointer;
  display: flex; flex-direction: column; gap: 4px; padding: 6px 4px;
}
.btn-hamburger span {
  display: block; width: 18px; height: 2px; background: var(--fg-dim);
  border-radius: 1px; transition: all 0.3s;
}

/* === C1: Help button === */
.btn-help {
  display: inline-flex; align-items: center; gap: 6px;
  margin-top: 12px; padding: 8px 16px;
  background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3);
  border-radius: 6px; color: var(--warning); font-size: 13px;
  font-family: var(--font-ui); cursor: pointer; transition: all 0.2s;
}
.btn-help:hover { background: rgba(251,191,36,0.15); }
.help-content {
  max-height: 0; overflow: hidden; transition: max-height 0.4s ease;
}
.help-content.open { max-height: 500px; }
.help-inner {
  background: rgba(251,191,36,0.05); border-left: 3px solid var(--warning);
  border-radius: 0 6px 6px 0; padding: 14px 18px; font-size: 14px;
  line-height: 1.8; margin-top: 8px; white-space: pre-line;
}

/* === C2: Comparison view === */
.comparison-section { margin-bottom: 36px; }
.comparison-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.comparison-card {
  background: var(--code-bg); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden;
}
.comparison-label {
  padding: 8px 14px; font-size: 12px; font-weight: 700;
  background: rgba(0,0,0,0.15); border-bottom: 1px solid var(--border); color: var(--fg-dim);
}
.comparison-code {
  padding: 14px 16px; font-family: var(--font-mono); font-size: 13px;
  line-height: 1.8; white-space: pre; color: var(--fg);
}

/* === C3: Theme toggle === */
.header-controls { display: flex; align-items: center; gap: 8px; }
.theme-toggle {
  background: none; border: 1px solid var(--border); border-radius: 6px;
  padding: 4px 10px; cursor: pointer; font-size: 15px;
  transition: all 0.2s; color: var(--fg-dim); line-height: 1;
}
.theme-toggle:hover { border-color: var(--accent); color: var(--fg); }
body.light {
  --bg: #f8f9fa; --bg-raised: #fff; --code-bg: #f1f3f5;
  --accent: #7c3aed; --accent-dim: rgba(124,58,237,0.12);
  --fg: #2d2d3f; --fg-dim: #6b7280; --fg-bright: #1a1a2e;
  --border: #e5e7eb; --warning: #d97706; --success: #059669;
}
body.light .term-popup { background: #fff; box-shadow: 0 4px 16px rgba(0,0,0,0.12); }
body.light .watch-panel { background: #f1f3f5; }
body.light .sidebar { background: #fff; border-right-color: #e5e7eb; }
body.light .concept-card { background: #fff; }
body.light .quiz-card { background: #fff; }
body.light .comparison-card { background: #f1f3f5; }
"""

# ── JS block to inject ────────────────────────────────────────────
JS_BLOCK = """
// === B2: Keyboard shortcuts ===
document.addEventListener('keydown', function(e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === 'ArrowRight' || e.key === ' ') {
    e.preventDefault();
    var btn = document.getElementById('btnStep');
    if (btn && !btn.disabled) btn.click();
  } else if (e.key === 'ArrowLeft') {
    e.preventDefault();
    if (currentStep > 0) { currentStep--; updateDisplay(); }
  } else if (e.key === 'r' || e.key === 'R') {
    if (!e.ctrlKey && !e.metaKey) {
      e.preventDefault();
      var btnR = document.getElementById('btnReset');
      if (btnR) btnR.click();
    }
  }
});

// === A3: Progress tracking ===
(function() {
  var path = window.location.pathname;
  var m = path.match(/\\/(\\d{2}_\\w+)\\/interactive\\/(\\d{2}_\\w+)\\.html/);
  if (!m) return;
  var lessonId = m[1] + '/' + m[2];
  var key = 'prg_progress';
  try {
    var data = JSON.parse(localStorage.getItem(key) || '{}');
    data[lessonId] = Date.now();
    localStorage.setItem(key, JSON.stringify(data));
  } catch(e) {}
})();

// === B1: Sidebar toggle ===
var sidebarOverlay = document.querySelector('.sidebar-overlay');
var sidebar = document.querySelector('.sidebar');
document.querySelector('.btn-hamburger').addEventListener('click', function() {
  sidebarOverlay.classList.add('open');
  sidebar.classList.add('open');
  // Mark visited links
  try {
    var data = JSON.parse(localStorage.getItem('prg_progress') || '{}');
    var links = sidebar.querySelectorAll('.sidebar-link');
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute('href');
      if (!href) continue;
      var lm = href.match(/\\/(\\d{2}_\\w+)\\/interactive\\/(\\d{2}_\\w+)\\.html/);
      if (lm && data[lm[1] + '/' + lm[2]]) links[i].classList.add('visited');
    }
  } catch(e) {}
});
function closeSidebar() {
  sidebarOverlay.classList.remove('open');
  sidebar.classList.remove('open');
}
if (sidebarOverlay) sidebarOverlay.addEventListener('click', closeSidebar);
var sidebarCloseBtn = document.querySelector('.sidebar-close');
if (sidebarCloseBtn) sidebarCloseBtn.addEventListener('click', closeSidebar);

// === C3: Theme toggle ===
(function() {
  var saved = localStorage.getItem('prg_theme');
  if (saved === 'light') document.body.classList.add('light');
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) toggle.addEventListener('click', function() {
    document.body.classList.toggle('light');
    var isLight = document.body.classList.contains('light');
    toggle.textContent = isLight ? '\\u2600' : '\\u263E';
    localStorage.setItem('prg_theme', isLight ? 'light' : 'dark');
  });
  // Set initial icon
  if (toggle) toggle.textContent = document.body.classList.contains('light') ? '\\u2600' : '\\u263E';
})();

// === C1: Help toggle ===
var helpBtns = document.querySelectorAll('.btn-help');
for (var h = 0; h < helpBtns.length; h++) {
  helpBtns[h].addEventListener('click', function() {
    var target = this.nextElementSibling;
    if (target && target.classList.contains('help-content')) {
      target.classList.toggle('open');
      this.textContent = target.classList.contains('open') ? '\\u2713 わかった！' : '\\u2753 わからなかった';
    }
  });
}
"""


def build_sidebar_html(current_file, section):
    """Build the sidebar HTML for a given file."""
    lines = []
    lines.append('<div class="sidebar-overlay"></div>')
    lines.append('<div class="sidebar">')
    lines.append('<div class="sidebar-title">ナビゲーション <button class="sidebar-close">&times;</button></div>')

    lines.append('<div class="sidebar-section">')
    lines.append('<div class="sidebar-heading">BASICS (言語共通概念)</div>')
    for fname, title in BASICS:
        href = f'../../01_basics/interactive/{fname}' if section == 'syntax' else fname
        cls = ' current' if section == 'basics' and fname == current_file else ''
        lines.append(f'<a class="sidebar-link{cls}" href="{href}"><span class="check">✓</span>{title}</a>')
    lines.append('</div>')

    lines.append('<div class="sidebar-section">')
    lines.append('<div class="sidebar-heading">SYNTAX (Python固有)</div>')
    for fname, title in SYNTAX:
        href = fname if section == 'syntax' else f'../../02_python_syntax/interactive/{fname}'
        cls = ' current' if section == 'syntax' and fname == current_file else ''
        lines.append(f'<a class="sidebar-link{cls}" href="{href}"><span class="check">✓</span>{title}</a>')
    lines.append('</div>')

    lines.append('</div>')
    return '\n'.join(lines)


def extract_step_descs(content):
    """Extract step descriptions from the steps array."""
    # Match: desc:'some text'
    return re.findall(r"desc:\s*'([^']*)'", content)


def add_line_comments(html_body, descs):
    """Add .line-comment spans to code lines."""
    lines = html_body.split('\n')
    result = []
    line_idx = 0
    for line in lines:
        if '<div class="code-line"' in line and 'data-line=' in line:
            # Find the closing </div> of this line
            # Check if it ends on the same line
            if '</div>' in line and line.strip().endswith('</div>'):
                # Single-line code-line
                comment = descs[line_idx] if line_idx < len(descs) else ''
                # Insert comment before the last </div>
                insert_pos = line.rfind('</div>')
                comment_html = f'<span class="line-comment"># {comment}</span></div>'
                line = line[:insert_pos] + comment_html
                line_idx += 1
            else:
                # Multi-line - just add to result as-is
                pass
        result.append(line)
    return '\n'.join(result)


def add_usage_badge(html_body, badge_text):
    """Add usage badge after concept-card."""
    if not badge_text:
        return html_body
    badge = f'<div class="usage-badge"><span class="badge-icon">\U0001F4CD</span> 使い道: {badge_text}</div>'
    # Insert after </div> of concept-card
    return html_body.replace('</div>\n\n  <div class="section-title">', badge + '\n\n  <div class="section-title">', 1)


def add_help_button(html_body, help_text, section_id):
    """Add help button after key-point section."""
    if not help_text:
        return html_body
    btn = f'<button class="btn-help" type="button">❓ わからなかった</button>'
    content = f'<div class="help-content"><div class="help-inner">{help_text}</div></div>'
    # Insert after key-point closing div
    target = '</div>\n\n  <div class="section-title">'
    # Find the second occurrence (after quiz section-title)
    idx = html_body.find(target)
    if idx >= 0:
        idx2 = html_body.find(target, idx + 1)
        if idx2 >= 0:
            insert_point = idx2
            insert_html = btn + '\n    ' + content + '\n\n  '
            return html_body[:insert_point] + insert_html + html_body[insert_point:]
    return html_body


def add_comparison(html_body, comp_data):
    """Add comparison section before quiz section."""
    if not comp_data:
        return html_body
    left = comp_data['left']
    right = comp_data['right']
    comp_html = f'''
  <div class="comparison-section">
    <div class="section-title"><span class="icon">⇄</span> {comp_data['title']}</div>
    <div class="comparison-grid">
      <div class="comparison-card">
        <div class="comparison-label">{left['label']}</div>
        <div class="comparison-code">{left['code']}</div>
      </div>
      <div class="comparison-card">
        <div class="comparison-label">{right['label']}</div>
        <div class="comparison-code">{right['code']}</div>
      </div>
    </div>
  </div>
'''
    target = '<div class="section-title"><span class="icon">'
    # Insert before the quiz section-title (second occurrence)
    idx = html_body.find(target)
    if idx >= 0:
        idx2 = html_body.find(target, idx + len(target))
        if idx2 >= 0:
            return html_body[:idx2] + comp_html + '\n  ' + html_body[idx2:]
    return html_body


def process_file(filepath, section, filename):
    """Apply all improvements to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 0. Strip previously injected CSS/JS to allow clean re-run
    content = re.sub(r'\n/\* === A1: Line comments === \*/.*?/\* === C3: Theme toggle === \*/.*?body\.light \.comparison-card \{ background: #f1f3f5; \}\n', '', content, flags=re.DOTALL)
    content = re.sub(r'\n// === B2: Keyboard shortcuts ===.*?// === C1: Help toggle ===\n.*?\n\}', '\n', content, flags=re.DOTALL)

    # 1. Add hamburger + theme toggle to header (before CSS injection!)
    if 'class="btn-hamburger"' not in content:
        old_header = '<div class="header-top">'
        idx = content.find(old_header)
        if idx >= 0:
            header_start = idx
            header_end = content.find('</div>', idx) + len('</div>')
            old_header_block = content[header_start:header_end]
            new_header = '<div class="header-top">\n\t    <a href="../../index.html" style="font-size:13px;color:var(--fg-dim);text-decoration:none;display:flex;align-items:center;gap:4px;">&larr; トップ</a>\n\t    <div class="header-controls"><button class="btn-hamburger" type="button" aria-label="メニュー"><span></span><span></span><span></span></button><button class="theme-toggle" type="button" aria-label="テーマ切替"></button></div>'
            step_match = re.search(r'<span class="header-step">.*?</span>', old_header_block)
            if step_match:
                new_header += ' ' + step_match.group(0)
            new_header += '\n\t  </div>'
            content = content[:header_start] + new_header + content[header_end:]

    # 2. Add sidebar before closing </div> of container
    if '<div class="sidebar-overlay"' not in content:
        sidebar_html = build_sidebar_html(filename, section)
        last_div = content.rfind('</div>')
        if last_div >= 0:
            content = content[:last_div] + sidebar_html + '\n\n' + content[last_div:]

    # 3. Extract step descriptions and add line comments (A1)
    if 'class="line-comment"' not in content:
        descs = extract_step_descs(content)
        content = add_line_comments(content, descs)

    # 4. Add usage badge (A2) - use regex for flexible whitespace
    badge = USAGE_BADGES.get(filename, '')
    if badge and '<div class="usage-badge"' not in content:
        badge_html = '<div class="usage-badge"><span class="badge-icon">\U0001F4CD</span> 使い道: ' + badge + '</div>\n\n'
        # Insert after concept-card closing, before <section
        content = re.sub(
            r'(</div>)\s*(<section\s+style)',
            r'\1\n    ' + badge_html + r'\2',
            content, count=1
        )

    # 5. Add help button (C1) - insert before quiz section-title
    help_text = HELP_TEXT.get(filename, '')
    if help_text and '<button class="btn-help"' not in content:
        btn_html = '<button class="btn-help" type="button">❓ わからなかった</button>\n    <div class="help-content"><div class="help-inner">' + help_text + '</div></div>\n\n  '
        # Insert before the second occurrence of section-title (which is the quiz)
        parts = content.split('<div class="section-title">')
        if len(parts) >= 3:
            content = parts[0] + '<div class="section-title">' + parts[1] + '<div class="section-title">' + btn_html + parts[2]
            for p in parts[3:]:
                content += '<div class="section-title">' + p

    # 6. Add comparison section (C2) - before quiz section
    comp = COMPARISONS.get(filename)
    if comp and '<div class="comparison-section"' not in content:
        comp_html = '\n  <div class="comparison-section">\n    <div class="section-title"><span class="icon">⇄</span> ' + comp['title'] + '</div>\n    <div class="comparison-grid">\n      <div class="comparison-card">\n        <div class="comparison-label">' + comp['left']['label'] + '</div>\n        <div class="comparison-code">' + comp['left']['code'] + '</div>\n      </div>\n      <div class="comparison-card">\n        <div class="comparison-label">' + comp['right']['label'] + '</div>\n        <div class="comparison-code">' + comp['right']['code'] + '</div>\n      </div>\n    </div>\n  </div>\n\n  '
        # Insert before the quiz section-title
        quiz_marker = '<span class="icon">&#10067;</span>'
        idx = content.find(quiz_marker)
        if idx >= 0:
            # Find the start of the containing section-title div
            line_start = content.rfind('<div', 0, idx)
            content = content[:line_start] + comp_html + content[line_start:]

    # 7. Inject CSS before </style>
    if '/* === A1: Line comments === */' not in content:
        content = content.replace('</style>', CSS_BLOCK + '</style>')

    # 8. Inject JS before </script>
    if '// === B2: Keyboard shortcuts ===' not in content:
        content = content.replace('</script>', JS_BLOCK + '</script>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    dirs = [
        (os.path.join(BASE, '01_basics', 'interactive'), 'basics'),
        (os.path.join(BASE, '02_python_syntax', 'interactive'), 'syntax'),
    ]

    count = 0
    for dirpath, section in dirs:
        if not os.path.isdir(dirpath):
            print(f'SKIP: {dirpath} not found')
            continue
        files = sorted([f for f in os.listdir(dirpath) if f.endswith('.html')])
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            try:
                process_file(filepath, section, filename)
                count += 1
                print(f'OK: {section}/{filename}')
            except Exception as e:
                print(f'ERR: {section}/{filename}: {e}')

    print(f'\nDone: {count} files updated')


if __name__ == '__main__':
    main()
