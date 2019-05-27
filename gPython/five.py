#

numstr = input("请输入3个数字: ")
numlist = numstr.split()
numlist.sort()
for n in numlist:
    print(int(n))
