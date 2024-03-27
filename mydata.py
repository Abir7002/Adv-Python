import pandas as pd
data = pd.read_csv("C:/Users/Abir Das/Documents/abir.csv")
x = data.dropna()
print(x.to_string())
