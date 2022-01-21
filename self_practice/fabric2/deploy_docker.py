# coding: utf-8
# @Author : lryself
# @Date : 2022/1/19 18:09
# @Software: PyCharm
import fabric2
import os

from fabric2 import Connection


def build_local_go(dir_name):
    os.system(f'f: & cd F:\\programme\\MicroService\\{dir_name} &'
              'SET CGO_ENABLED=0&'
              'SET GOOS=linux&'
              'SET GOARCH=amd64'
              '& go build -o ./deploy/ main.go')


def docker_build(connect, imageName: str, port: str, use_port: bool):
    connect.put(f"F:/programme/MicroService/{imageName}/deploy/main", f"/docker/{imageName}")
    with connect.cd(f"/docker/{imageName}/"):
        try:
            connect.run(f"docker stop {imageName}")
        except Exception:
            pass
        try:
            connect.run(f"docker rm {imageName}")
        except Exception:
            pass
        # connect.run(f"docker image rm {imageName}")
        connect.run(f"docker build -t {imageName} -f ./dockerfile .")
        if use_port:
            connect.run(f"docker run -d -p {port}:{port} --name {imageName} {imageName}")
        else:
            connect.run(f"docker run -d -P --name {imageName} {imageName}")


def main():
    conn = fabric2.Connection("192.168.41.100", "root", connect_kwargs={"password": "lpc123LPC"})
    build_local_go(conn)
    docker_build(conn, "registry_center", "9001", True)
    # docker_build(conn, "config_center", "9000", True)
    # docker_build(conn, "registry_center", "9001", True)


if __name__ == '__main__':
    main()
