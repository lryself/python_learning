#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file: listener.py
# description:
# author: lidekun
# datetime: 2020/6/24 13:05
# software: PyCharm
# coding=utf-8
import subprocess
import requests
import logging
import config


class Listener(object):
    def __init__(self):
        self.splash_host = 'localhost'
        self.splash_port = '8050'
        self.splash_timeout = 10
        self.splash_ping_times = 3
        self.logger = self.get_logger()

    def get_logger(self, name=__name__, level=logging.INFO):
        """
        获得一个logger
        :param name:
        :param level:
        :return:
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def ping_splash(self):
        """
        尝试连接splash，测试splash服务是否正常
        :return: 正常，True,无法访问,False
        """
        splash_url = 'http://{}:{}'.format(self.splash_host, self.splash_port)
        try:
            resp = requests.get(splash_url, timeout=self.splash_timeout)
        except Exception as e:
            return False
        if resp.status_code != 200:
            self.logger.error(u'状态码异常.{}'.format(resp.status_code))
            return False
        return True

    def listen_splash(self):
        """
        监听splash，尝试连接splash，直到成功或者失败self.splash_ping_times次。
        :return: 成功，True，失败，False
        """
        for i in range(self.splash_ping_times):
            if self.ping_splash():
                return True
        return False

    def restart_splash(self):
        """
        通过命令，重启docker服务和splash服务
        :return:
        """
        # (code, output) = commands.getstatusoutput("service docker restart")
        # self.logger.info(u'命令：service docker restart.状态码：{}.输出：{}.'.format(code, output))
        (docker_code, docker_output) = subprocess.getstatusoutput("systemctl restart docker")
        if docker_code != 0:
            self.logger.warning(u'docker重启出错')

        (code, output) = subprocess.getstatusoutput("docker restart {0}".format(config.SPLASH_NAME))
        self.logger.info(u'命令：docker restart {0}.状态码：{1}.输出：{2}.'.format(config.SPLASH_NAME, code, output))
        if code != 0:
            self.logger.warning(u'splash容器重启出错')

    def control(self):
        if self.listen_splash():
            self.logger.info(u'splash服务一切正常')
        else:
            self.logger.error(u'splash服务异常，正在重启...')
            self.restart_splash()
            self.logger.info(u'重启完成')


if __name__ == '__main__':
    Listener().control()
