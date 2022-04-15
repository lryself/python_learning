# 大作业11---51job网站爬虫
---
## 1.引言
### **1.1题目要求**：
在51job网站上，爬取2020年发布的Python开发工程师的职位的薪酬，计算北京地区该职位的平均薪酬
### **1.2项目背景**：
* 本项目使用了scrapy框架编写的爬虫程序，在此之前学习了xpath，lxml，scrapy等内容
* 项目于2020年6月13日全部完成
## 2.总体设计
### 2.1 需求分析：
1. 目标网址：51job
2. 爬取内容：2020年发布的Python开发工程师的职位的薪酬
3. 分析内容：计算北京地区该职位的平均薪酬
### 2.2 开发机配置：
1. 处理器：intel 8th i5-8300H
2. 内存：8GB
3. 系统：windows 10 64位 
### 2.3 项目结构：
* main_spider --爬虫项目主体
	* main_spider --爬虫代码
		* spiders --
			* \_\_init\_\_.py
			* a51job.py --51job网站爬虫
		* \_\_init\_\_.py
		* items.py
		* middlewares.py --中间件
		* pipelines.py --处理管道
		* settings.py --爬虫设置
		* config.py --全局变量
	* result --爬虫结果
		* positions.csv --所有爬取结果
		* analyze.txt --爬取结果分析
	* \_\_init\_\_.py --初始化
	* scrapy.cfg --爬虫配置
	* startproject.py --运行爬虫
* venv --虚拟环境
* README.md --项目说明
* requirements.txt --所需第三方库
### 2.4 需人工处理的步骤：
将config.py中的job_URL替换为您需要爬取的51job搜索结果页面的第一页的url
## 3.运行设计
1. 程序运行的入口为startproject.py
2. 程序爬取结果在result文件夹下，positions.csv为所有的爬取结果，analyze为分析结果
3. 程序运行时只会显示warning以上级别的日志，其他的已隐藏
## 备注：
1. 程序已调整符合pep8编码规范
2. 平均薪酬的计算方法为招聘给出的薪酬范围的平均值作为单个职位的薪酬