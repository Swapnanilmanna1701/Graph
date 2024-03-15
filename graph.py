
import matplotlib.pyplot as plt
x = ['Math','Physics','Chemistry']
y = [70,90,60]


plt.plot(x,y)
plt.title('Marks of Students')
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.legend()
plt.grid()
plt.show()
