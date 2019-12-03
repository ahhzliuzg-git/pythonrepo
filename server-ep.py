import socket
import threading
import time
def tcplink(sock,addr):
    print('Accpet new connection from %s:%s...' % addr)
    ###sock.send(b'Welcome!')
    buffer = []
    while True:
                #接收1kb的大小
        data = sock.recv(4096)
        #等待1
        #time.sleep(50)
        #如果dat为空 或者 data收到'exit'则退出
        if not data or data.decode('utf-8') == 'exit':
            break
        #发送Hello + data 
        ###sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        print('%s' %data)
        buffer.append(data)
        print('%s' %buffer)
        #接收数据
    sock.close()
    print('Connection from %s :%s closed.' %addr)
    text=b''.join(buffer)

##    header, html = text.split(b'\r\n\r\n', 1)
##    print(header.decode('utf-8'))
##    # 把接收的数据写入文件:
##    with open('ep.txt', 'wb') as f:
##        f.write(html)
    
    print(text.decode('utf-8'))
    # 把接收的数据写入文件:  ool't
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('127.0.0.1',9999))
#s.bind(('192.168.100.252',9999))
s.bind(('192.168.100.252',9999))
s.listen(5)
print('waiting for connection...')

while True:
    sock , addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
