str="the best python programming language is python"
#1.统计上面字符串里面有几个y字符
c=str.count("y")
print(f"u出现了{c}次")
#2.将字符串内的空格换成“|”
str_new=str.replace(" ","|")
print(str_new)
#3.将新的字符串分割，生成一个列表
list=str_new.split("|")
print(list)