## 2022年4、5月高频机试题

最近准备[华为](https://www.nowcoder.com/jump/super-jump/word?word=%E5%8D%8E%E4%B8%BA)OD社招的同学还比较多，增加了100多的订阅，大多是没有编程经验的同学，上来一顿的搜题背题，没有去理解题目思考结题思路，导致机考时题目稍微一变化就不知道怎么做了，不过OD的机试的重复也是真的高，下面是最近整理的高频机试题，希望对你有帮助。

所有题目见[《华为机试题整理（已更新185篇）》](https://pycoder.blog.csdn.net/article/details/124648380)

| 题目  | 分值  |
| --- | --- |
| [字符串格式化输出](https://pycoder.blog.csdn.net/article/details/124622168) | 100分 |
| [按身高和体重排队](https://blog.csdn.net/qq_23934063/article/details/124722680) | 100分 |
| [拼接 URL](https://pycoder.blog.csdn.net/article/details/124789706) | 100分 |
| [磁盘容量排序](https://pycoder.blog.csdn.net/article/details/124833659) | 100分 |
| [分糖果](https://pycoder.blog.csdn.net/article/details/124852441) | 100分 |
| [圆桌队列](https://pycoder.blog.csdn.net/article/details/124853534) | 100分 |
| [计算矩形相交面积](https://pycoder.blog.csdn.net/article/details/124903531) | 100分 |
| [We Are A Team](https://pycoder.blog.csdn.net/article/details/124775659) | 100分 |
| [数字涂色](https://pycoder.blog.csdn.net/article/details/125025444) | 100分 |
| [最少交换次数来组合小于k的整数](https://pycoder.blog.csdn.net/article/details/124971993) | 100分 |
| [员工工号问题](https://pycoder.blog.csdn.net/article/details/125055645) | 100分 |
| [补种未成活胡杨](https://pycoder.blog.csdn.net/article/details/125075713) | 100分 |
| [敏感字段加密](https://blog.csdn.net/qq_23934063/article/details/125108420) | 100分 |
| [5键键盘的输出](https://blog.csdn.net/qq_23934063/article/details/125113344) | 100分 |
| [IPv4地址转换成整数](https://pycoder.blog.csdn.net/article/details/125114748) | 100分 |
| [水仙花数](https://pycoder.blog.csdn.net/article/details/125115241) | 100分 |
| [单词接龙游戏](https://pycoder.blog.csdn.net/article/details/125120901) | 100分 |
| [数大雁](https://pycoder.blog.csdn.net/article/details/125118133) | 100分 |
| [二叉树按照中序遍历输出](https://pycoder.blog.csdn.net/article/details/125126797) | 100分 |
| [考古学家](https://pycoder.blog.csdn.net/article/details/125120430) | 100分 |
| [停车位问题](https://pycoder.blog.csdn.net/article/details/125137735) | 100分 |
| [幼儿园找出同班的小朋友](https://pycoder.blog.csdn.net/article/details/125120430) | 100分 |
| [高效的任务规划](https://pycoder.blog.csdn.net/article/details/125120380) | 200分 |
| [喊 7 的次数重排](https://pycoder.blog.csdn.net/article/details/124912915) | 200分 |
| [解密犯罪时间](https://pycoder.blog.csdn.net/article/details/125114910) | 200分 |
| [最长的指定瑕疵度的元音子串](https://pycoder.blog.csdn.net/article/details/125076242) | 200分 |
| [面试（最少面试官数）](https://pycoder.blog.csdn.net/article/details/124994936) | 200分 |
| [九宫格按键输入](https://pycoder.blog.csdn.net/article/details/124854517) | 200分 |
| [仿 LISP 运算](https://pycoder.blog.csdn.net/article/details/124874353) | 200分 |
| [路灯问题](https://pycoder.blog.csdn.net/article/details/124973199) | 200分 |
| [书籍叠放问题](https://pycoder.blog.csdn.net/article/details/125012163) | 200分 |
| [导师请吃火锅](https://pycoder.blog.csdn.net/article/details/125025504) | 200分 |
| [数据分类](https://pycoder.blog.csdn.net/article/details/125037065) | 200分 |
| [树形目录操作](https://pycoder.blog.csdn.net/article/details/124580509) | 200分 |
| [奥运会奖牌榜的排名](https://pycoder.blog.csdn.net/article/details/124058528) | 200分 |
| [转骰子](https://pycoder.blog.csdn.net/article/details/124722008) | 200分 |
| [机器人走迷宫](https://pycoder.blog.csdn.net/article/details/124621543) | 200分 |
| [跳格子游戏](https://pycoder.blog.csdn.net/article/details/125120448) | 200分 |
| [高效的任务规划](https://pycoder.blog.csdn.net/article/details/125120380) | 200分 |
| [圆桌队列](https://pycoder.blog.csdn.net/article/details/124853534) | 200分 |

## 机试必须要会的函数

## 输入输出处理

[华为](https://www.nowcoder.com/jump/super-jump/word?word=%E5%8D%8E%E4%B8%BA)OD社招使用的是ACM 模式，刷惯了LeetCode的同学一时可能会不适应，ACM模式你的代码需要处理输入`input`输出`print`

```python
while 1:
    try: 
        # 输入
        a = input().split()
        # 输出
        print(int(a[0]) + int(a[1]))
    except:
        break
```

当输入的是 4 2 3 4 5 ,每行的第一个数字表示后面有效数据的格式时，我们可以这样处理 `*nums`

```python
n, *nums = input().split()
print(n)
print(nums)
> 4
> ['1', '2', '3', '4']
```

当输入的数据需要批量转换数据类型是，我们可以使用 `map`

```python
n, *nums = list(map(int, input().split()))
print(n)
print(nums)
> 4
> [1, 2, 3, 4]
```

当输入的逗号分隔的数据时，我们可以使用 `.split(',')`分隔

当需要接收连续n行的输入时，我们可以使用推导式连续接收输入
如：[【华为机试真题 Python实现】机器人走迷宫](https://pycoder.blog.csdn.net/article/details/124621543) 问题

```python
# 4
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

n = int(input())
nums = [input().split() for i in range(n)]
print(n)
print(nums)

> 4
> [['1', '2', '3', '4'],
>  ['2', '3', '4', '5'],
>  ['3', '4', '5', '6'],
>  ['4', '5', '6', '7']]
```

当需要输出指定格式，可以使用
`"".join()` 不能拼接字符串，如果待处理数据时数值类型需要使用转化类型

```python
nums = [1, 2, 3, 4]
print(",".join(map(str, nums)))
> 1,2,3,4
```

## for 循环

当我们需要遍历一个可迭代对象（字典、列表、集合、字符串等）不需要特殊处理下标时，推荐使用`for`循环，可以避免访问越界问题

### 通过下标访问元素

```
nums = [1, 2, 3, 4]

for i in range(len(nums)):
    print(nums[i], end=" ")
> 1 2 3 4
```



### 直接迭代访问元素

```
nums = [1, 2, 3, 4]
for i in nums:
    print(i, end=" ")
> 1 2 3 4
```

### 同时访问下标和元素

```
nums = [1, 2, 3, 4]
for i, v in enumerate(nums):
    print(i, v, end=" ")
> 0 1 1 2 2 3 3 4 
```

## while 循环

当我们遇到滑动窗口问题，需要通过左右边界动态调整窗口大小时，推荐使用`while`

```
nums = [1, 2, 3, 4]
i = 0
j = 1
while j < len(nums):
    print(nums[i: j])
    j += 1
> [1]
> [1, 2]
> [1, 2, 3]
```

## 字符ASSIC码转换

当遇到对字符处理的题是，比如 abcz 转为 bcda，实际是对assic值加1来处理的

```python
ord('a')
> 97
ord('b')
> 98
chr(97)
> a
```

## [进制转换

如[【华为机试真题 Python实现】数据分类【2022 Q1 Q2 |200分】](https://blog.csdn.net/qq_23934063/article/details/125037065) 问题中出现的 [进制转换](https://www.nowcoder.com/jump/super-jump/word?word=%E8%BF%9B%E5%88%B6%E8%BD%AC%E6%8D%A2)`hex()` 整型转16进制数，返回字符串
函数名| 功能
:---|:---
hex|10进制转16进制数
int| 将一个字符串或数字转换为整型
bin|10进制转2进制

## 绝对值计算

abs() 函数返回数字的绝对值

## 幂运算

pow() 函数方法返回 xy（x 的 y 次方） 的值
我也可以使用 x**y 表示x 的 y 次方

## 最值选取

使用max获取最大值，min获取最小值

## 排序

当我们需要对列表、字典排序时，可以使用sorted
当需要按多种条件同时进行排序问题，需要根据金牌数、银牌数、铜牌数、国家名称首字母4个条件同时排序，我们可以使用lambda构建排序规则实现

```python
dex_lst = sorted(temp.items(), key=lambda itm: itm[1], reverse=True)
```