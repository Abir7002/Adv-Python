import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/Abir Das/Documents/Product.xlsx")
mylabel = ["Apple", "Mango", "Banana", "Grapes", "Potato", "Tomato", "Brinjal"]
data.plot(kind="pie", y="Prise", labels= mylabel,autopct='%1.1f%%')

plt.show()
