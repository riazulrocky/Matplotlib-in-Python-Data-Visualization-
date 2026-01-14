import matplotlib.pyplot as plt

x=[1,2,3,4]
y1=[10,20,30,40]
y2=[5,13,17,20]

plt.plot(x,y1,label="Line1",color="blue")
plt.plot(x,y2,label="Line2",color="red")
plt.title("Multiple Lines")
plt.legend()
plt.show()