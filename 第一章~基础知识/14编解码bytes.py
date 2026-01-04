
""""
1.ascii: 8bit 1byte   美国早期英文标准编码
2.gbk:16bit 2byte   中文windows默认
3.unicode: 32bit,4byte  (很少用，只是一个标准)
4.utf-8： mac默认，英文：8bit，1byte    欧洲：16bit，2byte   中文：24bit， 3byte
5.gbk和utf-8不能直接进行转换，需要转换成字符再转换，程序用的都是utf-8，用户常用是gbk
6.str.encode("编码“），bytes.decode("解码”)
"""
# 示例一：
s="Boson胡柏松"
bs1=s.encode("gbk")     #结果 b'xxxxx'是2byte数据类型，共6个字节+1个英文字节，注意：英文都是1byte
bs2=s.encode("utf-8")   #结果 b'xxxxx'是3byte数据类型，共9个字节+1个英文字节，注意：英文都是1byte
print(bs1)
print(bs2)
#把gbk的字节转换成功utf-8的字节
bs=b'\xd6\xdc\xbd\xdc\xc2\xd7'
s=bs.decode('gbk')       # 用decode解码成文字字符串
print(s)
bs3=s.encode('utf-8')      # 再用encode编码成utf-8
print(bs3)