import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0, 100, 1000)
# x = np.linspace(0, 100, 1000)
x_log = np.logspace(-2, 2, 1000)
x_lin = np.linspace(0.01, 100, 1000)
f = 5 / (2*x_log**2)**(1/3)
g = 10**5 * (2 * np.e)**(-x_lin/100)
h = (10**(2*x_lin) / 2**(5*x_lin))**2

plt.subplot(1, 3, 1)
plt.grid()
plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.loglog(x_log, f, label="f(x)")
plt.legend()

plt.subplot(1, 3, 2)
plt.grid()
plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.semilogy(x_lin, g, label="g(x)")
plt.legend()

plt.subplot(1, 3, 3)
plt.grid()
plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.semilogy(x_lin, h, label="h(x)")
plt.legend()

plt.show()
