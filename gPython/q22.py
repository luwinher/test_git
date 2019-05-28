#
"""Q22:两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。 """
allsit = dict() 
jia = ['a','b','c']
yi = ['x','y','z']

def comb(i,j,k):
    T1 = jia[0]+yi[i]
    T2 = jia[1]+yi[j]
    T3 = jia[2]+yi[k]
    return tuple([T1,T2,T3])
arr = list()
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i==j) or (i==k) or (j==k):
                continue
            arr.append(comb(i,j,k))
#print(arr)
for g in arr:
    if ('ax' in g) or ('cx' in g) or ('cz' in g):
        continue
    print(g)
