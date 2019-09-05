#客户端
# # 导入socket库:
import socket


# 创建一个socket:创建Socket时，AF_INET指定使用IPv4协议，
# 如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM 指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接:connect中的参数为元组
s.connect(('www.sina.com.cn', 80))#在这里容易出现错误，端口号要与客户端的端口号一致，否则会报错

# 发送数据:请求首页
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    #接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，
    # 在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close() # 当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了

#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
# 把HTTP头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)