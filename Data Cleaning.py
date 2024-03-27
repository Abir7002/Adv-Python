import pandas as pd
a= pd.read_csv("C:/Users/Abir Das/Desktop/Batting/ODI data.csv")
x= a.dropna(inplace = True)

print(x.to_string())
