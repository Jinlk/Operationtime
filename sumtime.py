# -*- codeing = utf-8 -*-
# @Time : 2020/8/27 0:48 
# @Author : Jin
# @File : sumtime.py 
# @Software: PyCharm

import time
def timer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("运行时间为：%s"%(stop_time-start_time))
    return warpper
