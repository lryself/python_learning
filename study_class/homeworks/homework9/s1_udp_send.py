# -*- encoding: utf-8 -*-
'''
@File : s1_udp.py
@Time : 2020/04/29 18:58:51
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具
'''

from socket import *
# here put the import lib

# 1. 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
dest_addr = ('192.168.1.2', 8888)

# 迭代1 连续发送数据
while True:
# 3. 从键盘获取数据
    send_data = input("请输入要发送的数据:")
# 迭代2 如果输入的数据是exit,就退出程序
    if send_data=='exit':
        break
# 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
# 5. 关闭套接字
udp_socket.close()