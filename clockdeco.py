#内省中能使用原函数名称，functools模块
import time
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args,**kwargs):
        t0 = time.perf_counter()
        result = func(*args,**kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs: #可以使用关键字参数
            pairs = ['%s=%r' % (k,w) for k,w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        msg = '[%0.8fs] %s(%s) ->%r' %(elapsed,name,arg_str,result)
        print(msg)
        return result
    return clocked