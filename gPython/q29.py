#
"""Q29:给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。"""

def calc(num):
    nnum = num
    rnum = 0
    count = 0
    while(num):
        rnum = rnum*10 + num%10
        num = num//10
        count += 1
    print("%d是一个%d位数，其逆序是%d"%(nnum,count,rnum))

num = input("请输入一个不多于5位的数字: ")
calc(int(num))
