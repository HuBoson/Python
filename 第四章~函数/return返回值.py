
# 如果函数的运行结果需要在其他函数中使用，就需要使用返回值的函数
# return多个返回值时，需要逗号分隔，按顺序传入数据，如果不需要返回值，可以省略return
# 返回值是一个(或多个)都是元组类型，在函数体的最后，用于结束该函数(不影响其他def函数体)
# 函数名称可以当做变量名称一样进行赋值操作
# 在多层嵌套中，内层函数的 return 值并不是直接返回到上一层的上一层函数。内层函数的 return 值只会返回给外层函数

#多个返回值示例：
def fun():
# 有多个返回值时，是一个元组，只能在一个return中体现，且return后面不能有其他内容，是因为程序执行return后就结束了，类似循环的break
# 如果函数没有写return返回值，默认为None（就是没有内容的意思，是一个空值）
    return 1,2
rs=fun()  #可以定义一个变量去接收return值
print(type(rs))   #得到是元组
num1,num2=fun()  #也可以这样拆包处理，定义两个变量，分别去接收return两个返回值
print(num1,num2)



def sum(a,b):
    s=a+b
    return s   #将s返回给函数调用处理
print(sum(1,2))
s1=sum(sum(1,2),4)   #将第一次return返回的结果值1+2=3进行调用，再和第二次调用的sum值4相加，结果为7
print(s1)

#多个返回值示例：
def sum(num):
    s=0    #累积和
    odd=0   #奇数和
    even=0   #偶数和
    for i in range(1,num+1):
        if i%2==0:    # 奇数
            odd+=i
        else: even+=i
        s+=i
    return s,odd,even     # 3个返回值
result=sum(10)
print(result)
# 解包赋值：
a,b,c=sum(10)  #返回的3个值是元组类型，用a,b,c三个变量进行解包赋值
print(a,b,c)   #解包后就不是元组了，也可以单独分开打印或调用