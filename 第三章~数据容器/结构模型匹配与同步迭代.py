
# match case结构模型匹配：可以匹配列表，字典，元组。但集合不可以；
# data=eval(input("请输入要匹配的数据"))
# match data:
#     case {"name":"张三","age":18}:
#         print("字典")
#     case [10,20,30]:
#         print("列表")
#     case (40,50,60):
#         print("元组")
#     case _:
#         print("相当于else")

#同步迭代：
fruits=["apple","banana","orange"]
counts=[3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case "apple",3:
            print("3个苹果")
        case "banana",4:
            print("4个香蕉")
        case "orange",5:
            print("5个橙子")




