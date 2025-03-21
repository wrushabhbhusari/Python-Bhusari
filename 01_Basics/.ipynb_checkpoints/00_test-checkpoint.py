import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

x = np.linspace(-10,7,100)
y= f(x)

plt.plot(x,y,label="y=sin(x)",color='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph of sin(x)")
plt.legend()
plt.grid()
plt.show()