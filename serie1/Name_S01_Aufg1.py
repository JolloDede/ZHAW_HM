import matplotlib.pyplot as plt
import numpy as np

plt.xlim()
plt.ylim()
plt.grid()

plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.title("Bild")

x = np.linspace(-10, 10, 400)
y = x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105
yab = 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29
yst = 1/6*x**6 - x**5 - 30/4*x**4 + 110/3*x**3 + 29/2*x**2 - 105*x

plt.plot(x, y, label="f(x)")
plt.plot(x, yab, label="f'(x)")
plt.plot(x, yst, label="F(x)")

plt.legend()
plt.show()
