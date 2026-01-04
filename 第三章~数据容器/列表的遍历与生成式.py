name = ['Tom', 'John', 'Smith']    #列表
# 通过while循环遍历（有下标的时候只能while），实现对列表进行遍历循环操作
i = 0
while i < 3:
    print(f"下标为{i}对应的元素是{name[i]}")
    i += 1  # 注意在这个位置

# for循环遍历，常用
for x in name:
    print(x)

#列表生成式：
import random
lst1=[item for item in range(4)]
print(lst1)
lst2=[item*item for item in range(6)]
print(lst2)
lst3=[random.randint(1,10) for item in range(4)]
print(lst3)
lst4=[i for i in range(10) if i % 2 == 0]   #从列表中选择符合i%2==0条件的元素组成新的列表
print(lst4)
#二维生成式列表：
lst5=[["城市","环比","同比"],
      ["北京",102,103],
      ["上海",104,505],
      ["深圳",101,90]]
print(lst5)
#遍历二维列表使用双层for循环：
for row in lst5:  # 行
    for item in row: # 列
        print(item,end="\t")
    print()  #换行用
#列表生成式生成一个4行5列的二维列表
lst6=[[j for j in range(5)] for i in range(4)]
print(lst6)



# 练习：
# 从一个列表中取出偶数放到一个新的列表中
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定义一个新的列表
lst_new = []
# 使用while循环实现遍历
i=0
while i<len(lst):
#判断哪些数是偶数
    if i %2==0:
        lst_new.append(i)  #添加到新的列表中
    i+=1
print(lst_new)

# 使用for循环实现遍历
# for x in lst:
#     if x % 2 == 0:
#         lst_new.append(x)   #添加到新的列表中
# print(lst_new)
