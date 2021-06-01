
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return  np.cos(x) + np.sin(x)#$x**4-x**2#12*x-18*x**2#6*x**2 - 6*x**3


a,b = -5,5
x = np.linspace(a,b,100)
y = f(x)

plt.plot(x,y,color='k')
plt.grid()
plt.show()
