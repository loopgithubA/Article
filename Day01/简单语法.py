# 语句分隔符
# print("hello yuan");print(1+1)
# print("hello yuan")  # 不能随便 空格
# print(1 + 1)

# 注释
import random  # 导入random模块
import datetime

# 获取1-100的随机数
print(round(random.random() * 100))

# 打印时间： 格式 年/月/日
print(datetime.datetime.now().strftime("%Y-%m-%d %X"))
"""
这是一个多行注释
"""
# PEP8 规范
# print(1 + 1)  # 运算符两侧 逗号冒号 加空格  快捷键：ctrl + alt + l
# 变量 用于存储在计算机里的数据
# 版本1
# print(1 + 2)
# print(1 * 2)
# 版本2
# x = 1
# y = 2
# z = x + y
# print(z)
# print(x + y)
# print(x - y)
# 1 叫做数据或者值，x y 叫变量，如果值没有被变量引用就会被回收

# 变量修改
# x = 10
# print(x)
# x = 20
# print(x)

# 数字字母下划线组合，不允许出现除了下划线以外的任何特殊符号；
# 不允许数字开头；
# 区分大小写 ；
# 不可以使用python 的关键字和内置函数名

# print = 100
# print("hello,word")  # 会报错

# 见名知意
# name = "liu"
# print(name)
# my_firstname = "柳"
# myFirstName = "柳"  # ”小驼峰“
# print(myFirstName)

# 数据类型 1 2 3 整形，1.2 浮点型；布尔类型 True False;字符串“”
# print(type(10))

# 比较表达式
# a = 10
# b = 3.14
# print(a > b)
# print(a == b)
# print(a <= b)

# 所有数据都有自己的bool值
# 零值：所有数据类型都有且只有一个值的bool状态是False
# 整形和弗蒂阿逆行的零值：0
# 字符串： “”  列表：[] 字典：{}  都是空的
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool([]))
print(bool({}))

# 构建字符串
# 方式1 双引号
s1 = "hello liu"
# 方式2单引号
s2 = 'hello liu'
# 方式3三引号
s3 = """
字符串类型
"""
s4 = """
    1.购买道具
    2.攻击
    3.逃跑
    4.退出
"""
print(s4)

# 字符串基本操作
# 转义操作\  将某些普通符号给予特殊功能；讲一些特殊符号普通画

# \n 换行符
s = " my name is liu\n i am 19"
print(s)
# S='let's Go!' # 报错
S = 'let\'s Go!'  # \ 可以讲‘普通化的效果
print(S)
# path='\yuan\next\download'# 会报错
path = '\yuan\\next\download'  # 取消反斜杠的特殊功能
print(path)
# 格式化输出
names = "龙傲天"
age = 18
height = 180
# 方式1
print("我的名字叫%s，我的年龄%d，我的身高%d" % (names, age, height))
# 方式2 推荐
print(f"我的名字叫{names}，我的年龄{age}，我的身高{height}")

# 字符串序列操作 1.容器类型 2.有序 正索引0123456789；负索引-1-2-3-4.。。。。-10
c = "hello yuan"
# 索引操作： 字符串【索引】 查询字符
# print(c[6])
# print(c[0])
# print(c[-1])
# 切片操作: 字符串【开始索引：结束索引:step=1】顾头不顾尾
# print(c[6:9])
# print(c[6:])  # 取到最后
# print(c[:5])
# print(c[-10:-5])  # 一定是从左向右切
# print(c[-4:])
# print(c[:5:2])  # 每隔两个取一个；
# print(c[:5:-1])  # 会报错 切片方向和步长方向不一致
# print(c[::-1])  # 将字符串翻转过来

# 拼接 +
# d = 'hello'
# e = ' liu'
# print(d + e)
name = "liu"
age = 19
# print("我的名字：" + name + " 我的年龄:" + age + "!")  # 拼接不了 字符串加整形 加不了
print("我的名字：" + name + " 我的年龄:" + str(age) + "!")
# print("*" * 100)

# 计算字符串长度 ：元素个数 len()
# s5 = "hello word"
# print(len(s5))

# 针对容器类型： in判断，判断某个成员是否存在
# s6 = "yuan rains eric alvin"
# print("rain" in s6)
# print("rains" in s6)
# print("erc" in s6)  # 必须是连续的

# 输入输出函数 input
# 接收的是动态值
# name = input("请输入姓名")
# age = input("请输入年龄")
# print(f"姓名：{name} 年龄{age}")

# num1str = input("num1::")  # input 接受的是字符串!!!!!!不论你传的是什么值
# num2str = input("num2::")
# print(int(type(num1str)))  # class ’str‘

# print(num1str + num2str)  # 字符串的拼接

# num1_int = int(num1str) # 将字符串类型化为整形
# num2_int = int(num2str)

# print(num1_int + num2_int)

# 输出函数print
# x=1000
# print(100,"hello",x)
# print(100,"hello",x,sep=",")

# 字符串内置方法 数据对.方法名（参数）
# upper lower
S1 = "hello WORD"
# num = 100
print(S1.upper())
print(S1.lower())
# print(num.upper())  # 报错，upper只针对字符串

# startwith：是否姨.。开头 endiwith是否以。。结尾 方法

s1 = "apple banana peach orange"
# print("banana" in s1)
print(s1.startswith("apple"))
print(s1.startswith("banana"))
# print(s1.startswith(" apple"))
# print(s1.startswith("a"))  # true
# name = "张杰"
# print(name.startswith("李"))
# print(name.endswith("杰"))

# 类型转换
numStr = input("请输入一个数字")
# 先判断numStr是否是一个数字字符串 is.digit
print(numStr.isdigit())
if numStr.isdigit():
    # numStr是一个纯数字字符串
    numInt = int(numStr)
    print(numInt * 2)
else:
    print("输入有误，请输入一个纯数字")

# strip  去除字符串两端的 空格 或 换行符

user = input("请输入用户名：")
user = user.strip()
print(user, len(user))

# split 把字符串分割 join链接起来

citys = "北京 哈尔滨 深圳 重庆"
ret = citys.split(" ")  # 列表
print(ret)
print(len(ret))
ret2 = ";".join(ret)  # 用；拼接起来
print(ret2)

# find  index

s = "yua rain apple banana"
ret = s.find("yuan")
print(ret)  # 没找到就是-1
# ret1 = s.index("apples") # 没找到会报错


# count: 计数 replace替换
names = "张三 李四 王五 张三 张三"
print(names.count("张三"))
info = "i am yuan;yuan is very nice and yuan is handsome"
new_info = info.replace("yuan", "alvin")
print(info)
print(new_info)

# 运算符
# 计算运算符
print(5 % 2)  # 5➗2 余数是1
# 判断奇数偶数
x = 23
print(x % 2 == 0)
# 赋值运算符
# a = 10
# a = a + 2
# a += 2
experience = 10
print(" 打死妖怪，增加10经验")
print(experience)
blood = 100
print("受到轻微攻击，掉血10")
blood -= 10
print("当前血值", blood)

# 逻辑运算符 and or not
chinese = 148
math = 150
print(chinese == 150 and math == 150)  # false
print(chinese == "150" or math == 150)  # true

age = 23  # 判断年龄在20-35
print(age > 20 and age < 35)  # true
print(20 < age < 35)  # true

user = "root"
pwd = "123"
username = input("请输入用户名")
password = input("请输入密码")
print(username == user and password == pwd)

total = 640
# 总成绩大于700 或者语文和数学同时满分
print(total > 700 or (chinese == 150 and math == 150))  # 多个条件用括号并列
