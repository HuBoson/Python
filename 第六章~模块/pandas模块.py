'''
核心数据结构：
Series：带标签的一维数组，可存储任意数据类型
DataFrame：带标签的二维表格结构，适合存储结构化数据
数据读取与查看：
使用 pd.read_csv() 读取CSV文件，掌握encoding、parse_dates等参数
用 head()、tail() 查看数据，describe()统计数据：可以得到最大、最小、平均值、标准差等信息 和 info() 获取数据概况
数据选择与过滤：
熟练使用 loc（基于标签）和 iloc（基于位置）进行数据选择
掌握布尔索引实现复杂数据过滤
数据清洗：
处理缺失值：用 isnull() 检测，fillna() 填充，dropna() 删除
去重：drop_duplicates() 移除重复行
数据操作与分析：
排序：sort_values() 按值排序，支持多列排序
分组聚合：groupby() 是Pandas最强大的功能之一，可按指定列分组并应用聚合函数
数据合并：用 merge() ,join() 和 concat() 处理多表连接
resample('D',how='ohlc') : 专门对“时间序列”按新的时间频率重采样的函数，
比如：1 分钟 K 线 → 5 分钟 / 1 小时；日数据 → 周 / 月数据升降采用,按月或日,ohlc开盘价,最高价,最低价,收盘价
pct_change() : 计算百分比变化率/收益率,常见写法：df['ret'] = df['close'].pct_change()
'''
from tokenize import group
import pandas as pd
from contourpy.util import data

date=pd.DataFrame({'group':['a','b','c','d','e','f'],'date':[1,4,2,6,9,10]})    # DataFrame创建数据
print(date)
date.sort_values(by=['group', 'date'], ascending=[False, True], inplace=True)   # 按 'group' 降序和 'date' 升序排序
print(date,'按group降序和date升序排序')
print('-'*50)

date1=pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[3,2,1,3,3,4,4]})
print(date1)
date1.drop_duplicates(subset=['k2'], keep='first', inplace=True)     # 按K2去掉重复的数据
date1.sort_values(by='k2')
print(date1,'# 按K2去掉重复的数据')
print('-'*50)
# Pandas中的Shift函数（数据处理）
# 在Pandas库中，shift函数用于数据偏移操作，常用于时间序列分析：
# 基础语法：DataFrame.shift(periods=1, freq=None, axis=0, fill_value=None)
# periods：移动步数，正数表示向下移动，负数表示向上移动
# freq：时间序列的移动频率（如'D'代表天）
# axis：移动方向，0为行方向，1为列方向
# fill_value：填充缺失值的默认值
df = pd.DataFrame({'value': [10, 20, 30, 40, 50]})
df['prev_value'] = df['value'].shift(1)  # 向下移动1行
print(df)

# rolling()函数：用于计算时间序列数据的滚动统计量，如移动平均、移动标准差等。
#示例:
# ticker = 'AAPL'
# data = yf.download(ticker, start='2022-01-01', end='2023-01-01')
# # 计算收盘价的5日和20日滚动均值
# data['MA_5'] = data['Close'].rolling(window=5).mean()
# data['MA_20'] = data['Close'].rolling(window=20).mean()