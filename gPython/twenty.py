#
""" Q20:一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？ """
ncount = float(input("请输入下落的次数: "))
sm1 = 0
count = 0
high = 100.0
while(high):
    count += 1
    sm1 += high
    high /= 2
    print("第%d次降落，共经过了%f米,即将反弹%f米" % (count,sm1,high))
    sm1 += high
    if count == ncount:
        break
