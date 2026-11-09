import numpy as np

def FlipRows(A, i):
    num_rows, _ = A.shape;
    
    for r in range(i, num_rows):
        if (A[r, i] != 0):
            A[[i, r]] = A[[r, i]]
            return A
    raise 'Matrix not solvable :('


def Name_S06_Aufg2(A, b):
    row_count, col_count = A.shape
    if row_count != col_count:
        raise 'Non square matrix!'

    #dreieck
    A = np.c_[A, b]
    n = row_count

    for i in range(0, n - 1):
        A = FlipRows(A, i)
        a = A[i, i]

        for j in range(i + 1, n):
            b = A[j, i]
            multiply = b / a
            A[j] -= A[i] * multiply


    #solve up
    x = np.array(np.ones(n))

    for i in range(n - 1, -1, -1):
        divisor = A[i, i]
        sum = 0;
        for j in range(i + 1, n):
            sum += A[i, j] * x[j]
        x[i] = (A[i, n] - sum) / divisor

    # determinant
    det = 1
    for i in range(0, n):
        det *= A[i, i]

    return A, det, x
