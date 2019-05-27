#
""""""
num=[1,2,3,4]
list1 = []
list2 = []
for i in num:
    for j in num:
        if i==j:
            continue
        else:
            for k in num:
                if i==k or j==k:
                    continue
                else:
                    list1.append(i*100+j*10+k)
for n in list1:
    if n not in list2:
        list2.append(n);

print(list2)
