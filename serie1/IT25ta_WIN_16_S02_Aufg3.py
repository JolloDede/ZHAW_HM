import matplotlib.pyplot as plt
import numpy as np

def calc_sum_instabil(n, s_n):
    n_werte = []
    umfang_werte = []
    for _ in range(30):
        n_2n = 2 * n

        # der Term wird bei kleineren s_n, wegen der beschränkung auf 64 bit, irgendwann = 0
        term = (s_n**2) / 4.
        # der ganze term wird somit 1
        term = 1. - term
        # s_2n wird zu 2 - 2 * 1 und somit = 0
        s_2n = np.sqrt(2. - 2. * np.sqrt(term))

        umfang = n_2n * s_2n

        n_werte.append(n_2n)
        umfang_werte.append(umfang)

        n = n_2n
        s_n = s_2n
    return n_werte, umfang_werte

def calc_sum_stabil(n, s_n):
    n_werte = []
    umfang_werte = []
    for _ in range(30):
        n_2n = 2 * n

        s_n2 = (s_n**2)
        term = 1. - s_n2 / 4.
        nenner = 2 * (1 + np.sqrt(term))
        s_2n = np.sqrt(s_n2 / nenner)

        umfang = n_2n * s_2n

        n_werte.append(n_2n)
        umfang_werte.append(umfang)

        n = n_2n
        s_n = s_2n
    return n_werte, umfang_werte

plt.figure(figsize=(10, 6))
n = 6
s_n = 1
n_werte, umfang_werte  = calc_sum_instabil(n, s_n)

plt.plot(n_werte, umfang_werte, label="f1(x)")

# mit der stabilen berechnung nähern wir uns immer weiter dem Wert von 2 * PI an
n = 6
s_n = 1
n_werte, umfang_werte  = calc_sum_stabil(n, s_n)
plt.plot(n_werte, umfang_werte, label="f2(x)")

plt.axhline(2 * np.pi, linestyle='--', label=f'Exakter Wert (2*pi ≈ {2*np.pi:.5f})')
# um besser zu sehen wann die Werte 0 werden
# plt.xscale('log')
plt.xlim()
plt.ylim()
plt.grid()
plt.xlabel("X Achse")
plt.ylabel("Y Achse")
plt.title("Bild")
plt.legend()
plt.show()
