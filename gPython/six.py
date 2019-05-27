#

fib = [0,1]
num = int(input("请输入一个数值："))
for n in range(2,num):
    fib.append(fib[n-2]+fib[n-1])

print(fib)
