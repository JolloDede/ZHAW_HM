import matplotlib.pyplot as plt
import numpy as np

plt.grid()

plt.xlabel("X Achse")
plt.ylabel("Y Achse")

# x = np.arange(0, 100, 1000)
# x = np.linspace(0, 100, 1000)
x = np.logspace(0, 100, 1000)
f = 5 / (2*x**2)**(1/3)
g = 10**5 * (2 * np.e)**(-x/100)
h = (10**(2*x) / 2**(5*x))**2

plt.subplot(1, 3, 1)
plt.loglog(x, f, label="f(x)")
plt.legend()

plt.subplot(1, 3, 2)
plt.semilogy(x, g, label="g(x)")
plt.legend()

plt.subplot(1, 3, 3)
plt.semilogy(x, h, label="h(x)")
plt.legend()

plt.show()
