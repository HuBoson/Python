#用户系统输入数字大小，并提示输入的数字过大或过小，循环猜中为止

import random  #系统自动生成对的数字
num = random.randint(1,10)
count = 0  #设置一个次数变量
while True:
    user_num = int (input("请输入一个1-10的数字"))
    count += 1  # +1为每输入一次的计数
    if user_num >num:
        print("您输入的数字太大了")
    elif    user_num < num:
        print("您输入的数字太小了")
    else:
        print ("恭喜您！猜中了")
        print(f"您总共猜了{count}次")
        break   #注意此处缩进，如果平齐if，没有猜完游戏就结束了，这个缩进应该平齐内循环结构内容