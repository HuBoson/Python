from configparser import UNNAMED_SECTION
#
import pandas as pd
df=pd.read_csv('C:\\Users\WIN10\Desktop\Python学习\第六章~模块\date\SMA.csv',index_col=1,parse_dates=True)  # 这种方式前面不行用2个“\”,index_col=1设定第2列为索引,parse_dates=True将日期转成DataFrame格式
df=pd.read_excel('.\date\KOL.xlsx')
# 删除名为 'Unnamed: 0' 的列
if 'Unnamed: 0' in df.columns:
    del df['Unnamed: 0']
print(df.info())    # 如果不指定head值，会全部打开所有数据
print(df.head())    # 如果不指定head值，会全部打开所有数据
print(df.describe())

# 数据的保存/读取
hdf5=pd.HDFStore('存入地址+新文件名.h5', 'w')     # hd5格式,金融数据常用数据格式,'w'写入到文件路径,打开也是语法,用'r'打开文件,生成了hd5文件.
df.to_json('新文件名')   # 另存json格式文件到本地
df.to_csv('新文件名')   # 另存csv格式文件到本地
df.to_excel('新文件名')   # 另存excel格式文件到本地
