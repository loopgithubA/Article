# 查询
# names = ["liu", "jian", "xun", "rui"]
# # print(names[0])
#
#
# for i in range(4):
#     # print(f"姓名：{names[i]}")
#     print(f"{names[i].title()}你好!")

# 删除 del pop remove
# guests = ['guido van rossum', 'jack turner', 'lynn hill']
#
# for i in range(3):
#     print(f"{guests[i].title()},please come to dinner!")
#
# name = f"Sorry\n{guests[0].title()} can not come to dinner!"  # guido van rossum 无法来参加
# print(name)
# # 将无法来的加冰替换为liurui
# # guests[0] = "liurui"
# del guests[0]  # 先删除后插入
# guests.insert(0, "liurui")
# print(guests)
# for j in range(3):
#     print(f"{guests[j].title()},please come to dinner!")
#
# # 添加append
# print("we have found a bigger table!")
# guests.insert(0, "liujianxun")
# guests.insert(2, "huangbenxi")
# guests.append("ducadi")
# print(guests)
#
# print("Sorry,I can only invite two people to the dinner!")
# for k in range(5):
#     not_guests = guests.pop()
#     print(f"Sorry!{not_guests},there is no room for you!")
#     if len(guests) == 2:
#         break
# print(not_guests)

# for l in range(0, 2):
#     print(f"{guests[l]},you are still in the invitation list")
#
#
# del guests[0]
# del guests[0]
#
# print(guests)

# locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']
# print(locations)
# print(sorted(locations))  # 顺序改变
# print(locations)  # 顺序未变：使用sorted（）只是暂时改变顺序
# print(sorted(locations, reverse=True))  # 按字母降序排
# print(locations)
#
# locations.reverse()  # 将列表倒过来
# print(locations)
# locations.reverse()
# print(locations)
#
# locations.sort()  # 永久改变顺序
# print(locations)
# locations.sort(reverse=True)
# print(locations)
