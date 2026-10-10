import matplotlib.pyplot as plt
import numpy as np

def aufgabe_a():
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")

    x = np.linspace(0.5, 1.5, 100)
    f1 = np.sqrt(100*x**2 - 200*x + 99)

    plt.plot(x, f1, label="f1(x)")

    plt.legend()
    plt.show()
    # Für werte zwischen 0.9 and 1.1 gibt es Werte von denen man keine sqrt ziehen kann und deshalb ist die Funktion in diesem Bereich nicht definiert

def aufgabe_b():
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")

    step = 10**-7
    x = np.arange(1.1 + step, 1.3, step)
    zaehler = 100*x - 200
    nenner = np.sqrt(100*x**2 - 200*x + 99)
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
