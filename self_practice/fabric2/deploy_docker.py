# coding: utf-8
# @Author : lryself
# @Date : 2022/1/19 18:09
# @Software: PyCharm
import os

import fabric2


def build_local_go(dir_name: str):
    os.system(f'f: & cd F:\\programme\\MicroService\\{dir_name} &'
              'SET CGO_ENABLED=0&'
              'SET GOOS=linux&'
              'SET GOARCH=amd64'
              '& go build -o ./deploy/ main.go')


def go_docker_build(connect, imageName: str):
    connect.put(f"F:/programme/MicroService/{imageName}/deploy/main", f"/docker/{imageName}")
    with connect.cd(f"/docker/{imageName}/"):
        try:
            connect.run(f"docker-compose build")
            connect.run(f"docker-compose up -d")
        except Exception as e:
            print(e)


def docker_build(connect, imageName: str):
    with connect.cd(f"/docker/{imageName}/"):
        try:
            connect.run(f"docker-compose build")
            connect.run(f"docker-compose up -d")
        except Exception as e:
            print(e)


def docker_restart(connect, imageName: str):
    with connect.cd(f"/docker/{imageName}/"):
        try:
            connect.run(f"docker-compose stop")
            connect.run(f"docker-compose start")
        except Exception as e:
            print(e)


def main():
    conn = fabric2.Connection("XXX", "root", connect_kwargs={"password": "XXX"})
    # print("开始交叉编译config_center")
    # build_local_go("config_center")
    # print("开始远程部署config_center")
    # go_docker_build(conn, "config_center")
    # docker_build(conn, "config_center")

    # print("开始交叉编译registry_center")
    # build_local_go("registry_center")
    # print("开始远程部署registry_center")
    # go_docker_build(conn, "registry_center")
    docker_build(conn, "registry_center")

    # print("开始远程部署fabric_server")
    # docker_build(conn, "fabric_server")

    # print("开始交叉编译crypt_center")
    # build_local_go("crypt_center")
    # print("开始远程部署crypt_center")
    # go_docker_build(conn, "crypt_center")
    # docker_build(conn, "crypt_center")

    # print("开始交叉编译sso_center")
    # build_local_go("sso_center")
    # print("开始远程部署sso_center")
    # go_docker_build(conn, "sso_center")
    # docker_build(conn, "sso_center")

    conn.close()


if __name__ == '__main__':
    main()
