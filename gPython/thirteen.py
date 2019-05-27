#
"""Q13:打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。 """
import math

for n in range(100,1000):
    sum1 = math.pow((n//100),3) + math.pow((n%100//10),3) + math.pow((n%10),3)
    #print("%d\t%d" % (n,sum1))
    if n == sum1:
        print(n)
"""
n = 123
print(n//100)
print(n%100//10)
print(n%10)
if 16 == 16.0:
    print("ok")
"""
