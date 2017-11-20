# 函数
"""
你可以定义一个由自己想要功能的函数，以下是简单的规则：
    函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
    任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    函数内容以冒号起始，并且缩进。
    Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 函数定义
def func1(param):
    print(str(param))
    return "return"

# 函数参数的类型和应用场景
# 调用函数
print(func1("hello world!"))

print("十六进制:"+hex(20))

print("# 函数的参数")

# 位置参数
def power(x):
    return x * x

# 默认参数  -- 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# 参数组合  参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

def func(*args, **kw):
    pass

