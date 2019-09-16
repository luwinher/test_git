#
def main():
    str1 = "hello, world!"
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('or'))
    print(str1.find("shit"))
    try:
        print(str1.index('or'))
        print(str1.index('sh'))
    except ValueError:
        pass
    print(str1.startswith('He'))
    print("startswith(hel): "+str(str1.startswith('hel')))

    print("endswith(!): "+str(str1.endswith('!')))
    print("cneter: " + str1.center(50, '*'))
    print("Rjust: " + str1.rjust(50, " "))
    str2 = "abcd123456"
    print("str2[2]: " + str2[2])
    print(str2[2:5])
    print(str2[2:])
    print(str2[2::2])
    print(str2[::2])
    print(str2[::-1])
    print(str2[-3:-1])
    print(str2.isdigit())
    print(str2.isalpha())
    print(str2.isalnum())
    str3 = '   jackfrued@126.com '
    print(str3)
    print(str3.strip())

if __name__ == '__main__':
    main()
