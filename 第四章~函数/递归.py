
# 递归就是在函数体内，调用该函数自己来进行运算的方式，一般要使用if语句来判断递归的运算和终止（或定义明确的结束条件），
# 否则会一直循环到默认1000次，最多可以设置2000次
# 优点:
# 简洁性: 递归可以使代码更简洁和易于理解，特别是在处理自相似问题时。
# 自然性: 许多问题（如树和图的遍历）天然适合递归解决方案。
# 缺点:
# 性能问题: 递归调用可能导致大量的栈空间使用，甚至导致栈溢出。
# 效率低下: 未经优化的递归可能会重复计算相同的子问题，导致性能下降。
# 优化递归
# 为了提高递归的性能，可以使用技术如记忆化（memoization）和尾递归优化（Python 不支持尾递归优化，但可以通过其他方式改进）。
# 示例一：阶乘算法
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)      # 在函数体内自己调用自己
print(fac(5))  # 输出结果: 120       # 阶乘算法：5*4*3*2*1  n*(n-1)*...

# 示例二：快速排序，利用递归来对数组进行排序
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)   # 外部函数的返回值是内部函数本身

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)  # 输出: [1, 1, 2, 3, 6, 8, 10]

# 示例三，递归：函数自己调用自己并重复执行，如果没有设定拦截默认就是一个死循环，默认最大深度重复次数是1000，最多可以设置2000次
#示例如下：
def func4():
    print(10)
    # func4()    #如果执行这行递归代码，会报错！超出最大深度，maximum recursion depth exceeded！
func4()

