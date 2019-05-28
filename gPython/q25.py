#
""" Q25: 求1+2!+3!+...+20!的和。 """
factorial = 1
sum1 = 0
for s in range(1,21):
#    for f in range(1,s+1):
#        factorial
    factorial *= s
    sum1 += factorial
    print("%d,%d"%(factorial,sum1))
