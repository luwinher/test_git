#

for num in range(100,1000):
    if ((num//100)**3+((num%100)//10)**3+(num%10)**3) == num:
        print(num)
