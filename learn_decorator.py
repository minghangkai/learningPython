#初级装饰器（双层嵌套）

#函数对象有一个__name__属性，可以拿到函数的名字：now.__name__ >>>'now'
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator——log
# 可以定义如下：
def log(func):
    def wrapper(*args, **kw):#*args为任意参数，**kw为任意字典
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log    # 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
def now():
    print('2015-3-25')
now()

# 高级装饰器（三层嵌套）
"""
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
# 比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#这个3层嵌套的decorator用法如下： #相当于执行now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')

now()
"""

# 经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
# 未解决这个问题，Python内置的functools.wraps 将decorator装饰之后的函数__name__属性还原
# 所以，一个完整的decorator的写法如下：
"""
import functools
#不带参数
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#带参数
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
"""