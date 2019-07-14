#!/user/bin/env python
import getpass

_userName = "张磊"
_password = 5201314
userName = input("用户名：")
password = int(getpass.getpass("密码："))
if _userName == userName and _password == password:
    print("用户{name}登录成功！".format(name = userName))
else:
    print("登录失败！")
