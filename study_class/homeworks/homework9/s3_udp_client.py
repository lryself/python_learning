# -*- encoding: utf-8 -*-
'''
@File : s3_udp_client.py
@Time : 2020/04/30 23:26:52
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答--客户端
'''
import socket
# here put the import lib
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=("192.168.1.6",9999)
# addr=input("请输入ip和端口，用空格隔开").split()
while True:
    data=input("请输入：")
    s.sendto(data.encode("utf-8"),addr)
    message=s.recv(1024)
    print("message:{}".format(message.decode("utf-8")))