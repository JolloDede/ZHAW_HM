import numpy as np

def WIN_16_S05_Aufg3(f, x0, x1, tol):
    fx0 = f(x0)
    fx1 = f(x1)
    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    print(x2)
    if np.abs(x1 - x2) < tol:
        return x2
    else:
        return WIN_16_S05_Aufg3(f, x1, x2, tol)


def aufgabe_1(x):
    return np.exp(x**2) + x**-3 - 10

def aufgabe_2(h):
   return (np.pi / 3) * h**3 - 5 * np.pi * h**2 + 471

print("Ergebniss: ", WIN_16_S05_Aufg3(aufgabe_1, -1, -1.2, 0.001))
print("Ergebniss: ", WIN_16_S05_Aufg3(aufgabe_2, 9, 7.65851, 0.001))

# Ich denke, dass durch das aufschreiben der Nullstellen beim ausrechnen von Hand viele Ungenauigkeiten entstanden sind, welshalb die Ergebnisse abweichen

# Beim Newton Verfahren, wenn die Steigung 0 wird dann teilen wir durch 0 was nicht geht.
