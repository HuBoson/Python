"""
ZeroDivisionError: 当除数为0时，引发的异常
IndexError:索引超出范围所引发的异常
KeyErrr：字典取值时key不存在的异常
NameError：使用一个没有声明的变量引发的异常
SyntaxError: 语法错误
ValueError：传入值错误
AttributeError：属性或方法不存的异常
TypeError：类型不合适引发的异常
IndentationError：不正确的缩进
"""
# try：  except...else...finally结构

# try:         #尝试：可能会出现异常的代码
#     num1=int(input('请输入第一个数字'))
#     num2=int(input('请输入第二个数字'))
#     result=num1/num2
# except ZeroDivisionError:    # 捕获异常：如果出现异常，要执行的代码，ZeroDivisionError（被0除的意思）
#     print('除数不能为0')
# except ValueError:           # 出现异常执行,ValueError输入出错,没有异常不会执行
#     print('不能将字符串转成整数，请输入整数数字')
# except BaseException:       # 出现异常执行,BaseException:最大异常,没有异常不会执行
#     print('未知异常')
# else:                         # 没有出现异常的每个except要执行的代码,出现的不执行
#     print('结果',result)
# finally:                        # 无论是否出现异常，都会对上面没一行执行的代码确认执行
#     print('程序执行结束')

# raise 创建和引发自定义异常,并不限于在try语句块中使用。为了中断程序的正常执行流程或测试异常处理机制,在循环中使用raise来中断循环并引发异常。
# 示例：
try:
    gender=input('请输入你的性别')
    if gender!='男' and gender!='女':
        raise Exception('输入的性别只能男或者女')
    else:
        print('您的性别是:',gender)
except Exception as e:
    print(e)