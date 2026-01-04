name = ["周杰伦", "林俊杰", "王力宏", "王一博", "林俊杰","易烊千玺"]  # 列表名称
# print(name)

# 1.append(),将添加的内容以整体的方式追加到另一个列表中,在列表中增加内容，如下；
# name.append(["迪丽热巴","叶轻眉")  #默认添加在最后一个
# print(name)

# 2.extend(添加数据容器)，将添加的内容以单个元素的方式追加到另一个列表中
# name2=["杨紫","刘亦菲"] #默认添加在后面
# name.extend(name2)
# print(name)

#3.insert（插入），在指定的位置添加下标或元素
# name.insert(3,"王源") #在上面的名字第三的位置增加了“王源”（含0是第四的位置）
# print(name)

#4.del(删除列表中的某一个元素和下标)
# del name[0]
# print(name)

#5.pop，(删除下标对应的元素),与del不同的是pop可以返回被删除的元素
# name.pop(0)
# print(f"删除的元素是{name.pop(0)}")    # 返回被删除的元素

#6.remove(删除元素)，删除重复的元素的时候默认会先删除前面的
# name.remove("林俊杰")
# print(name)

#7.clear（清空列表），把列表里面的元素全部清空
# name.clear()  #注意clear后面需要有个(),否则不能清空列表
# print(name)

#8.count(获取某个元素出现的次数)
# print(f"林俊杰出现{name.count('林俊杰')}次")

#9.index(获取元素在列表中的下标)，如果没有该元素就会报错
# print(f"王一博的下表是{name.index('王一博')}")  #外面有双引号的情况下，里面应该用单引号

#10.len(获取列表中元素的个数)
print(f"列表中共有{len(name)}个人的名字")