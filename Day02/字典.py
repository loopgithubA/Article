# """
# {} 表示字典
# 键值之间用：隔开   键值对用，隔开   ; 值可以是任意python中的类型   数 字符串 集合 字典都可以
# eg： { "color": "green"  , "point": 5  }
# """
# # 访问键值对
# alien_0 = {"color": "green", "points": 5}
# new_point = alien_0["points"]
# print(f"You just earned {new_point} points!")
#
# # 添加键值对
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)
#
# # 修改字典中的值
# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}")
#
# alien_1 = {'x_position': 0, "y_position": 25, "speed": "medium"}
# print(f"Original position is {alien_1['x_position']}")
# alien_1["speed"] = "fast"
# # 向右移动外星人
# # 根据当前速度确定外星人能够移动多远
# if alien_1["speed"] == "slow":
#     x_increment = 1
# elif alien_1["speed"] == "medium":
#     x_increment = 2
# else:
#     x_increment = 3
#     # 新位位置旧位置加上移动距离
# alien_1["x_position"] = alien_1["x_position"] + x_increment
# print(f"New position :{alien_1['x_position']}")
#
# # 删除键值对
# """
# del 字典名【“键”】  将键值对全部删除 删除的键值对会永远消失
# """
#
# print(alien_0)
# del alien_0["points"]
# print(alien_0)
#
# """
# 用 get( 指定键  ， 指定键不存在时返回的值  )  在指定的键不存在时返回一个默认值
# 如果指定的键 不存在则考虑使用 get()方法
#
# """
# #  alien_0["points"]# 会报错，因为字典中没有point 的键值对
# point_value = alien_0.get("point", "No point value assigned.")
# print(point_value)

# people = {
#     'first_name': 'liu',
#     'last_name': 'rui',
#     'age': 18,
#     'city': 'Wuhan'
# }
# print(people)
#
# favorite_numbers = {
#     'mandy': 42,
#     'micah': 23,
#     'gus': 7,
#     'hank': 1_000_000,
#     'maggie': 7,
# }
# num = favorite_numbers['mandy']
# print(f"Mandy's favorite number is {num}.")
# num = favorite_numbers['micah']
# print(f"Micah's favorite number is {num}.")
# num = favorite_numbers['gus']
# print(f"Gus's favorite number is {num}.")
# num = favorite_numbers['hank']
# print(f"Hank's favorite number is {num}.")
# num = favorite_numbers['maggie']
# print(f"Maggie's favorite number is {num}.")

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
# }
# word = 'string'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'comment'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'list'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'loop'
# print(f"\n{word.title()}: {glossary[word]}")
# word = 'dictionary'
# print(f"\n{word.title()}: {glossary[word]}")

# """
#     遍历字典
# 1. 遍历 键 and 值
# 2.遍历  键 or 值
# """
# for key, value in favorite_numbers.items():  # 声明两个变量（见名知意）来储存字典中的键和值   items（）用来获取键和值
#     print(f"\nKey:{key}")
#     print(f"Value:{value}")
#
# for name in favorite_numbers.keys():
#     print(name.title())
#
# """
# for name in favorite_numbers:  # 默认遍历键
#     print(name.title())
# """
# friends = ["mandy", "micah", "gus"]
# for name in favorite_numbers.keys():
#     print(f"Hi,{name.title()}")
#     if name in friends:
#         num = favorite_numbers[name]  # 将 name 的当前值 当作键
#         print(f"\t{name.title()},I see you love {num}")
# # 还可以使用 key（）确认某人是否接受了调查
# if "liurui" not in favorite_numbers.keys():
#     print("\nLiuRui,please take our pool")

# 按照特定的顺序遍历字典中的所有键  sorted()
# for name in sorted(favorite_numbers.keys()):
#     print(f"{name.title()},thank you for taking the pool")

# 遍历所有值

# for num in favorite_numbers.values():
#     print(num)
# """
# 这种方法是遍历所有值，不考虑重复值。
# 如果要提出重复值，可以考虑用集合set;
# 用过对包含重复原色的列表调用set（），可以找出列表中独一无二的元素，并创建一个新的集合
#
# 集合也是用{} 定义，   区别  有键值对 就是字典 ；没有键值对   就是集合
# 集合不会以特定的顺序存储元素
# """
# for num in set(favorite_numbers.values()):
#     print(num)
# for key, value in glossary.items():
#     print(f"{key.title()} : {value}")

