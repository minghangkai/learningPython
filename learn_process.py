#该文件运行时应只运行某一部分，即将其他部分注释掉
from multiprocessing import Process #跨平台支持
from multiprocessing import Process, Queue
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
from multiprocessing import Pool #如果要启动大量的子进程，可以用进程池的方式批量创建子进程
import subprocess #subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
import os, time, random #fork()需要os


#部分一
"""
#linux/mac可运行部分，windows不能运行
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:it would create a process
#os.fork()———— 子进程永远返回0，而父进程返回子进程的ID
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
"""


#部分二：跨平台部分
"""
#子进程执行函数
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    #将子进程执行函数和函数进程名传入Process类中创建实例
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')
"""

#部分三：用进程池的方式批量创建子进程
"""
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    #获得当前时间
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        # apply_async 是异步非阻塞的。
        # 意思就是：不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。
        # apply方法是阻塞的。
        # 意思就是等待当前子进程执行完毕后，在执行下一个进程。
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    #请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
    # 这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
    # 这是Pool有意设计的限制，并不是操作系统的限制。如果改成：p = Pool(5),则会最多同时执行5个
    p.close()
    p.join()
    print('All subprocesses done.')
"""

#部分四：子进程不做记录，若需查看则去廖雪峰教程

#部分五：进程间通信
"""
"""
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()