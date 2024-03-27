import pandas as pd
data = pd.read_csv("C:/Users/Abir Das/Documents/Book1.csv")
x = data.fillna(10)
print(x.to_string())
