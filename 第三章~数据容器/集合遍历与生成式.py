from stringprep import in_table_a1

#集合的遍历操作
s={10,20,30,40,50}
for item in s:
    print(item,end="\t")
#使用enumerate()函数:
for index,item in enumerate(s):
    print(index,"--->",item)

#集合生成式：
s={i for i in range(9)}
print(s)
s={i for i in range(9) if i%2==0}
print(s)

