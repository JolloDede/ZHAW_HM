import matplotlib.pyplot as plt
import numpy as np

def aufgabe_a_1():
    plt.xlim()
    plt.ylim()
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")

    x = np.linspace(0, 100, 1000)
    c = 1
    a = 2
    f1 = c * a**x
    f2 = c * x**a

    plt.plot(x, f1, label="f_exp(x)")
    plt.plot(x, f2, label="f_pot(x)")

    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

def aufgabe_a_2():
    plt.xlim()
    plt.ylim()
    plt.grid()

    plt.xlabel("X Achse")
    plt.ylabel("Y Achse")

    x = np.linspace(0, 100, 1000)
    f = 5 / (2*x**2)**(1/3)
    g = 10**5 * (2 * np.e)**(-x/100)
    h = (10**(2*x) / 2**(5*x))**2

    plt.plot(x, f, label="f(x)")
    plt.plot(x, g, label="g(x)")
    plt.plot(x, h, label="h(x)")

    # plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

print("welche teilaufgabe wollen sie ausführen")
aufgabe = input()

match aufgabe:
    case 'a1':
        aufgabe_a_1()
    case 'a2':
        aufgabe_a_2()
