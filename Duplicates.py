import pandas as pd
a = pd.read_csv("C:/Users/Abir Das/Documents/Book2.csv")
x = a.drop_duplicates(inplace = True)
print(x)
