"""协程"""

from greenlet import greenlet


def func1():
    print(1)            # 第二步：输出 1
    gr2.switch()        # 第三步：切换到 func2 函数
    print(2)            # 第六步：输出 2
    gr2.switch()        # 第七步：切换到 func2 函数，从上一次执行的位置继续向后执行


def func2():
    print(3)            # 第四步：输出 3
    gr1.switch()        # 第五步：切换到 func1 函数，从上一次执行的位置继续向后执行
    print(4)            # 第八步：输出 4


gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch()            # 第一步：去执行 func1 函数
