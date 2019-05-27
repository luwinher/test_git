#
import math

for n in range(10000):
    n1 = math.sqrt(n+100)
    n2 = int(n1)
    if (n1-n2) == 0:
        n3 = math.sqrt(n+268)
        n4 = int(n3)
        if (n3-n4) == 0:
            print( n)
