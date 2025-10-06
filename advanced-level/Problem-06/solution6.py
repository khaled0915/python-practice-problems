import pandas as pd


df = pd.read_csv("f:/bongodev-class-content/python-practice-problems/advanced-level/Problem-06/users.csv")  


top_users = df.sort_values(by="score", ascending=False).head(5)

print("Top 5 Users by Score:")
print(top_users)
