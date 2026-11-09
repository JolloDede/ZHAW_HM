import numpy as np
from IT25ta_WIN_16_S06_Aufg2 import Name_S06_Aufg2

# Aufg a)

x = [1997, 1999, 2006, 2010]
y = [150, 104, 172, 152]
offset = x[0]

# make 1997 => 0 etc.
x = [i - offset for i in x]

deg = 3
n = deg + 1

A = np.zeros([n, n])

for i in range(n):
    for j in range(len(x)):
        A[i, j] = x[i]**(deg - j)

_, _, s = Name_S06_Aufg2(A, y)

import matplotlib.pyplot as plt

plt.xlim()
plt.ylim()
plt.grid()

plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.title("Bild")

for i in range(len(x)):
    plt.scatter(x[i] + offset, y[i])

p = np.poly1d(s)

s2 = np.polyfit(x, y, deg)
p2 = np.poly1d(s2)

xPlot = np.linspace(1996, 2011, 150)
yPlot = p(xPlot - offset)
y2Plot = p2(xPlot - offset)

plt.plot(xPlot, yPlot)
plt.plot(xPlot, y2Plot)

plt.legend()
plt.show()


#Aufg b)

print("our guess")
print("2003: ", np.polyval(s, 2003 - offset))
print("2004: ", np.polyval(s, 2004 - offset))

print("polyfit guess")
print("2003: ", np.polyval(s2, 2003 - offset))
print("2004: ", np.polyval(s2, 2004 - offset))
