#语句嵌套示例

#接受用户输入
height = float(input ("请输入您的身高【CM】"))

vip_lever = int(input ("请输入您的VIP等级 1-4级"))

#代码判断，依次判断，第一条不满足，也会进入第二条...，停留在满足条件的位置
if height  >120:
    print(f"身高{height}，不能免费进入")  #第一层缩进Tab键
    print("如果您的VIP等级2以上可以免费游玩")
    if vip_lever >=2:
        print(f"您的VIP是{vip_lever},可以免费进入")   #第二层缩进Tab键
    else:   #以上都不满足才会进入此条件判断
        print("您需要补票10元")
else:    #需要全部满足以上if条件才会进入此步
    print("欢迎您的到来")