import matplotlib.pyplot as plt
import numpy as np
sub = ['Math','Physics','Chemistry']
s1=[96,99,95]
s2 = [89,100,96]
plt.plot(sub, s1,label="Swapnanil")
plt.plot(sub, s2,label="Supriti")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Marks Comparison of Students")
plt.legend()
plt.show()
