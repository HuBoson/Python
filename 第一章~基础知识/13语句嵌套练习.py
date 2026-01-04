#满足多个条件下的判断

#用户输入信息
# age= int(input ("请输入您的年龄"))
# if 18 <= age <= 40:    #ctrl+alt +L格式化
#     print("年龄满足要求")
#     rate_time = int (input ("请输入您的入职时长"))
#     lever = int(input("请输入您的级别"))
#     if rate_time >2 or lever >= 2:
#         print("恭喜您,可以领取")
#     else:
#         print ("不满足条件")
# else:
#     print ("年龄不满足")



#多嵌套的练习
# import random  #导入随机数模块功能，
# num = random.randint (1,10)#生成一个随机数
# user1 = int(input("请输入一个数字【1-10】"))
# if user1 != num:   #  !=为“不等于”的意思
#     if user1 > num:      #第一层子缩进
#         print("您猜的太大了")  #缩进量要大于if
#     else:           #第一层子缩进，与上一行if缩进量一样
#         print ("您猜的太小了")
#     print("请猜第二次")   #第一层子缩进，平齐上面if
#     user2 = int(input("请再次输入【0-10】的数字"))  #第二层缩进
#     if  user2 != num:  #第二层缩进
#         if user2 > num:   #第二层子缩进
#             print("您猜的太大了")
#         else:    #第二层子缩进，与上一行if缩进量一样
#             print("您猜的太小了")  #缩进量要大于if
#         print ("请猜第三次")
#
#         user3 =int (input("请再次输入一个【0-10】的数字"))
#         if user3 != num:  #第三层缩进
#             print(f"游戏结束！答案是{num}")
#         else :   #与if缩进一样，同层逻辑
#             print ("恭喜您第三次猜中了！！")
#     else:    #这行如果放在第二次猜的结果后面会影响后面的代码不能执行，因为层级比第三次猜的层级高一层
#         print("恭喜您第二次猜中了")
# else:
#     print ("恭喜您第一次就猜中了")

#判断年份，多公式连接的练习
# year = int(input("请输入年份"))
# #能被4整除，但不能被100整除，同时被400整除的公式
# if (year %4==0 and year %100!=0 or year %400==0):
#     print ("今年是润年")
# else:
#     print("今年是平年")
# print ("查询完毕！")


#电脑猜拳游戏
import random
user = int(input("请输入0石头，1剪刀，2布"))
computer = random.randint(0,2)
#以下采用多公式and 和 or连接
if (user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
    print ("用户赢了")
elif user == computer:
    print("平局")

else:
    print("电脑赢了")

