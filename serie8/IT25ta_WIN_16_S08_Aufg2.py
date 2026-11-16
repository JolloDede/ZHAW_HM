import numpy as np
import timeit

# Aufg a)

def IT25ta_WIN_16_S08_Aufg2(A):

    A = np.copy(A)
    A = A.astype('float64')

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise 'Non square matrix!'

    Q = np.eye(n)
    R = A

    for j in range(0, n-1):
        a = np.copy(R[j:, j]).reshape(n-j, 1)
        e = np.zeros(n-j).reshape(n-j, 1)
        e[0] = 1.
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = v / np.linalg.norm(v)
        H = np.eye(n-j) - 2 * (u @ u.T)
        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = Qi @ R
        Q = Q @ Qi.T

    return(Q, R)


# Aufg b)

A = np.array([[1, -2, 3],
              [-5, 4, 1],
              [2, -1, 3]])
b = np.array([1, 9, 5])

Q, R = IT25ta_WIN_16_S08_Aufg2(A)
print("Q = \n", Q)
print("R = \n", R)

# Rx = Q^T b, rückwärts einsetzen
y = Q.T @ b
n = len(y)
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    sum = 0
    for j in range(i + 1, n):
        sum += R[i, j] * x[j]
    x[i] = (y[i] - sum) / R[i, i]

print("x = ", x)


# Aufg c)

t1 = timeit.repeat(lambda: IT25ta_WIN_16_S08_Aufg2(A), number=100)
t2 = timeit.repeat(lambda: np.linalg.qr(A), number=100)
avg_t1 = np.average(t1)/100
avg_t2 = np.average(t2)/100

print("3x3 eigene: ", avg_t1)
print("3x3 numpy:  ", avg_t2)


# Aufg d)

Test = np.random.rand(100, 100)

t1 = timeit.repeat(lambda: IT25ta_WIN_16_S08_Aufg2(Test), number=100)
t2 = timeit.repeat(lambda: np.linalg.qr(Test), number=100)
avg_t1 = np.average(t1)/100
avg_t2 = np.average(t2)/100

print("100x100 eigene: ", avg_t1)
print("100x100 numpy:  ", avg_t2)

# Kommentar:
# Bei der 3x3 Matrix ist numpy etwa 2x schneller, bei der 100x100 Matrix etwa 20x.
# Je grösser n wird, desto grösser wird der Unterschied. 
# numpy.linalg.qr() verwendet offensichtlich einen besseren Algorithmus mit einer tieferen Zeitkomplexität
