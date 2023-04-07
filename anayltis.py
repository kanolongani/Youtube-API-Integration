import pandas as pd

df = pd.read_csv("video_details.csv")
df.plot.scatter(x = 'likes', y = 'comments', s = 100);