# 统计班级平均分

all_score = 0  # 年级总分变量设定
for x in range(1, 3):  # 从2个班学生统计
    y_score = 0  # 班级总分变量设定
    for y in range(1, 4):  # 每个班3名同学
        score = int(input(f"请输入{x}班，编号为{y}的个人分数"))  # 输入个人分数
        y_score += score  # 所有输入个人总分等于班级总分，注意写法
    print(f"第{x}班的总分是{y_score},班的平均分是{y_score / 3}")
    all_score += y_score  # 注意此处缩进，在外循环内， 所有班级总分等于年级总分，注意写法
print(f"全年级总分是{all_score},平均分是%.2f" % (all_score / 6))  # 注意此处与小数后两位的写法
