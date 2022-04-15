# -*- encoding: utf-8 -*-
'''
@File : s4_chatroom.py
@Time : 2020/04/30 23:28:11
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
题目：设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室；
  参考文档：https://blog.csdn.net/CxsGhost/article/details/103319864
'''
import os
import socket
import datetime
import threading
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


class Sever(object):
    def __init__(self, duan: int = 9999, user_number: int = 5):
        '''
        创建服务器并开始运行

        :param duan:服务器端口号

        :param user_number:最大用户连接数
        '''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.users = {}  # 用户池
        try:
            self.sock.bind((get_host_ip(), duan))
        except Exception as e:
            print(e)
        else:
            self.sock.listen(user_number)
            print("服务器开始运行，ip为：{}端口为：{}".format(get_host_ip(), duan))
            while True:
                s, addr = self.sock.accept()
                self.users[addr] = s
                print("用户{}加入聊天室，现有{}人".format(addr, len(self.users)))
                threading.Thread(target=self.recv_send, args=(s, addr)).start()

    def recv_send(self, sock: socket, addr: str):
        '''
        用户线程类

        :param sock:用户的socket

        :param addr:用户的ip和端口
        '''
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("utf-8")
                msg = "{}用户{}发来消息：{}".format(get_now_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("utf-8"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    def close_sever(self):
        '''
        关闭服务器
        '''
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever = Sever()
    while True:
        cmd = input()
        if cmd == "stop sever":
            sever.close_sever()
        else:
            print("输入命令无效，请重新输入！")
