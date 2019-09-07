# 协程没有线程切换的开销,不需要多线程的锁机制
# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
# Python对协程的支持是通过generator实现的。
def consumer():
    r = ''
    while True:
        n = yield r
        # Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
        # 即n等于函数produce中c.send(n)中的n
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n) # r等于consumer（）中的r，即每次yield后的r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；send方法有一个参数，该参数指定的是上一次被挂起的yield语句的返回值。
# consumer通过yield拿到消息，处理，又通过yield把结果传回；Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。