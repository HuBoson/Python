# 系统生成一个数字，得到大于5的数字员工享有奖金领取
# import random    #系统生成的kpi变量
# monye = 10000   #总金额1万元
# for i in range(1,21):  #共有20个员工
#     kpi = random.randint(1, 10)
#     if kpi > 5:   #kpi大于5以上，才能领奖金
#         continue   #KPI小于5的不发，继续往下循环
#     monye -= 1000  #每次减一次总额，每次发放=1000元，理解“-=”的意思
#     print(f"给第{i}号员工发送1000元，还剩{monye}")
#     if monye <= 0:  #账号没有钱了
#         print ("本次奖金发送完毕！")
#         break    #用break退出循环


# while和for循环综合使用
# 两个的区别在于：在不知道需要的循环的次数下，使用while做循环时，但需要控制循环递增。

import random
x = True
monye = 10000  #注意总变量可以在循环外，放在while循环内也可以
while x:
    for i in range(1,21):
        kpi = random.randint(1,10)
        if kpi < 5:
            continue
        monye -= 1000
        print(f"第{i}号员工已经领取1000元，还剩{monye}元")
        if monye <1000:  #注意此处缩进，如果与for平齐，就表示在for循环外，就会出现要循环20次才结束
            x = False  #注意while循环需要此处来判断是否结束，否则会不停止的循环
            break  #此处结束循环，
print ("本月工资发放完毕！")



