# {一对一对的数据 就叫字典}  {一个一个的数据就叫集合}
# five_men_fight_bg = {"ian", "alex", "佩奇", "志哥"}
# happy_day = {"ian", "刘诗诗", "佩奇", "柳岩"}
# print(five_men_fight_bg)  # 没有顺序
# print(type(five_men_fight_bg))
# print(five_men_fight_bg[0])# 索引就会报错

# # 找出同时参演两部电影的人  交集
# print(five_men_fight_bg.intersection(happy_day))
# print(five_men_fight_bg & happy_day)
# # 两个电影一共多少人   并集
# print(five_men_fight_bg.union(happy_day))
# print(five_men_fight_bg | happy_day)
# # 参演了five 没有参演happy  差集
# print(five_men_fight_bg.difference(happy_day))
# print(five_men_fight_bg - happy_day)
# # 只参演了一部电影   交叉补集
# print(five_men_fight_bg.symmetric_difference(happy_day))
# print(five_men_fight_bg ^ happy_day)

# set1 = {1, 2, 3, 4, 6, 7, 8, 8, 8, 8, 8, 8, 1, 2, 2, 3, 4}
# print(set1)  # 12345678  无重复值

# # 列表 list
# alex = [1, 2, 3, 4, 5, 6, 7, 8, 6, 6, 6, 6, 6, 6, 6]
# print(alex)
# alex_set=set(alex)# 去除了重复值
# print(alex_set)

"""
流畅控制结构
1.顺序结构  基本结构
2.选择结构 分支结构 条件语句-判断
3.循环结构--重复执行某些代码
"""

# 状态的标记 灯的开关（开/关）  标记（或者/嘎）
# 暗号 秘书  12345： 一切正常  其他：出事了
anhao = 12345

# 循环嵌套
# 第一层循环 楼层号
for floor in range(1, 6):  # for 临时变量 in 范围 :   冒号不能掉！！！！
    print(f"欢迎来到第{floor}层")
    # if 条件：
    if floor == 3:
        print("警告牌：Alex与狗禁止入内~~！")
        continue
    # 第二层循环控制 房间号
    for room in range(1, 9):
        print(f"{floor} 0 {room}")
        if floor == 4 and room == 4:
            print("我还会回来的")
            anhao = 666   # 把anhao一改，前面判断是否 就直接break跳出最近的循环 就进入不了第五层
            break  # 直接跳出循环 后面的405 406  都没了  然后继续下面的if
    if anhao != 12345:
        print("ian:你不用回来了")
        break

# 循环控制保留字 ： 智能控制离他 【最 近 的 一 层 循 环】！！！！
# contimue  跳出本次循环，直接开始下一次
# break 直接跳出循环

import random

first = []
second = []
third = []
people = []
# 生成员工列表1-300
for i in range(1, 301):
    people.append(i)

# 第一次抽奖
for j in range(1, 31):
    x = random.choice(people)
    third.append(x)
    j += 1

print("恭喜获得三等奖：三斤苹果", third)
del people[x]

# 第二次抽奖
for k in range(1, 7):
    x = random.choice(people)
    second.append(x)
    k += 1

print("恭喜获得二等奖：iPhone14", second)
del people[x]

# 第三次抽奖
for l in range(1, 4):
    x = random.choice(people)
    first.append(x)
    l += 1

print("恭喜获得一等奖：泰国五日游+手术费报销", first)
del people[x]