#数据录入 input（“提示语”）
print("欢迎来到xx银行！")
pwd = input ("请输入您的取款密码")
print("您的密码是%s"% pwd)  #注意：所有从键盘输入的数据都为字符串，所以此处的格式化符号为%s
print(type(pwd))


#练习：欢迎登录小程序

user_name= input("请输入您的用户名称：")
user_type =input("请输入您的用户类型：")
user_pwd = input("请输入您的密码：")
#格式化输出
print("用户名称%s,类型%s,密码%s"%(user_name,user_type,user_pwd))