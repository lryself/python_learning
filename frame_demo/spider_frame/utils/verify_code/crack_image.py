# coding: utf-8
# @Author : lryself
# @Date : 2022/8/26 0:22
# @Software: PyCharm
import tesserocr
from PIL import Image

image = Image.open("8-2.jpg")

image = image.convert('L')
threshold = 170
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()

result = tesserocr.image_to_text(image)
print(result)
