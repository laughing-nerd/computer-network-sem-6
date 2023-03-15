from matplotlib import pyplot as plt
import math
p=[]
f1=[]
f2=[]

p=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
for i in p:
    f1.append(1/(1-math.exp(-i)))
    f2.append((1-math.exp(-i))/(1+math.exp(i)))

plt.xlabel("p --->")
plt.ylabel("f(p) --->")
plt.plot(p,f1, label=r"f1(p)=$\frac{1}{1-e^{-p}}$")
plt.plot(p,f2, label=r"f2(p)=$\frac{1-e^{-p}}{1+e^{+p}}$")
plt.legend()
plt.show()




