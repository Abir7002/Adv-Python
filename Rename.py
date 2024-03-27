import pandas as pd
data = pd.read_csv("C:/Users/Abir Das/Documents/abir.csv")
##x = ["Player","Span"]
x = {"Player":"Khiladi","Mat":"Match"}
y = data.rename(x,axis="columns")
##y = data.drop(x, axis="columns")
print(y.to_string())