# rivers = {
#     'nile': 'egypt',
#     'mississippi': 'united states',
#     'fraser': 'canada',
#     'yangtze': 'china',
# }
# for river, nation in rivers.items():
#     print(f"\nThe {river.title()} runs through {nation.title()}")
#
# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print(f"- {river.title()}")
#
# print("\nThe following countries are included in this data set:")
# for country in rivers.values():
#     print(f"- {country.title()}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
# print("\n")
#
# coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle'] # 有些人已在字典中 有些人不在字典中
#
# for coder in coders:
#     if coder in favorite_languages.keys():
#         print(f"Thank you for taking the poll, {coder.title()}!")
#     else:
#         print(f"{coder.title()}, what's your favorite programming language?")
#
# """
# 列表中包含众多字典，每个字典包含特定对象的众多信息
# """
# # 创建一个用于存储外星人的空列表
# aliens = []
# # 创建30个绿色的外星人
# for alien_numbers in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)
#
# # 将前三个外星人修改为黄色  ； 速度中等    ； 分值10
# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["point"] = 10
#         alien["speed"] = "medium"
#     elif alien["color"] == "yellow":
#         alien["color"] = "red"
#         alien["point"] = 15
#         alien["speed"] = "fast"
#
# # 显示前5个外星人
# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# # 显示创建了多少个外星人
# print(f"Total number of aliens {len(aliens)}")
#
# """
# 当需要在字典中“”“”将一个键关联到多个值“”“”的时候，可以在字典中嵌套一个列表
# """
#
# """
# 字典中可以嵌套字典
# """
#
# # 创建一个用于存储人的空列表
# people = []
# # 定义一些人并将他们添加到前述列表中
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 46,
#     'city': 'sitka',
# }
# people.append(person)
# person = {
#     'first_name': 'lemmy',
#     'last_name': 'matthes',
#     'age': 2,
#     'city': 'sitka',
# }
# people.append(person)
# person = {
#     'first_name': 'willie',
#     'last_name': 'matthes',
#     'age': 11,
#     'city': 'sitka',
# }
# people.append(person)
# # 显示列表包含的每个字典中的信息
# for person in people:
#     name = f"{person['first_name'].title()} {person['last_name'].title()}"
#     age = person['age']
#     city = person['city'].title()
#     print(f"{name}, of {city}, is {age} years old.")
#
# # 创建一个用于存储宠物的空列表
# pets = []
# # 定义各个宠物并将其存储到列表中
# pet = {
#     'animal type': 'python',
#     'name': 'john',
#     'owner': 'guido',
#     'weight': 43,
#     'eats': 'bugs',
# }
# pets.append(pet)
# pet = {
#     'animal type': 'chicken',
#     'name': 'clarence',
#     'owner': 'tiffany',
#     'weight': 2,
#     'eats': 'seeds',
# }
# pets.append(pet)
# pet = {
#     'animal type': 'dog',
#     'name': 'peso',
#     'owner': 'eric',
#     'weight': 37,
#     'eats': 'shoes',
# }
# pets.append(pet)
# # 显示每个宠物的信息
# for pet in pets:
#     print(f"\nHere's what I know about {pet['name'].title()}:")
#     for key, value in pet.items():
#         print(f"\t{key}: {value}")

# favorite_places = {
#     'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
#     'erin': ['hawaii', 'iceland'],
#     'willie': ['mt. verstovia', 'the playground', 'new hampshire']
# }
#
# for f_name, places in favorite_places.items():
#     print(f"\n{f_name} `s favorite places is :")
#     for place in places:
#         print(f"- {place}")
#
# favorite_num = {
#     "mary": [1, 2, 3, 4],
#     "liu": [3, 6, 8, 9],
#     'chen': [12, 34],
#     "xun": [4, 5]
# }
# for name, nums in favorite_num.items():
#    print(f"{name}'s favorite number is :")
#    for num in nums:
#        print(f"- {num}")
#
#
# cities = {
#     'santiago': {
#         'country': 'chile',
#         'population': 6_310_000,
#         'nearby mountains': 'andes',
#     },
#     'talkeetna': {
#         'country': 'united states',
#         'population': 876,
#         'nearby mountains': 'alaska range',
#     },
#     'kathmandu': {
#         'country': 'nepal',
#         'population': 975_453,
#         'nearby mountains': 'himilaya',
#     }
# }
# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population']
#     mountains = city_info['nearby mountains'].title()
#     print(f"\n{city.title()} is in {country}.")
#     print(f" It has a population of about {population}.")
#     print(f" The {mountains} mounts are nearby.")



