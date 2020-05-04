# -*- encoding: utf-8 -*-
'''
@File : s4_client.py
@Time : 2020/05/04 19:43:23
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：聊天室的客户端
'''
import socket
import threading
import os
# here put the import lib


def get_host_ip() -> str:
    '''
    获取本机ip

    :return:返回本机ip
    '''
    return socket.gethostbyname(socket.gethostname())


def get_now_time() -> str:
    '''
    获取现在时间

    :return:格式是：年-月-日 时:分:秒
    '''
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time


def recv_msg():  #
    print("连接成功！现在可以接收消息！\n")
    while True:
        try:  # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            response = s.recv(1024)
            print(response.decode("utf-8"))
        except ConnectionResetError:
            print("服务器关闭，聊天已结束！")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("utf-8"))
    os._exit(0)


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc1, duan1 = input("请输入服务器的ip和端口，用空格隔开")
    # addr = (soc1, int(duan1))  # 服务器端的IP和端口
    addr = (get_host_ip(), 9999)
    try:
        s.connect(addr)
    except Exception as e:
        print(e)
    else:
        threading.Thread(target=recv_msg).start()
        threading.Thread(target=send_msg).start()
