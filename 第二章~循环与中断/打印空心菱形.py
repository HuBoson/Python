row = eval(input('请输入菱形的行数,需为基数:'))
while row%2==0:     # 判断行数的奇偶,行数是偶数,重新输入行数
    print('请重新输入菱形的行数:')   # 输入偶数时提示重新输入
    row=eval(input('输入菱形的行数:'))  # 当输入偶数时,控制无限循环
# 输出菱形
top_row=(row+1)//2   # 上半部分的行数,为奇数
# 上半部分
for i in range(1,top_row+1):   # 控制上半部分的行数
    for j in range(1,top_row+1-i):   # 控制外围为空的直角三角形部分
        print(' ',end='')    # 打印空格占位用
    for k in range(1,i*2):    # 控制每行*或空格的数量
        if k==1 or k==i*2-1:    # 空心部分边的*和空格的条件判断
            print('*',end='')    # end=''不换行，而是以空格分隔，继续在同一行打印下一个*
        else: print(' ',end='')  # 打空格为空心部分
    print()     # 当两个并列的for循环执行完毕后,再换行
# 下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):    # 控制下半部分的行数
    # 控制外围为空的直角三角形部分
    for j in range(1,i+1):
        print(' ',end='')
    # 倒三角
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:   # 空心部分边的*条件判断
            print('*',end='')
        else: print(' ',end='')          # 打空格为空心部分
    print()

