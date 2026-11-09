import numpy as np
from IT25ta_WIN_16_S06_Aufg2 import Name_S06_Aufg2

tasks = [ 

    ('A1', [[4, -1, -5], 
            [-12, 4, 17], 
            [32, -10, -41]], [-5, 19, -39]),

    ('A1_2', [[4, -1, -5], 
            [-12, 4, 17], 
            [32, -10, -41]], [6, -12, 48]),

    ('A2', [[2, 7, 3], 
            [-4, -10, 0], 
            [12, 34, 9]], [25, -24, 107]),

    ('A2_2', [[2, 7, 3], 
            [-4, -10, 0], 
            [12, 34, 9]], [5, -22, 43]),

    ('A3', [[-2, 5, 4], 
            [-14, 38, 22], 
            [6, -9, -27]], [1, 40, 75]),

    ('A3_2', [[-2, 5, 4], 
              [-14, 38, 22], 
              [6, -9, -27]], [16, 82, -120]),

    ('A4', [[-1,  2,  3,  2,  5,  4,  3, -1],
            [ 3,  4,  2,  1,  0,  2,  3,  8],
            [ 2,  7,  5, -1,  2,  1,  3,  5],
            [ 3,  1,  2,  6, -3,  7,  2, -2],
            [ 5,  2,  0,  8,  7,  6,  1,  3],
            [-1,  3,  2,  3,  5,  3,  1,  4],
            [ 8,  7,  3,  6,  4,  9,  7,  9],
            [-3, 14, -2,  1,  0, -2, 10,  5]], [-11, 103, 53, -20, 95, 78, 131, -26]),
]

for t in tasks:
    name, mat, b = t
    print("------")
    print(name)
    A = np.array(mat, dtype=np.float64)
    A_triangle, detA, our_solution =  Name_S06_Aufg2(A, b)
    numpy_solution = np.linalg.solve(mat, b)
    print("our solution: ", our_solution)
    print("numpy solution: ", numpy_solution)

    print("equal: ", np.allclose(our_solution, numpy_solution))

#Nein, es gibt keine Unterschiede