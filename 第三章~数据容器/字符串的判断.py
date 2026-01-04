#字符串的判断
str="hello world,hello python,hello china"
#1.startswith(),判断是否以某个子串作为开始，可以得到一个True或False的结果
rs =str.startswith("hello")
print(f"是否以“hello”开始{rs}")
#2.endswith()，判断是否以某个元素结束
rs=str.endswith("china")
print(rs)  #判断结果为True