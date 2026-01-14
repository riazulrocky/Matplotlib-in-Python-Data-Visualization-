from matplotlib import pyplot as plt

names=["A", "B", "C", "D"]
values=[10, 24, 36, 18]
plt.barh(names, values, color="orange")
plt.title("Horizontal Bar Chart")
plt.show()