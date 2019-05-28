#
"""Q24:有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""

fib = [1,2]
sum1 = 0
for n in range(2,21):
    fib.append(fib[n-1]+fib[n-2])
    sum1 += fib[n-1]/fib[n-2]
#    print("%d/%d"%(fib[n-2],fib[n-1]))
sum1 += fib[-1]/fib[-2]
print(fib)
print(sum1)
