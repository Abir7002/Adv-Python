import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C:/Users/Abir Das/Documents/MARKSHEET.csv")
data.plot(kind="scatter",axix="columns",x="Student",y="Total")
plt.show()
