# coding: utf-8
# @Author : lryself
# @Date : 2021/3/2 22:14
# @Software: PyCharm

from line_profiler import LineProfiler


def do_stuff():
    for i in range(1000):
        for j in range(1000):
            print(i+j)


if __name__ == '__main__':
    lp = LineProfiler()
    lp_wrapper = lp(do_stuff)
    lp_wrapper()
    lp.print_stats()
