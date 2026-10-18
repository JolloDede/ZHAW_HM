import matplotlib.pyplot as plt
import numpy as np

schritte = 20

def calc_x_werte(a):
    x_werte = np.zeros(schritte + 1)
    k = 0.1
    x_werte[0] = k
    for i in range(schritte):
        k = a * k * (1 - k)
        x_werte[i + 1] = k
    return x_werte


x_05 = calc_x_werte(0.5)
x_15 = calc_x_werte(1.5)
x_25 = calc_x_werte(2.5)
x_30 = calc_x_werte(3)
x_38 = calc_x_werte(3.8)

plt.grid()
plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.plot(range(schritte+1), x_05, label="f(0.5)")
plt.plot(range(schritte+1), x_15, label="f(1.5)")
plt.plot(range(schritte+1), x_25, label="f(2.5)")
plt.plot(range(schritte+1), x_30, label="f(3)")
plt.plot(range(schritte+1), x_38, label="f(3.8)")
plt.legend()

plt.show()

# a) für alle Werte < 1 gehen die Werte irgendwann gegen 0
# Für alle Werte ]1, 3[ konvergieren auf einen bestimmten werte
# Für Werte [3, 3.5[ osziliert es um einen Punkt
# Ab 3.5 wird es chaotisch
# b) Ein Fixpunkt entstehen, wenn das System in volkommene Balance gerät
# c) $k = 1 - 1 / a$ Die Werte werden sich in diesem Bereich sammeln bei Aufgabe a wird beschrieben wie sich die Werte verhalten wenn sie diesen Punkt erreichen
