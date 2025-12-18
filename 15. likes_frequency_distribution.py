import pandas as pd

df=pd.read_csv("socialmedia.csv")
likes_frequency=df["Likes"].value_counts()
print("Likes Frequency Distribution:")
print(likes_frequency)