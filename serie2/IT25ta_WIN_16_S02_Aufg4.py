# exp = 1
# while 1. + (2**-exp) != 1:
#     exp += 1

# print(exp)

eps = 1.

while 1. + (eps / 2.) != 1.:
    eps = eps / 2.

print(eps, "= 2^53 * 2")

q_min = 1.

while 1. + q_min != q_min:
   q_min *= 2.

print(q_min, " = 2^53")

# eps wie auch q_min sind beides Werte die mit 2^53 gebildet werden können
# Sie brauche nur den Exponenten der Floatzahl
