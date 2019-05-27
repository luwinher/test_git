#
"""Q8:输出 9*9 乘法口诀表。 """
for i in range(1,9):
    for j in range(1,9):
        if i >= j:
            print(("%d * %d = %d" % (j,i,i*j)),end=' ')
    print()
