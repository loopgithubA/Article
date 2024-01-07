# # alex落地问题
# height = 100  # 原始高度
# distance = 0  # 和
# for i in range(10):
#     # 将下落的高度加入到总和中
#     distance += height
#     if i == 9:
#         break
#     # 计算反弹高度
#     height /= 2
#     # 将反弹高度计入总和
#     distance += height
#     # if i == 9:
#     #     distance -= height
# print(f"共经历了{distance}米")


# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j > i:
#             break
#         print(f"{i}*{j}={j * i}", end="\t")
#     print()

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i}*{j}={j * i}", end="\t")
#     print() # end=\n” 相当于换行了

# 年会抽奖
# import random
#
# staff_list = []
# level = [30, 6, 3]  # 从0 开始
# for i in range(1, 301):
#     staff_list.append(f"员工{i}")
#
# for j in range(3):
#     lucky_people = random.sample(staff_list, level[j])
#     for winner in lucky_people:  # 去除中奖的人  将lucky_people中的每一个数据拿出来，再去除
#         staff_list.remove(winner)  # 如果直接 remove ，不是【a b c】  去除【b，c】
#         # a ！= 【b，c】  b!=[b,c] c!=[b,c];所以说找不到；如果【a b c [b c]】 则可以去除
#     print(f"恭喜获得{3 - j}等奖：{lucky_people}")
#     print(f"还剩{len(staff_list)}个人未中奖")

"""
生成一副扑克牌，分为花色 和点数
"""
_花色_ = ["黑桃", "红桃", "方片", "梅花"]
_点数_ = ["A", "2", "3", "4", "5", "6", "7", "9", "10", "J", "Q", "K"]
puke_0 = []
for puke_花色 in _花色_:
    for puke_点数 in _点数_:
        puke = puke_花色 + puke_点数
        puke_0.append(puke)
import random

# 给5个玩家发牌
shoupais = []
wanjia = []
for i in range(0, 5):
    shoupais = random.sample(puke_0, 3)
    wanjia.append(shoupais)
    for shoupai in shoupais:
        # 豹子最大：三张一样的数字666pop
        digit = shoupai.pop()
        puke_0.remove(shoupai)
