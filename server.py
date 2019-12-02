#just for git test  add this sentence.
import socket
import threading
import time
def tcplink(sock,addr):
    print('Accpet new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
                #接收1kb的大小
        data = sock.recv(1024)
        #等待1
        time.sleep(1)
        #如果dat为空 或者 data收到'exit'则退出
        if not data or data.decode('utf-8') == 'exit':
            break
        #发送Hello + data 
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

        #接收数据
        # 接收数据:
    sock.close()
    print('Connection from %s :%s closed.' %addr)
#socket.SOCK_STREAM是针对tcp的，UDP是用socket.DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connection...')

while True:
        sock , addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
#just for git test2  add this sentence.