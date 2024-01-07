# favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
# for favorite_pizza in favorite_pizzas:
#     # print(favorite_pizza)
#     print(f"I like {favorite_pizza} pizza")
# print()
# print("I really like pizza\n")
#
# animals = ["spider monkey", "lemur", "giraffe"]
# for animal in animals:
#  print(animal)
# print("\n")
# # 针对每种动物打印一个句子
# for animal in animals:
#  print(f"A {animal} has a long tail.")
# print("\nAll of these animals have long tails.")

# even_numbers=list(range(1,5)) # list()将range直接转化为列表 range(start,end,step=1)
# print(even_numbers)

# # 打印1-20 含20
# numbers = list(range(1, 21))
# for number in numbers:
#  print(number)
#
# #   1-10000的列表
# numbers = list(range(1, 1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# Odd_numbers=list(range(1,21,2))
# for number in Odd_numbers:
#     print(number)

# numb = list(range(3, 31))
# num_3 = []
# for i in numb:
#     if i % 3 == 0:
#         num_3.append(i)
# print(num_3)


# threes = list(range(3, 31, 3))
# for number in threes:
#  print(number)


# cube = [value ** 3 for value in range(1, 11)]
# cubes = []
# for number in range(1, 11):
#     cube = number ** 3
#     cubes.append(cube)
# for cube in cubes:
#     print(cube)

# qiepian = ['pepperoni', 'hawaiian', 'veggie', "spider monkey", "lemur", "giraffe"]
# print(f"The first three items in the list are {qiepian[:3]}")
# print(f"Three items from the middle of the list are {qiepian[2:5]}")
# print(f"The last three items in the list are {qiepian[-3:]}")

# favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
# friend_pizzas = favorite_pizzas[:]
# favorite_pizzas.append("meat lover's")
# friend_pizzas.append('pesto')
# print("My favorite pizzas are:")
# for pizza in favorite_pizzas:
#     print(f"- {pizza}")
# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(f"- {pizza}")

# # 元组不可修改！！！！！！ 列表可以
# dimensions=(200,50)
# print(dimensions[0])
# print(dimensions[1])
# # dimensions[0]=20 会报错 ，元组不能修改  只包含一个元素的元组（3   ，   ）  ， 不能掉  元组是由逗号标识的
# for dimension in dimensions:
#     print(dimension)

# 虽然布恩那个修改元组的元素  ，但是可以给元组的变量重新赋值
# print("Origianl dimentions")
# for dimention in dimensions:
#     print(dimention)
#
# dimensions=(400,50)
# print("\nModified dimensions")
# for dimention in  dimensions:
#     print(dimention)
#

# # 自助餐
# menu_items = (
#     'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
#     'salmon burger', 'crab cakes',
# )
# print("You can choose from the following menu items:")
# for item in menu_items:
#     print(f"- {item}")
# menu_items = (
#     'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
#     'black cod tips', 'king crab legs',
# ) # 元组元素不能修改
# print("\nOur menu has been updated.")
# print("You can now choose from the following items:")
# for item in menu_items:
#     print(f"- {item}")
