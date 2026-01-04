
# py内置函数之数据类型：
# 1.数据类型有int整数、float浮点数、bool布尔(包含True和False)、complex复数（实数+虚数）和str字符串：
分数score = 90      #int整数，也可以用中文名做变量
height =1.87       #float带小数点的为浮点数
print(round(0.1+0.2,1))   # py等计算机语言中两个小数在计算时需要round取整，最后的",1"是保留一位小数的意思，否则结果为：0.30000000000000004
is_marry = False    #bool布尔类型，内容为空和数字为0时，为False,其他为True
name = "张三"         # "字符串"
#通过type() 来检测数据类型
print("姓名是",name,type(name))  #class 'str'
print ("张三的分数是",分数score,type(分数score))   #class 'int'
print ("张三的身高是",height,type(height))     #class 'float'
print("张三是否有结婚",is_marry,type(is_marry))   #class 'bool'

# 2.sum(总和),min(最小数),max(最大数),pow(次幂方)
lst=[1,45,23,98,33]
print(max(lst))      #用max找出列表中最大的数，为“98”
print(min(lst))     #用min找出列表中最大的数，为“1”
print(sum(lst))      #用sum计算列表中数的总和，为“200”
print('商和余数：',divmod(13,4))  #商和余数： (3, 1)
print(round(3.1415926,2))   # 尾数“2”为保留2位小数，如果-1负数就整余到个位，以此类推。

print('-'*50)
x=3
y=12
print(pow(x,y))   #通过pow计算次幂值，等同于x**y，结果为“531441”

# 3.bin（二进制），oct（八进制），hex（十六进制），format（格式化），ord（码位），chr（反转码位）
a=18   #我们常用的十进制
print(bin(a))  #通过bin内置函数命令转换成二进制，结果为 0b10010
print(oct(a))  #通过oct内置函数命令转换成八进制，结果为 0o22
print(hex(a))  #通过hex内置函数命令转换成十六进制，结果为 0x12
print(format(a,"08b"))  # "08b"意思是:通过"0"补充成一个完整的8位二进制数（超过8位不能自动切割），尾“b”代表二进制，“o”为八进制，“x”为十六进制
a1="我"
print(ord(a1))   # ord查找”我“字在unicode中码位是25105，只能单字查找
print(chr(25105))   # chr通过编码位置，展示出“我”文字

b=0b10010
print(int(b))  #其他进制的数都可以通过int内置函数命令转换成二进制，结果为 18

# 4.slice打断数据
s=slice(2,5,3)
print('我爱大家的中华大地深圳宝安'[s])
