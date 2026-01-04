
# 字符串有以下几种操作
# 1.find\rfind()：两个功能一样，find为从左到右查找，rfind为从右向做查找，查询字符串出现的位置，当不存在时候结果为-1，与index不同的是当查询元素不存在时index会报错
# print(f"hello出现的位置是{str.find('hello')}")  #只显示第一次出现的位置下标
# print(f"py出现的位置是{str.rfind('py')}")     #从右向左查找完，再返回本身计数（不含本身元素后的计数下标）
# print(f"hello出现的位置是{str.find('his')}")  #当结果没有“his”时候下标显示是-1
# # print(f"hello出现的位置是{str2.index('his')}")  #当结果没有“his”时报错
#
# #2.index\rindex():两个功能一样，find为从左到右查找，rfind为从右向做查找，当查询元素不存在时index会报错
# print(f"hello出现的位置是{str.index('hello')}")
# print(f"hello出现的位置是{str.rindex('hello')}")  #是按右向左查找每个字母计数下标为12（不含本身元素后的计数下标）
#
# #3.count()统计字符串出现的次数
# print(f"hello出现的次数是{str.count('hello')}")
#
# #4.len（）长度统计
# print (f"总长度是{len(str)}")
#
#
# #注意：以下几个操作，因为字符串是不可变类型，所以修改后，要新生成一个新的字符串才可以，如下：
# #5.replace() 替换字符串里面的元素
# str3=str1.replace('hello','你好！')  # 新生产一个字符串str3
# print(str3)
#
# #6.split()分割字符串，以逗号分割字符
# str4 = str2.split(",")   # 新生产一个字符串str4
# print(str4)
#
# #7.join()用其他符号将字符串拼接成一个新的字符串
# str5="@".join(str4)            #使用@符号重新拼接字符串并生成一个新的字符串str5
# print(str5)

#8.strip()去除一些没有用的空格、换行符号等，常用一些爬虫的数据整理

#9.字符串大小写操作：
s1="python"
s2=s1.title()  # 将单词首字母大写
print(s2)
s3=s1.upper()  #  将所有字母大写
print(s3)
s4=s1.lower()    # 将单词所有字母小写
print(s4)

#用upper()来忽略大小的示例：
code="xAd1"
user=input("请输入验证码:")
if code.upper()==user.upper():
    print("验证码正确")
else:
    print ("验证码不正确")
