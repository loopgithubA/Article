# cars = ["audi", "bmw", "subaru", "toyota"]  # bmw 全大写，其他的首字母大写
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())
# pytho 默认区分大小写，即：Audi==audi   ？   答案是False

# car = "Audi"
# car.lower() == "audi"  # True   注意 lower（）不会修改原来car的值，因此car=“Audi”

# alien_color = ["green", "yellow", "red"]
# for color in alien_color:
#     if color=="green":
#         print("恭喜玩家获得5分")
#     else:
#         print("未通过测试")

# alien_color = "green"
# if alien_color=="green":
#     print("由于玩家射杀外星人获得5分")
# else:
#     print("玩家获得10分")
#
# alien_color="red"
# if alien_color=="green":
#     print("由于玩家射杀外星人获得5分")
# else:
#     print("玩家获得10分")
#
# alien_color = "green"
# if alien_color == "green":
#     mark = 5
# elif alien_color == "yellow":
#     main = 10
# else:
#     mark = 15
# print(f"玩家获得{mark}分")

# alien_color = "yellow"
# if alien_color == "green":
#     mark = 5
# elif alien_color == "yellow":
#     mark = 10
# else:
#     mark = 15
# print(f"玩家获得{mark}分")
#
# alien_color = "red"
# if alien_color == "green":
#     mark = 5
# elif alien_color == "yellow":
#     mark = 10
# else:
#     mark = 15
# print(f"玩家获得{mark}分")
# age = 18
# if age < 2:
#     print("You're a baby!")
# elif age < 4:
#     print("You're a toddler!")
# elif age < 13:
#     print("You're a kid!")
# elif age < 18:
#     print("You're a teenager!")
# elif age < 65:
#     print("You're an adult!")
# else:
#     print("You're an elder!")

# favorite_fruits = ['blueberries', 'salmonberries', 'peaches']
# if 'bananas' in favorite_fruits:
#     print("You really like bananas!")
# if 'apples' in favorite_fruits:
#     print("You really like apples!")
# if 'blueberries' in favorite_fruits:
#     print("You really like blueberries!")
# if 'kiwis' in favorite_fruits:
#     print("You really like kiwis!")
# if 'peaches' in favorite_fruits:
#     print("You really like peaches!")

# if 的条件是一个列表时，当列表为空列表  则 相当于False ；至少含有一个元素 则True
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure to want a plain pizza?")

# available_toppings = ["mushroom", "olives", "green peppers", "pineapple"]
# requested_toppings = ["mushroom", "fresh fries", "extra cheese"]
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry,we dom't have {requested_topping}")
#
# print("\nFinished making your pizza!")

# user_list = ["admin", "liurui", "liujianxun", "huangbenxi", "liunian"]
# for user in user_list:
#     if user == "admin":
#         print("Hello admin,would you like to see a status report?")
#     else:
#         print(f"Hello {user},thank you for logging in again.")

# usernames = []
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print(f"Hello {username}, thank you for loggin in again!")
# else:
#     print("We need to find some users!")

# current_users = ["Admin", "liurui", "liujianxun", "huangbenxi", "liunian"]
# new_users = ['admin', 'Willie', 'PHIL', 'liujianxun', 'Iona']
# # current_users_lower=[user.lower() for user in current_users]
# current_users_lower = []
# for users in current_users:
#     current_users_lower.append(users.lower())
#
# for user in new_users:
#     if user.lower() in current_users_lower:
#         print("用户名已被使用，请输入其他用户名")
#     else:
#         print("该用户名未被使用")

# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
# current_users_lower = [user.lower() for user in current_users]  # 不区分大小写 也就是说 John 和 JOHN 是一样的
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:  # 将new_user  小写
#         print(f"Sorry {new_user}, that name is taken.")
#     else:
#         print(f"Great, {new_user} is still available.")

# math = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in math:
#     if i == 1:
#         tail = "1st"
#     elif i == 2:
#         tail = "2nd"
#     elif i == 3:
#         tail = "3rd"
#     else:
#         tail = str(i) + "th"
#     print(tail)
#
# numbers = list(range(1, 10))
# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     else:
#         print(f"{number}th")
