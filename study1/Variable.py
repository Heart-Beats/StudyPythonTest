#!/user/bin/env python

'''
print("Hello World")
name = "张磊"
age ="23"
print("我的名字是"+name,"今年"+age+"岁")
'''

#print(input("你的名字是："))

name = input("姓名：")
age = input("年龄：")
info1 = '''--**--个人信息1 --**--
    姓名：'''+name +'''
    年龄：'''+ age
print(info1)

age = int(age)
info2 = '''--**--个人信息2 --**--
    姓名：%s
    年龄：%d'''%(name,age)
print(info2)

info3 = '''--**--个人信息3 --**--
​	姓名：{_name}
​	年龄：{_age}'''.format(_name = name,_age = age)
print(info3)

info4 = '''--**--个人信息4 --**--    
​	姓名：{0}
​	年龄：{1}'''.format(name,age)
print(info4)