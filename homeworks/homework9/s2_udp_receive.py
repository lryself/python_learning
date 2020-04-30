# -*- encoding: utf-8 -*-
'''
@File : s2_udp_receive.py
@Time : 2020/04/30 16:54:20
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出
'''
import socket
# here put the import lib
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_addr=("",8888)
udp_socket.bind(udp_addr)
print("本机ip为：",socket.gethostbyname(socket.gethostname()))
print("本机端口号：",udp_addr[1])
print("开始接收")
while True:
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print("{1}:{0}".format(recv_data[0].decode("gbk"),recv_data[1]))

udp_socket.close()