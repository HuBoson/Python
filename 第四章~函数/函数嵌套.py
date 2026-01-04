# 函数嵌套类似循环语句，必须调用最外层的def函数程序才能执行。
#示例：
def func1():
    print(1)
    def func2():
        print(2)
        def func3():
            print(3)
        print('b')
        func3()
        print('c')
    print('a')
    func2()
    print('d')
func1()





