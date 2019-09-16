#!/home/winher/ENV36/bin/python
#

def gcd(x, y):
    (x, y) = (x, y) if x < y else (y, x)
    for f in range(x, 0, -1):
        if x%f == 0 and y%f == 0:
            return f

def lcm(x ,y):
    return x * y // gcd(x, y)


def is_prime(num):
    if num >= 2:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
    else:
        return False

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //=10
    return total == num
