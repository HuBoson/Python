#多装饰器+循环使用
login_flag=False

def login(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag==False:
            print('未完成用户登录')
        #登录校验
        while 1:
            username=input('请输入您的姓名')
            password=input('请输入密码')
            if username=='admin' and password=='123456':
                print('登录成功')
                login_flag=True
                break
            else:
                print('登录失败，请重新输入')
        ret=fn(*args, **kwargs)
        return ret
    return inner
@login
def add():
    print('添加员工信息')
@login
def delete():
    print('删除员工信息')
@login
def upd():
    print('编辑员工信息')
@login
def search():
    print('搜索员工信息')

add()
delete()
search()