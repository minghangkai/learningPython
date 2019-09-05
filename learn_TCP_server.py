#服务端：与client1配套
# 导入socket库:
import socket,time
import threading

#服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))
#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')
#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:target参数为线程执行方法，args/kwargs: 要传入方法的参数。
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

