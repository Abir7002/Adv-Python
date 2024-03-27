import matplotlib.pyplot as plt

Brands = ["Poco","Iphone","Redmi","Vivo","1+"]
Price = [20000,100000,10000,30000,60000]

plt.bar(Brands,Price,color= "Red")
plt.title("Phone")
plt.xlabel("Brands")
plt.ylabel("Price")
plt.show()
