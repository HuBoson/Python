"""
安装requests：
1.进入windows开始菜单运行搜索框输入cmd进入windows的dos界面输入pip install requests回车（调用python库中的pip进行安装）
安装完后如果有提示版本升级可以再输入python -m pip install --upgrade pip回车确认，两次见Successfully表示安装成功。
"""
# 示例：
import requests    # 导入爬虫模块
import re  # 导入正则表达式模块提取需要的内容
url=requests.get("https://www.weather.com.cn/")   # 通过爬虫requests.get网址
url.encoding='utf-8'   # 设置编码格式
print(url.text)    # 对象名（变量名）.属性，调用网址中的文字信息
city=re.findall('" target="_blank">([\u4e00-\u9fa5]*)',url.text)  # 调取网址HTML中内容，正则中[\u4e00-\u9fa5提取中文文字
name=re.findall('"station_name2">([\u4e00-\u9fa5]*)</div>',url.text)
mm=re.findall('"temperature" > (.*) mm < / div >',url.text)
print(city)
print(name)
print(mm)

