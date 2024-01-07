"""
单分支语句
if 表达式 ：
    语句1
    语句2
    (都属于表达式的语句)
else:
    语句3
    语句4

语句5     与if else并列 并不属于else 后面的语句
"""
import string

# age = int(input("请输入年龄"))
# if age >= 18:
#     print("成人电影")
#     print("亚洲区")
#     print("欧美区")
# else:
#     print("青少年电影")
#     print("黑猫警长")
#     print("大头儿子")
#
# print("欢迎收看")

# 多分支语句
"""
if 表达式1：
    语句1
    语句2
    语句n
elif 表达式2：
    语句1
    语句2
    
else：
    语句1
    语句2
"""

# height = float(input("请输入您的身高【米】："))
# weigh = float(input("请输入您的体重【公斤】："))
# BMI = weigh / height ** 2
#
# if BMI < 18.5:
#     print("偏瘦")
# elif BMI < 24:
#     print("正常")
# elif BMI < 28:
#     print("超重")
# else:
#     print("肥胖")

"""
分支嵌套
"""
#
# pid = input("请输入你的身份证号：")
# # 身份证号位数判断是否为18位
# if len(pid) == 18:
#     print("打印个人信息")
#     # 打印性别，身份证号倒数第二位是偶数就是女生 奇数是男生
#     num = int(pid[-2])  # "5"==>5
#     if num % 2 == 0:
#         print("性别：女性")
#     else:
#         print("性别：男性")
#     # 打印籍贯
#     jiguanCode = pid[:6]
#     print('jiguanCode',jiguanCode)
#     if jiguanCode=='110000':
#         print("籍贯：北京市")
#     elif jiguanCode=="120000":
#         print("籍贯：天津市")
#     elif jiguanCode=="310000":
#         print("籍贯：上海市")
#     elif jiguanCode=="500000":
#         print("籍贯：重庆市")
#     else:
#         print("不是直辖市")
# else:
#     print("输入有误")
# print("程序结束")

"""
循环语句 while(条件循环) for(遍历循环)
while 表达式:
    循环语句体
        
for  i in 容器数据类型:   字符串 列表 字典
    循环语句
    
    
"""
# 有效次数循环(初始变量 条件判断 步进语句)
# 打印1-100
# count = 0
# while count < 100:
#     count += 1
#     print("count", count)

# # 打印100-1
# count1 = 100
# while count1 > 0:
#     print(count1)
#     count1 -= 1

# 遍历列表
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for i in l:
#     print(i)

# range(start,end,step=1)
# for i in range(100,1,-1): # 1娶不到,100到1
#     print(i)


# 随机验证码
import random
import string

# char = random.choice("0123456789abcdefg")
# print(string.ascii_lowercase)  # "abcdef...xyz "
# print(string.ascii_uppercase)  # "ABCDEF...XYZ"
# print(string.digits)  # "0123456789"

# s = ""
# for i in range(5):
#     all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
#     random_char = random.choice(all_chars)
#     # print("random_char:",random_char)
#     s += random_char
# print(s)

"""
如果是范围性的数据,那么+=就是拼接,如果是可以累加的数据那就是求和

"""
# 拼接
# s = ""
# for i in range(5):
#     s += str(i)# 字符串的拼接
# print(s)

# 1+2+3+....100
# ret = 0
# for i in range(1, 101):
#     ret += i
# print(ret)

# 计算1-100 所有偶数和
# ret1 = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         ret1 += i
#
# print(ret1)


# break 推出整个循环
# continue 退出档次循环
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# print("process end")

# 打印半径为1-100的园的面积 Πr²
# 找到第一个面积大于1000的半径值
# for r in range(1, 101):
#     # print(r)
#     # 计算园的面积
#     erea = 3.14 * r ** 2
#     if erea > 1000:
#         print(f"半径为{r}的圆的面积:{erea}")  # 格式化输出
#         break # 第一个大于1000的半径值

# 游戏案例
# while True:
#     print("""
# 进去第一关:
# 选择:
#     1.攻击
#     2.购买装备
#     """)
#     choice = input("请输入你的选择:")
#     # 分支判断
#     if choice == "1":
#         print("攻击..")
#     elif choice == "2":
#         print("购买装备...")
#     # 引导用户是否继续
#     choice2 = input(
#         """
#         1.回到第一关
#         2.退出游戏
#         3.继续
#         """
#     )
#     if choice2=="1":
#         continue
#     elif choice2=="2":
#         break
#
#     print("""
#     进去第二关:
#     选择:
#         1.前进
#         2.查看地图
#         3.回城
#         """)
#     choice3 = input("请输入你的选择:")
#     # 分支判断
#     if choice3 == "1":
#         print("前进..")
#     elif choice3 == "2":
#         print("查看地图...")
#     elif choice3 == "3":
#         print("回城...")
#     break
# print("process end")
# 京牌摇号小程序
# 1.允许用户最多选择3次
# 2.每次放出20个车牌号
# 3.京[A-Z]-[xxxxx],可以是数字和字母在组合
import random
import string

#
# Upper_word = string.ascii_uppercase
# digits_word = string.digits
# all_charts = Upper_word + digits_word
#
# s = ""
# chepai = ""
# cishu = 0
# while cishu < 3:
#     print(
#         """
#     1.随机生成20个车牌
#     2.退出
#         """
#     )
#     choice = input("请输入你的选择:")
#     if choice == "1":
#         for j in range(1, 21):
#             for i in range(1, 6):
#                 rand_Upper = random.choice(Upper_word)
#                 rand_charts = random.choice(all_charts)
#                 s += rand_charts
#                 if i == 5:
#                     chepai = f"京{rand_Upper}-{s}"
#                     s = ""
#             print(chepai)
#         cishu += 1
#     else:
#         break

count = 0
while count < 3:
    car_nums = []
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase)
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num)
        print(i + 1, c_num)
    choice1 = input("请输入你喜欢的号码:").strip()
    if choice1 in car_nums:
        print(f"恭喜获的您的号码:{choice1}")
        exit("Good luck!")
    else:
        print("不合法的选择")
    count += 1
