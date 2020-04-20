# -*- encoding: utf-8 -*-
'''
@File : s4_save_question.py
@Time : 2020/04/19 20:25:34
@Author : lryself 
@Version : 1.0
@Contact : lnolvwe@163.com
题目：爬取这个网址上http://www.python3.vip/doc/prac/python/0001/，所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；
    文本文件类似（注意是类似的效果，不是说一定要做的一模一样）的效果如下：

  参考文档：https://blog.csdn.net/weixin_43687366/article/details/88877996
   大家看完这篇文档后，再开始动手做这道题；

'''

from bs4 import BeautifulSoup
import requests
import tools
import re
# here put the import lib
url = 'http://www.python3.vip/doc/prac/python/0001/'
 
#伪装成浏览器
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
 
#发送请求
r = requests.get(url,headers=headers).content.decode('utf-8')
# print(r)
 
#解析html文档
soup = BeautifulSoup(r,'html.parser')	#这里用lxml会出错
# print(type(soup))
 
#查找每个练习的a链接href属性获取对应的链接地址
re_a = soup.find( class_ ='nav__items').find_all('a')	#返回的是100个a标签的列表
 
#创建一个列表保存url
list = []
for i in re_a:
	list.append(i.attrs['href'])
# print(list)
 
 
"""
	2、根据获取的每个练习的链接地址来请求每个练习获得页面内容
"""
class dataclass:
  def __init__(self,x):
    self.title=x
    self.question=""
    self.answer=""
  
  def addquestion(self,x):
    self.question+=x
    self.question+="\n"

  def addanswer(self,x):
    self.answer+=x
    self.answer+="\n"
  
def finddata(list1,data1):
  for i in range(len(list1)):
    if list1[i].title==data1:
      return i
  return None

def writedata(f,list1):
  for i in list1:
    f.write(i.title+"\n")
    f.write(i.question+"\n")
    f.write("答案与解析：\n")
    f.write(i.answer+"\n")
    f.write('-'*50+"\n")
with open("s4_questions.txt","w"):
  pass
for x in list:
  data=[]
  # 请求详细页面
  test = requests.get(x, headers=headers).content.decode('utf-8')
  # print(test)

  # 解析html文档
  soup_test = BeautifulSoup(test, 'html.parser')
  if soup_test.find('head').text=='404 Not Found':
    print(x+"打开失败")
    continue
  # print(type(soup_test))

  # 查找练习内容
  # 查找标题
  title_text = soup_test.find(class_='page__title').text

  list1=soup_test.find(class_='content').contents
  p=-1
  isquestion=True
  for i in list1:
    if i=='\n':
      continue
    if i.text=='':
      continue
    elif re.match(r"^题目[0-9]$",i.text) or i.text=="编程题" or i.text=="判断题":
      isquestion=True
      data.append(dataclass(i.text))
      p+=1
    elif re.match(r"^题目[0-9]-答案$",i.text):
      isquestion=False
      p=finddata(data,i.text[:3])
    elif i.name=='p':
      if i.text=='请大家点击此处链接，观看讲解视频':
        data[p].addanswer(i.text)
        data[p].addanswer(i.contents[0].attrs['href'])
      elif i.text=="扫码分享给朋友，一起学更有动力哦":
        continue
      elif i.text=="答案与解析":
        continue
      elif i.text=='点击这里 下载一个zip包，解压后，得到一个目录source。':
        title_text+="\n{}{}".format(i.contents[0].attrs['href'],i.text)
      else:
        if isquestion:
          data[p].addquestion(i.text)
        else:
          data[p].addanswer(i.text)
    elif i.name=='div':
      if "class" in i.attrs:
        if i.attrs['class'][0]=='highlighter-rouge':
          data[p].addquestion(i.text)
        elif i.attrs['class'][0]=='language-py' and i.attrs['class'][1]=='highlighter-rouge':
          data[p].addanswer(i.text)
    elif i.name=='ul':
      list2=i.find_all('p')
      for w in list2:
        data[p].addquestion(w.text)
  with open("s4_questions.txt","a",encoding="utf-8") as f:
    f.write("章节："+title_text+"\n")
    writedata(f,data)
    f.write("*"*50+"\n")

print("全部保存完成")
  # 查找题目
  # questions = soup_test.find(class_='content').find_all('h2')
  # for w in questions:
  #   if re.match(r"^题目[0-9]$",w.text) or w.text=="编程题" or w.text=="判断题":
  #     data.append(dataclass(w.text))
  # question = soup_test.find(class_='content').find_all('p')
  # p=0
  # flag=True
  # for i in question:
  #   if i.text == '请大家点击此处链接，观看讲解视频':
  #     flag=True
  #     p-=1
  #     data[p].addanswer(i.text)
  #     data[p].addanswer(i.contents[0].attrs['href'])
  #   elif i.text == '扫码分享给朋友，一起学更有动力哦':
  #     break
  #   elif i.text == '答案与解析':
  #     continue
  #   elif i.text !='':
  #     flag=True
  #     data[p].addquestion(i.text)
  #   elif flag==True:
  #     p+=1
  #     flag=False
  # if soup_test.find(class_='language-py highlighter-rouge'):
  #   answers = soup_test.findall(class_='language-py highlighter-rouge')
  #   for i in answers:
  #     answer=''
  #     answer1 = i.findall('span')
  #     for w in answer1:
  #       answer+=w.text


  # # 程序源代码
  # try:
  #   dict['code'] = soup_test.find(class_="hl-main").text
  # except Exception as e:
  #   dict['code'] = soup_test.find('pre').text
  # # print(code)
  # # print(dict)

  # with open('s4_question.txt','w',encoding='utf-8') as file:
  #   file.write(dict['title']+'\n')
  #   file.write(dict['tm']+'\n')
  #   file.write(dict['cxfx']+'\n')
  #   file.write(dict['code']+'\n')
  #   file.write('*'*50+'\n')
  #   file.write('\n')