#
"""Q23:利用循环打印菱形."""
num = int(input("输入行数："))

for row in range(num):
    for lie in range(num-row):
        print(' ',end='')
    for star in range((row*2+1)):
        print('*',end='')
    print()

for row in range(num+1):
    for lie in range(row):
        print(' ',end='')
    for star in range((2*(num-row)+1)):
        print('*',end='')
    print()
