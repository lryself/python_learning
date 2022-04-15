# -*- encoding: utf-8 -*-
"""
@File : s4_chat_udp
@Time : 2020/4/26 20:58
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：
"""
from multiprocessing import Process
from socket import *
# here put the import lib


def send_massage():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    dest_addr = ('192.168.1.2', 9999)
    while True:
        send_data = input("请输入要发送的数据:")
        if send_data == 'exit':
            break
    # for send_data in ("hallo","你好","byebye"):
        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    udp_socket.close()


def recv_message():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("", 8888))
    while True:
        # 接收数据
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # 打印显示接收到的数据
        if recv_data == 'exit':
            break
        print(recv_data[1],":"+recv_data[0].decode("utf-8"))

    udp_socket.close()


if __name__ == '__main__':
    # p1 = Process(target=send_massage)
    print(gethostbyname(gethostname()))
    p2 = Process(target=recv_message)
    p2.start()
    # p1.start()
    # p1.join()

    send_massage()
    # p2.join()
    #因发现进程无法从键盘读取，故主进程执行发送命令，子进程执行接收命令 