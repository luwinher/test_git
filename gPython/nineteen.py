#
""" Q19:一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。 """

def findfactor():
    for num in range(2,1001):
        number = num
        factor = [1]
        sum1 = 0
        for n in range(2,num+1):
            if num%n == 0:
                num /= n
                factor.append(n)
        for nl in factor:
            sum1 += nl
        if sum1 == number:
            print(number)

findfactor()

