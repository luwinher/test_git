#

"""q26:利用递归方法求5!。 """
def flator(n):
    if n==1:
        return 1
    return flator(n-1)*n

print(flator(5))
