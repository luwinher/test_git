#!/home/winher/ENV36/bin/python
#
"""
login auth
"""

import getpass

username=input("Please input Username: ")
#password=input("Please input Password: ")
password=getpass.getpass("Please input Password: ")

if username == 'admin' and password == '123456':
    print("It's OK")
else:
    print("It's Fail")
