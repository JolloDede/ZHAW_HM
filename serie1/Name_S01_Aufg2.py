import matplotlib.pyplot as plt
import numpy as np

def  plot_func_ab_u_stam(a, xmin, xmax):
    shape_a = np.shape(a)
    if len(shape_a) == 0 or shape_a[0] == 0:
        raise Exception('Fehler')

    if len(shape_a) == 1:
        a = np.array(a, dtype=float).flatten()
    elif len(shape_a) == 2:
        if shape_a[0] == 1:
            a = np.array(a, dtype=float).flatten()
        elif shape_a[1] == 1:
            a = np.array(a, dtype=float).flatten()
        else:
            raise Exception('Fehler')
    else:
        raise Exception('Fehler')

    x = np.linspace(xmin, xmax, 400)

    p = np.zeros_like(x, dtype=float)
    for coeff in a:
        p = p * x + coeff

    n = len(a) - 1
    if n == 0:
        da = np.array([0.0])
    else:
        powers_d = np.arange(n, 0, -1)
        da = a[:-1] * powers_d

    dp = np.zeros_like(x, dtype=float)
    for coeff in da:
        dp = dp * x + coeff

    powers_int = np.arange(n, -1, -1)
    divisors = powers_int + 1
    inta_high = a / divisors
    inta = np.append(inta_high, 0.0)

    pint = np.zeros_like(x, dtype=float)
    for coeff in inta:
        pint = pint * x + coeff

    return(x, p, dp, pint)

# Main
[x, y, yab, yst] = plot_func_ab_u_stam([1, 5, 30, 110, 29, 105], -10, 10)

plt.xlim()
plt.ylim()
plt.grid()

plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.title("Bild")

plt.plot(x, y, label="f(x)")
plt.plot(x, yab, label="f'(x)")
plt.plot(x, yst, label="F(x)")

plt.legend()
plt.show()
