""""
主要用pandas的文件读取,pd.read_csv(文件目录地址+文件名,index_col=1,parse_dates=True)
常用with open,不用close文件
open(文件路径，mode="",encoding="”)，也可以用open直接创建新文件
mode分别有  r:read 以只读模式读取文件
           w：write  每次open都会清空文件夹再写入，如果文件不存在会自动创建一个文件
           a: append  在原来的文件中增加内容
           b: 读写的非文本文件（图片、视频等），文件类型会转换成 bytes
           + ：与w/r/a等一同使用，在原来功能上增加读写功能
           with：连接上下文，每次操作不需用close关闭
绝对路径：c:/文件夹名称/xxxx.txt
相对路径：   ./上一层文件夹/文件夹名称/xxxx.txt，其中"./"表示当前位置，前面加一个点"../"表示上一级目录
修改文件：1.从源文件中读取内容
        2.从内存中进行调整（修改）
        3.把修改后的内容写入新的文件中
        4.删除源文件，将新文件重命名成源文件
"""
import os     # 操作系统相关的模块引入
import time   # 时间相关的模块

# 读取文件示例：
open("c:/文件夹名称.txt")       # 绝对路径
open("./文件夹名称/代码/xxx.txt")      # 相对路径
f=open("c:/文件夹名称.txt",mode="r",encoding="utf-8")   # mode为需要做什么编辑，r是read读取的意思
content=f.read()        # 全部读取
print(content)
line=f.readline()       # 读取文件中的某一行代码，可以一次多次持续读取
print(line)
line=f.readline().strip()      # 用strip去除读取文件中的字符串左右两端的空白，换行，制表符等。
print(line)
con=f.readlines()          # readlines读取全部行放在一个列表中
print(con)

# 用循环的方式读取文件，最常用的方式：
for line in f:             #从f赋值的文件夹中读取每一行数据
    print(line.strip())       # 用strip去除读取文件中的字符串左右两端的空白，换行，制表符等。

# write写入文件：
f=open("../文件夹名称.txt",mode="w",encoding="utf-8")   #mode为需要做什么编辑，r是write读取的意思
f.write("需要写入的元素")
f.close()         #每次操作后需要关闭文件

# write循环写入：
lst=[11,22,33,44,55,66,77,88]
f=open("张三.txt",mode="w",encoding="utf-8")        # 放在循环外
for line in lst:
    f.write(line)
    f.write("\n")        # 用\n来换行
    f.close()

# append写入：在原来的文件中增加内容,不会清楚之前的内容
f=open("../文件夹名称.txt",mode="a",encoding="utf-8")   #mode为需要做什么编辑，a是append读取的意思
f.write("需要写入的元素")


#with使用：
with open("../文件夹名称.txt",mode="r",encoding="utf-8") as f:   # as给打开的文件取别名的作用，f:表示在这个文件里操作下面的循环
    for line in f:
        print(line.strip())
# f.close()      # with打开文件就不需要再用close了

# 读取图片：在读写非文本文件的时候需要加“b”
with open("图片名称.jpg",mode="rb") as f:
    for line in f:
        print(line.strip())

#文件的复制或移动，从源文件中读取内容，写入到新的文件中
# 打开源文件，太长的时候可以用“\”表示连接下一行
with open("图片名称.jpg",mode="rb") as f1,\
     open("./文件夹名称/新的图片.jpg",mode="wr") as f2:   # 写入新的地址
    for line in f1:
        f2.write(line)

#文件的修改：
with open("文件名称.txt",mode="r",encoding="utf-8") as f1,\
     open("文件名称_副本.txt",mode="w",encoding="utf-8") as f2:
    for line in f1:
        line=line.strip()     # 用strip去掉换行
        if line.startswith("要修改的元素"):
            line=line.replace("要修改的元素","修改后的元素")
        f2.write(line)
        f2.write("\n")
time.sleep(3)   # 可以打开文件夹观察到程序用3秒时间命名文件
#删除源文件
os.remove("源文件名称")
#把副本文件重命名成源文件
os.rename("源文件名称_副本.txt","源文件名称.txt")
