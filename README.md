# spotify-portfolio
Spotifyチャートデータを使ったデータ分析ポートフォリオ
## 1. プロジェクト概要

**タイトル：**

Spotifyチャートデータを用いた人気アーティスト分析と傾向可視化

**目的：**

SQLとPythonを用いて、アーティストの人気傾向をデータから読み解き、再生数やチャートイン曲数との関係を分析。

「SQLでの集計・Pythonでの可視化・仮説に基づいた検証」という分析業務の基礎的スキルを実践した。

---

## 2. 使用技術・ツール

| カテゴリ | 内容 |
| --- | --- |
| 言語 | SQL、Python |
| ライブラリ | pandas、matplotlib |
| データ | Spotifyチャートデータ（手動で収集） |
| 使用環境 | MySQL、VSCode |

---

## 3. 分析内容と実行結果

---

### 分析①：アーティスト別総再生数TOP10

**目的：**

再生数の多いアーティストを抽出し、ユーザーの人気傾向を把握する。

**SQLクエリ：**

```sql
SELECT artist_names, SUM(streams) AS total_streams
FROM spotify_chart
GROUP BY artist_names
ORDER BY total_streams DESC
LIMIT 10;

```

**可視化：**

Python (matplotlib) にて横棒グラフ作成

![Spotify_graph.png](attachment:ce1bac2e-136d-4d65-99b6-55bb95753e60:Spotify_graph.png)

**考察：**

- Mrs. GREEN APPLE が圧倒的な再生数で1位。複数の楽曲でのチャートインが要因と推察。
- 上位はJ-POP系アーティストが多く、日本国内リスナーの傾向を反映していると考えられる。

---

### 分析②：チャートイン曲数と再生数の相関分析

**目的：**

アーティストの「チャートインした曲数」と「総再生数」に相関関係があるかを確認。

**前処理：**

- SQLでアーティストごとのチャートイン曲数を集計（`COUNT(DISTINCT track_name)`）
- 再生数合計とマージ（pandas）

**可視化：**

散布図＋相関係数の算出（`df.corr()`）

![soukan.png](attachment:2b9c7bc9-c0d9-4b48-9ddd-e3368a4657db:soukan.png)

**相関係数：**

**r = 0.95**（非常に強い正の相関）

**考察：**

- チャートイン曲数が多いアーティストほど再生数も高い傾向。
- Mrs. GREEN APPLEは最多の12曲がチャートインし、再生数も最大。
- 一方でJinのように1曲だけで高再生数を記録している例もあり、単曲バズ型の成功も存在。

---

## 4. 学び・工夫点

- SQLとPythonの組み合わせによる実務的な分析フローを体験
- グラフに日本語フォントを適用し、読みやすいアウトプットを意識
- 相関分析を通じて、仮説立てと検証という「データアナリストの思考」を実践
