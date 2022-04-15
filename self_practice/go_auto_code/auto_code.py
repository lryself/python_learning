# coding: utf-8
# @Author : lryself
# @Date : 2022/1/17 15:37
# @Software: PyCharm
import os
import re


if __name__ == '__main__':
    project_name = "sso_center"
    rep_dir = {
        "${{project_name}}": project_name
    }

    def pathLoad(p) -> str:
        return os.path.abspath(p).replace("templete", project_name)

    if not os.path.exists(project_name):
        os.mkdir(project_name)

    for filepath, dirname, filename in os.walk("templete"):
        result_path = pathLoad(filepath)
        for d in dirname:
            dp = pathLoad(os.path.join(filepath, d))
            if not os.path.exists(dp):
                os.mkdir(dp)
        for f in filename:
            fp = pathLoad(os.path.join(filepath, f))
            if re.match("^.*\.exe$", f):
                with open(os.path.join(filepath, f), "rb") as f1:
                    with open(fp, "wb") as f2:
                        temp = f1.read()
                        f2.write(temp)
            else:
                with open(os.path.join(filepath, f), "r", encoding="utf8") as f1:
                    with open(fp, "w", encoding="utf8") as f2:
                        temp = f1.read()
                        for k, v in rep_dir.items():
                            temp = temp.replace(k, v)
                        f2.write(temp)

    # go_get_list = [
    #     "github.com/fsnotify/fsnotify",
    #     "github.com/gin-contrib/cors",
    #     "github.com/gin-contrib/sessions",
    #     "github.com/gin-gonic/gin",
    #     "github.com/go-redis/redis",
    #     "github.com/heatxsink/go-logstash",
    #     "github.com/lestrrat-go/file-rotatelogs",
    #     "github.com/rifflock/lfshook",
    #     "github.com/sirupsen/logrus",
    #     "github.com/spf13/viper",
    #     "gorm.io/driver/mysql",
    #     "gorm.io/gorm"
    # ]
    # for c in go_get_list:
    #     os.system(f"go get {c}")
