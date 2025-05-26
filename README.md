
## Spotify チャートデータ分析ポートフォリオ

## プロジェクト概要

Spotifyのチャートデータをもとに、アーティストの再生数やチャートイン傾向を分析。  
SQLとPythonを使って、集計・可視化・相関分析まで一貫して行いました。

## 使用技術

- SQL（MySQL構文）
- Python（pandas, matplotlib）
- Jupyter / VSCode
- GitHub

## ファイル構成

spotify-portfolio/
├── spotify_data.csv # 元データ
├── graph_top10.py # Top10再生数グラフコード
├── correlation_analysis.py # 相関分析コード
├── Top10_bar_chart.png # 横棒グラフ
├── Correlation_scatter.png # 散布図（相関分析）
└── README.md # この説明



## 分析①：アーティスト別総再生数TOP10

### 使用SQL
```sql
SELECT artist_names, SUM(streams) AS total_streams
FROM spotify_chart
GROUP BY artist_names
ORDER BY total_streams DESC
LIMIT 10;
グラフ

考察
Mrs. GREEN APPLEが最多再生数で1位。複数のヒット曲による安定した人気が伺える。

上位には日本のJ-POPアーティストが多く、国内ユーザーの傾向が反映されている。

📈 分析②：チャートイン曲数 × 総再生数の相関分析
曲数が多いほど、再生数が高いという傾向はあるのか？

pandasでアーティストごとの曲数と再生数をマージし、相関係数を算出

相関係数
r = 0.95（非常に強い正の相関）

グラフ

考察
チャートイン曲数が多いアーティストほど、総再生数も高い傾向が見られた。

Jinのように1曲だけで高い再生数を記録しているアーティストもおり、単曲ヒット型の成功も存在。

✍️ 今後の展望
時系列データが取れれば、再生数の推移や順位変動の分析も行いたい。

楽曲のジャンルやユーザー属性との関係性なども外部データを組み合わせて分析してみたい。

📎 制作目的
転職活動において、データ分析スキルを実務に近い形で証明するためのポートフォリオとして制作しました。
