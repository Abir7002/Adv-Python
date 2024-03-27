import matplotlib.pyplot as plt

populations = [100000,400000,7000000,500000]

mylable = ["Nepal","India","China","America"]

mycolor = ["Orange","Blue","Red","Navy"]
plt.pie(populations, labels =mylable,colors = mycolor)
plt.show()
