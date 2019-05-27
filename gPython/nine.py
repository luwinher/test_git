#
"""Q9:模拟Linux用户登录。 """
import os
name = input("请输入用户名：")
flag = os.system("su - "+name)
if flag == 0:
    os.system('exit')
    print("登录成功")
else:
    os.system('sleep 3s')
    print("登录失败")
