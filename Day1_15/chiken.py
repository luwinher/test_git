#!/home/winher/ENV36/bin/python
#

for y in range(1, 20):
    x = (200-14*y)/8
    s = (200-14*y)%8
    if s == 0 and x >= 0:
        print("Father C:%d, Mother C:%d, Kid C:%d" % (y, x, (100-x-y)))
