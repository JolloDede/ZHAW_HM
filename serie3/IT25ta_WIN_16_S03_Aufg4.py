import matplotlib.pyplot as plt
import numpy as np

# Bei x = 1.1 ist 100x^2 + 99 = 220 und 200x = 220. Wenn diese beiden Zahlen subtrahiert werden, bleibt nur noch der Rundungsfehler übrig.
# = ist ungefähr im Text oben
def aufgabe_a():
    x = 1.1
    left = 100 * x**2 + 99
    right = 200 * x
    res = left - right
    print(left)
    print(right)
    print(res)

def aufgabe_b():
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")

    step = 10**-7
    x = np.arange(1.1 + step, 1.3, step)
    zaehler = x * (100*x - 100)
    nenner = 100*x**2 - 200*x + 99
    f1 = np.abs(zaehler / nenner)

    plt.semilogy(x, f1, label="f1(x)")

    plt.legend()
    plt.show()

print("welche teilaufgabe wollen sie ausführen")
aufgabe = input()

match aufgabe:
    case 'a':
        aufgabe_a()
    case 'b':
        aufgabe_b()

# c nein die Auslöschung kann nicht vermieden werden, da die Konditionszahl gegen unendlich tendiert bei 1.1, dies bedeuete selbst durch algebraische Umformungen kann es nicht vermieden werden
