import matplotlib.pyplot as plt
import numpy as np

def aufgabe_a():
    plt.xlim()
    plt.ylim()
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")
    plt.title("Bild")

    x = np.linspace(1.99, 2.01, 501)
    # x = np.linspace(1.99, 2.01, 2)
    # x = np.linspace(-10, 10, 400)
    # Bei dieser Funktion treten immer wieder Rundungsfehler auf. Die akkumulierten Rundungsfehler lösen vor allem in kleinen Intervallen grosse Unterschiede aus
    f1 = x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128
    f2 = (x - 2)**7

    plt.plot(x, f1, label="f1(x)")
    plt.plot(x, f2, label="f2'(x)")

    plt.legend()
    plt.show()
    # Die beiden Funktionen sind faktisch gleich beim interpertieren des Computer wird jedoch nicht die gleiche Interpretation verwendet. Die Funktion f2 lässt sich vom Computern, für kleine Intervalle, genauer berechnen als f1.

def aufgabe_b():
    plt.xlim()
    plt.ylim()
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")
    plt.title("Bild")

    x = np.arange(-10e-14, 10e-14, 10e-17)
    f1 = np.divide(x, np.sin(1 + x) - np.sin(1))
    # KI gefragt wie der Grenzwert wirklich aussehen würde
    f2 = np.divide(x, 2 * np.cos(1 + x / 2) * np.sin(x / 2))

    plt.plot(x, f1, label="f1(x)")
    plt.plot(x, f2, label="f2(x)")

    plt.legend()
    plt.show()
    # Nein die berechunung ist instabil
    # Umso näher wir an die 0 gehen umso mehr Ungenauigkeiten treten auf

def aufgabe_c():
    print()

print("welche teilaufgabe wollen sie ausführen")
aufgabe = input()

match aufgabe:
    case 'a':
        aufgabe_a()
    case 'b':
        aufgabe_b()
    case 'c':
        aufgabe_c()
