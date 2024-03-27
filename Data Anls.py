import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/Abir Das/Desktop/Batting/t20.csv")
print(data.to_string())
data.plot(kind="bar")
plt.show()
