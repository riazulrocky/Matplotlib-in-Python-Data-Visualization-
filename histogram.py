import matplotlib.pyplot as plt

data=[5,15,12,17,15,26,25,39,30]
plt.hist(data,bins=5,
         color="skyblue",edgecolor="black")
plt.title("Histogram")
plt.show()