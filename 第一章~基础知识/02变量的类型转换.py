#以下是将变量转换成整数int
text ="90"
#注意：只能转换本身就是数字的字符串，非数字的字符串不能转换
print(text)  #此时打印出来的属性是字符串str
num = int(text)   #将变量的字符串type转换成int整数
print(num,type(num))   #打印出来的属性是整数int
print(num+120)     #转换后就可以用来计算

#以下是将变量转换成浮点数float
text1 = "1.83"
height = float(text1)     #将变量属性转换成浮点float
print(height,type(height))  #打印出来的属性是整数float

#以下是将变量转换成字符串str
txet2 = 1.57
num =  str(txet2)    #将变量属性转换成字符串str
print(num,type(num))   #打印出来的属性是字符串<class 'str'>