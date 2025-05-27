import matplotlib.pyplot as plt
from matplotlib import font_manager

jp_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msgothic.ttc")


artists = [
    "Mrs. GREEN APPLE", "Number_i", "back number", "Kenshi Yonezu", "Jin",
    "XG", "Vaundy", "Yorushika", "King Gnu", "tuki."
]
streams = [
    6513056, 3407064, 2532684, 1623276, 1456784,
    1184964, 1169484, 1148768, 1138252, 942404
]

plt.figure(figsize=(8, 6))
plt.barh(artists[::-1], streams[::-1]) 
plt.title("再生数が多いアーティストTOP10", fontproperties=jp_font)
plt.xlabel("総再生数", fontproperties=jp_font)
plt.ylabel("アーティスト名", fontproperties=jp_font)
plt.tight_layout()
plt.show()