import numpy as np

def Name_S09_Aufg2(A, A_g, b, b_g):
    x = np.linalg.solve(A, b)
    x_g = np.linalg.solve(A_g, b_g)

    rel_abweichung_A = np.linalg.norm(A - A_g, ord=np.inf) / np.linalg.norm(A, ord=np.inf)
    cond_A = np.linalg.cond(A, np.inf)

    if cond_A * rel_abweichung_A < 1:
        rel_abweichung_b = np.linalg.norm(b - b_g, ord=np.inf) / np.linalg.norm(b, ord=np.inf)
        term1 = cond_A / (1 - cond_A * rel_abweichung_A)
        term2 = rel_abweichung_A + rel_abweichung_b
        dx_max = term1 * term2
    else:
        dx_max = np.nan

    dx_obs = np.linalg.norm(x - x_g, ord=np.inf) / np.linalg.norm(x, ord=np.inf)

    return [x, x_g, dx_max, dx_obs]