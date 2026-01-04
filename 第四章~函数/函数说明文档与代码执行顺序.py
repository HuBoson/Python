#函数说明文档添加
#示例：
def get_sum(x,y):
    """
    类似这样说明此函数的计算方式
    :param x: 
    :param y: 
    :return: 
    """  #用引号添加说明文档，左侧箭头可以隐藏和打开内容
    return x+y
sum=get_sum(1,2)
print(sum)

#函数的执行流程
def test_a():
    print("--------2--------")
def test_b():
    print("--------1--------")
    test_a()     #此处调用了test_a
    print("--------3--------")
test_b()  #打印test_b的函数结构为1,2,3，其中2是从test_a调用过来的，按顺序执行