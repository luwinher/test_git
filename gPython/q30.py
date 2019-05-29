#
"""Q30:一个5位数，判断它是不是回文数。"""

def calc(num):
    rnum = 0
    while(num):
        rnum = rnum*10+num%10
        num //= 10
    return rnum

num = int(input("请输入一个回文数: "))
rnum = calc(num)
if rnum == num:
    print("%d是一个回文数"%num)
else:
    print("%d不是一个回文数"%num)
