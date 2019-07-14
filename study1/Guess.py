#!/user/bin/env python

"""
age = 23
count = 0
while count < 3:
    guessAge = int(input("猜猜我多大？\n"))
    if age == guessAge:
        print("恭喜你猜对了")
        break
    elif age > guessAge:
        print("猜小了，请重新再猜")
    else:
        print("猜大了，请重新再猜")
    count+=1
else:
    print("你已猜测太多次了，请明天再猜")
"""
"""
age = 23
for count in range(3):
    guessAge = int(input("猜猜我多大？\n"))
    if age == guessAge:
        print("恭喜你猜对了")
        break
    elif age > guessAge:
        print("猜小了，请重新再猜")
    else:
        print("猜大了，请重新再猜")
else:
    print("你已猜测太多次了，请明天再猜")
"""

import os
import os.path

rootDir = "C:\\Users\HL_913305160\Desktop\python.txt"
fileHandler = open(rootDir)
status = fileHandler.readline()
if status == "锁定":
    print("当前状态已被锁定")
    fileHandler.close()
else:
    _name = "张磊"
    _password = 19960102
    for count in range(3):
        name = input("请输入用户名：")
        password = int(input("请输入你的密码："))
        if _name == name and _password == password:
            print("登录成功！")
            break
        else:
            print("你输入的用户名或者密码有误，请重新输入")
    else:
        print("你已输错太多次了，当前状态被锁定")
        fileHandler = open(rootDir, 'w')
        fileHandler.writelines("锁定")
        fileHandler.close()
