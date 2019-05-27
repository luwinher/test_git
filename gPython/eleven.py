#
"""Q11:古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ """
rabbitcount = list()
month = input("请输入月数：")
rabbit = [1,0,0]
for m in range(1,int(month)+1):
#    print("%d\t%d,%d,%d" % (m,rabbit[0],rabbit[1],rabbit[2]))
    rabbitcount.append(rabbit[0]+rabbit[1]+rabbit[2])
    rabbit[2]=rabbit[2]+rabbit[1]
    rabbit[1]=rabbit[0]
    rabbit[0]=rabbit[2]
print(rabbitcount)
