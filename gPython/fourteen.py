#
"""Q14:将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。 """
import math
number = input("请输入一个数：")
num = int(number)
def prime(num):
    flag = 0
    primelist = list()
    for n in range(2,num+1):
        for s in range(2,n):
           # print("%d,%d"%(n,s))
            if n%s==0:
                flag=1
                break
       #print(flag)
        if flag==0:
            primelist.append(n)
        else:
            flag=0
    return primelist

primes = prime(num)
#print(primes)
nflag = 1
numlist = list()
while(num!=1 and primes):
    for i in primes:
        if num%i==0:
            numlist.append(i)
            num = num/i
            nflag = 0
#print(numlist)
if numlist[-1]==int(number):
    print("%d=%d*%d"%(int(number),1,int(number)))
else:
    numlist.sort()
    numlist.reverse()
    print("%d="%int(number),end='')
    nx = numlist.pop()
    print(nx,end='')
    while(numlist):
        print("*",end='')
        nx = numlist.pop()
        print(nx,end='')
    
print()

