#if语句的使用
#在条件判断中必须使用==进行比较，如果错误地使用=会导致语法错误，因为=是赋值运算符而不是比较运算符
#判断输入的年龄是否成年

print("欢迎来到迪士尼游乐园")
age= int(input("请输入您的年龄"))   #变量必须转换成int数字
#判断
if age>=18:   #数字后面必须有冒号，且必须是布尔类型，赋值，条件为True
    print ("您的年龄是%d"%age,"收费50元")    #条件满足后，语句，前面用Tab键空格缩进表示在if语句内这行的代码，当判断结果为True时才会执行
else:   #需要冒号分行，不满足条件时，需换行执行False结果
    print(f"您的年龄{age},可以免费进入游玩")
print("谢谢使用")    #此行顶格表示不在if语句内执行的代码

#多重判断示例：if条件会从第一个开始依次确定执行前面的代码命令
#接收用户输入
age = int(input("请输入您的年龄"))
height = float(input("请输入您的身高"))
vip = int(input("请输入您的VIP 【1-4】等级"))
if age <=18:
    print(f"您的年龄是{age},可以免费游玩")
elif height <=120:   #从上往下依次判断表达式，只有第一个满足条件的if或elif块会被执行，后续的条件不再判断。
    print("您的身高小于120【CM】，可以免费游玩")
elif vip>=2:
    print(f"您是VIP{vip}")
else:
    print ("您需要付费100元")

#密码输入练习
keyword = 123
#以下是用户输入提示
if int (input("请您输入密码")) == keyword:
    print("您输入的密码正确")
elif int(input("请再一次输入密码"))==keyword:
    print("恭喜您密码正确")
else:
    print ("您输入密码错误，请重新输入")