# coding: utf-8
# @Author : lryself
# @Date : 2021/1/12 20:39
# @Software: PyCharm

if __name__ == '__main__':
    model_templetes = '''# coding: utf-8
from . import db


'''
    import re

    with open("models/models.py", "r", encoding="utf-8") as f:
        str_lines = f.readlines()
        m = ""
        name = ""
        for line in str_lines:
            if re.match("^(class|t_).*:", line):
                if not m == "":
                    with open(name, "w", encoding="utf-8") as f1:
                        f1.write(m)
                name = "models/{}Model.py".format(line[6].lower()+line[7:-12])
                m = model_templetes + line
            elif re.match("^(from|db|#|\n).*", line):
                continue
            else:
                m += line
        else:
            with open(name, "w", encoding="utf-8") as f1:
                f1.write(m)
