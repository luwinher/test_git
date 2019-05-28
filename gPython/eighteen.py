#
"""Q18:求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。 """

import random,math
r = random.randint(1,9)
num = input("请输入一个数值:")
sum = 0
rsum = 0
for n in range(0,int(num)+1):
    rsum += pow(10,n)*r
#    print(rsum)
    sum += rsum

print(sum)
