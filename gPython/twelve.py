#
"""Q12:判断101-200之间有多少个素数，并输出所有素数。 """
import math
count = 0
flag = 0
siglelist = []
for s in range(101,201):
    for n in range(2,int(math.sqrt(s)+1)):
        if s%n == 0:
            flag=1
    if flag == 0:
        count +=1
        siglelist.append(s)
    else:
        flag=0

print("一共有%d个素数"%count)
print(siglelist)
