import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

jp_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")

streams_data = {
    "artist_names": [
        "Mrs. GREEN APPLE", "Number_i", "back number", "Kenshi Yonezu", "Jin",
        "XG", "Vaundy", "Yorushika", "King Gnu", "tuki."
    ],
    "total_streams": [
        6513056, 3407064, 2532684, 1623276, 1456784,
        1184964, 1169484, 1148768, 1138252, 942404
    ]
}

song_count_data = {
    "artist_names": [
        "Mrs. GREEN APPLE", "back number", "Number_i", "Kenshi Yonezu", "Vaundy",
        "XG", "Yorushika", "King Gnu", "tuki.", "Jin"
    ],
    "song_count": [
        12, 6, 6, 4, 4,
        3, 3, 2, 2, 1
    ]
}

df_streams = pd.DataFrame(streams_data)
df_songs = pd.DataFrame(song_count_data)

merged_df = pd.merge(df_streams, df_songs, on="artist_names")

correlation = merged_df["song_count"].corr(merged_df["total_streams"])
print(f"相関係数：{correlation:.2f}")


plt.figure(figsize=(8, 6))
plt.scatter(merged_df["song_count"], merged_df["total_streams"], color='orange')


for i, row in merged_df.iterrows():
    plt.text(row["song_count"] + 0.05, row["total_streams"], row["artist_names"], fontsize=8)


plt.title(f"チャートイン曲数と総再生数の相関（r={correlation:.2f}）", fontproperties=jp_font)
plt.xlabel("チャートイン曲数", fontproperties=jp_font)
plt.ylabel("総再生数", fontproperties=jp_font)
plt.grid(True)
plt.tight_layout()
plt.show()