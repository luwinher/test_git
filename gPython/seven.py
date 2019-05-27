#
r = list(range(0,100))
a = [ x for x in r if x%3 is 0]
print(a)
#b = a[:]
b = a
a.append(100)
print(b)
