import pandas as pd
data = pd.read_csv("C:/UsersAbir Das/OneDrive/Documents/MARKSHEET.csv")
x =data.drop_duplicates()
print(x)
