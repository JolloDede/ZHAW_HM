import numpy as np

def fact_rec(n):
    # y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
    # Fehler, falls n < 0 oder nicht ganzzahlig
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)

def fact_for(n):
    prod = n
    for i in range(1, n):
           prod *= i
    return prod

import timeit

t1 = timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
t2 = timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)

print("average rec: ", np.average(t1))
print("average for: ", np.average(t2))

# For ist schneller da keine FunctionCallStack aufgebaut werden muss

# Limit für integer gibt es nicht das int so gross sein kann wie das Memory zulässt
# Das Printen von int hat jedoch eine Grenze von 4300 Zeichen die umgewandelt werden können
# Ja weil die 11 bit, des Exponenten, bei 171 überschritten werden
