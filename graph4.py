# this is plotting a graph using function
import matplotlib.pyplot as plt
import numpy as np
def f(x,a,b,c):
    return a*x**2+b*x+c
xlist = np.linspace(-10,10,num=1000)
ylist =f(xlist,5,2,3)
plt.figure(num=0, dpi=120)
plt.plot(xlist,ylist,label="f(x)")
plt.plot(xlist,ylist**4,label="f(x)**8")
plt.plot(xlist,ylist**(1/2), label='f(x)**(1/2)')
plt.xlabel("height")
plt.ylabel("weight")
plt.title("Swapnanil's graph")
plt.legend()

plt.show()