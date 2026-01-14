import matplotlib.pyplot as plt
labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [45, 25, 15, 15]

plt.pie(sizes, labels=labels,
        autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()