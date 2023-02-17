# is_old = False
# age = 25
# is_licenced = True
# if age >= 20 and is_licenced:
#     is_old = True
#     print("you can drive now!")
# elif age < 20:
#     print("You are can not drive you are of age")
# elif not is_licenced:
#     print("you are not licenced please get yours first")
# else:
#     print("you can not dive at the moment!")
#     print("Hello")
# ############################################ Truthy & Falsely
# password = "Hello2222"
# username = "user1"
# if password and username:
#     print(f"Welcome back username {username} again ! ")
# else:
#     print("username or password is not correct !!")
# ###########################################Ternary Operator
# condition_if_true if condition else condition_if_false
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"
# print(can_message)
# ###########################################Short Circuiting
# is_friend = True
# is_User = False
# if is_friend and is_User:
#     print("best Friends for ever")
# elif is_User or is_friend:
#     print("Hello man")
# else:
#     print("not Friends")
# ##########################################Logical Operators
# print(4 == 5)
# print(4 > 5)
# print(4 < 5)
# print(4 >= 5)
# print(4 <= 5)
# print(5 != 5)
# print('a' > 'A')  # convert alphabets into nums
# ######################################### Excercise
# is_magician = False
# is_expert = True
# if is_magician and is_expert:
#     print("you are a master magician")
# elif is_magician and not is_expert:
#     print("at least you `re getting there")
# elif not is_magician:
#     print("you need magic powers")
# print(True == 1) # == checks for the value and datatype if implicit cast-able
# print('1' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])
# print([1, 2, 3] is [1, 2, 3])  # is checks for the location in memory
# print([1, 2, 3] == [1, 2, 3])  # is checks for the location in memory
# print('1' is '1')  # is checks for the location in memory
# print([1, 2, 3] == [1, 2, 3])
# ######################################################## Loops
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # mutable not hashable(can not be key in dict)
my_set = {1, 2, 3, 4}  # immutable not hashable(can not be key in dict)
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # immutable hashable
my_dict = {
    "name": "ayman",
    "age": 27,
    my_tuple: {10.20, 30, 40, 50, 60, 70}
}  # mutable and not hashable (can not be key in dict)
# for i in my_set:
#     print(i)
#     for x in my_dict:  # keys
#         print(x)
# for keys, values in my_dict.items():  # keys
#     print(keys, values)
# for x in my_dict.values():  # keys
#     print(x)
# #################################################### Exercise Counter
# counter = 0
# for item in my_list:
#     counter += item
# print(counter)
# #################################################### range
# for _ in range(1, 5):  # range is special type not Tuple
#     print(_)
# for _ in range(1, 5, 2):  # range(start,end,step over)
#     print(_)
# for _ in range(10, 1, -2):  # -1 reverse
#     print(_)
for _ in range(2):  # -1 reverse
    print(list(range(10)))
# ######################################################## Enumerate
