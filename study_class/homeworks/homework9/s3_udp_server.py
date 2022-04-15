# -*- encoding: utf-8 -*-
'''
@File : s3_udp_server.py
@Time : 2020/04/30 23:27:30
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答--服务器端
'''
import socket
# here put the import lib
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
duan=9999
s.bind((socket.gethostbyname(socket.gethostname()),duan))
print("本机ip为：",socket.gethostbyname(socket.gethostname()))
print("本机端口为:",duan)
while True:
    data, addr = s.recvfrom(1024)
    print('Received from {}:{}.'.format(addr[0],addr[1]))
    s.sendto('Hello, {}!'.format(data.decode("utf-8")).encode("utf-8"), addr)