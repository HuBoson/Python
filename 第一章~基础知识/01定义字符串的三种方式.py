text1 = "这个是双引号的定义方式"   #双引号
text2 = '这个单引号的定义方式'    #单引号
text3 =  """这个三引号多方的定义方式
如下：
我是一只小小的鸟，
想要飞也飞不高哦"""     #3引号的
print(text1)
print(text2,type(text2))  #注意：打印type属性一起打印的写法
print(text3)
print(type(text3))   #注意：type属性可以和内容分开来打印，或上面text2的打印写法