import numpy as np
import matplotlib.pyplot as plt
from IT25ta_WIN_16_S09_Aufg2 import Name_S09_Aufg2

dx_max_values = []
dx_obs_values = []
ratio_values = []

for i in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100)

    A_g = A + np.random.rand(100, 100) * 10**-5
    b_g = b + np.random.rand(100) * 10**-5

    [x, x_g, dx_max, dx_obs] = Name_S09_Aufg2(A, A_g, b, b_g)

    dx_max_values.append(dx_max)
    dx_obs_values.append(dx_obs)
    ratio_values.append(dx_max / dx_obs)

plt.semilogy(dx_max_values, label="dx_max")
plt.semilogy(dx_obs_values, label="dx_obs")
plt.semilogy(ratio_values, label="dx_max / dx_obs")

plt.xlabel("Iteration")
plt.ylabel("Relativer Fehler")
plt.legend()
plt.grid()
plt.show()

# Die dx_max Schranke ist um einiges zu gross, sie befindent sich ca. bei 10⁻1, aber dx_obs ist ca. 10⁻4. 
# Das Verhältnis ist bei ca. 10³, also ist die Schranke ca 1000x grösser als sie sein müsste.