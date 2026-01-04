#郑骰子游戏为系统随意生成的1-6的数字
#三个数相等为豹子，两个相等为双子，三个数不一样为单数，连顺为顺子（如：123,345...）
#引入系统随意生成命令
import random  # 系统命令

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)
num3 = random.randint(1, 6)
max_num = 0
mi_num = 0
# 判断出最大值
if num1 > num2 and num1 > num3:
    max_num = num1
elif num2 > num1 and num2 > num3:
    max_num = num2
else:
    max_num = num3

# 判断出最小值
if num1 < num2 and num1 < num3:
    mi_num = num1
elif num2 < num1 and num2 < num3:
    mi_num = num2
else:
    mi_num = num3
# 判断结果
if num1 == num2 == num3:
    print(f"数字{num1},{num2},{num3}，为豹子")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print(f"数字{num1},{num2},{num3}，为双子")
elif max_num - mi_num == 2:
    print(f"数字{num1},{num2},{num3}，为顺子")
else:
    print(f"数字{num1},{num2},{num3}，为单子")
