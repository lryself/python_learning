# -*- encoding: utf-8 -*-
'''
@File : s1_udp_receive.py
@Time : 2020/04/30 00:07:28
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具
'''

from socket import *
# here put the import lib

def main():
   # 绑定端口信息
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    
    local_addr=('',8888)

    udp_socket.bind(local_addr)
    while True:
    # 接收数据
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
        print(recv_data)
    
    #迭代升级
        # print("%s:%s" %(recv_data[0].decode('gbk'),recv_data[1]))
    
   # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()