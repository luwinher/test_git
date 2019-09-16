#!/home/winher/ENV36/bin/python
#

"""
        [ 3x-5 (x >1)
 f(x) = [ x +2 (-1 <= x <= 1)
        [ 5x+3 (x < -1)

"""
x = int(input("Please input value x: "))

if x > 1:
    print((3*x-5))
elif x >= -1:
    print((x+2))
else:
    print((5*x+3))
