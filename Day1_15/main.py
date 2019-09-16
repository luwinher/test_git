import module1 as m

if __name__ == "__main__":
    num = int(input("Please input a number: "))
    if m.is_palindrome(num) and m.is_prime(num):
        print("%d is a palindrome and prime number."% num)
    a = int(input("Please input 2 number: "))
    b = int(input())
    print("%d and %d gcd is %d, lcm is %d." % (a, b, m.gcd(a, b), m.lcm(a, b)))

