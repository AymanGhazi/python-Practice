# print((20 - 3) ** 2)
# print(int('0b101', 2))

# constants
PI = 5
PI = 10

# danders
# __import__()
# print(type(int('5')))
a, b, c = 5, 2, 3

# augmented assignment operator
user_age = 2
user_age += 10

# str
log_str = '''
hello 
WOW
O O
----
'''

first_name = 'Ayman'

# escape sequence
st = "It`s \t \"kind of\" \t Sunny \n I hope you have a good Day "
# formatted strings
user_name = "Ayman"
formatted_string = f"HI {user_name} . you are  {user_age} years old"
formatted_string2 = "HI {0} . you are  {1} years old".format(user_name, user_age)
formatted_string3 = "HI {new_name} . you are  {new_age} years old".format(new_name="Khalid", new_age=55)
# string slicing
hello = "hello"
hell = hello[0:4]
All = hello[:5]
All1 = hello[0:]
All2 = hello[::2]  # start:end:+stepOver
All3 = hello[-1]  # startEnd
All4 = hello[::-1]  # start:end: reverse order

# immutability can not be changed
selfish = "1234567"
# selfish[0] = 8 ==> Error
# length
length = selfish.__len__()  # dander method owned by string
# print(len("Hellllllo")) #functions

# booleans
is_Active = bool(1)
is_Active = bool('True')

# exercise
relationShip_status = "single"
relationShip_status = "it\'s complicated"
# print(relationShip_status)

# name = input("what is your name ? ")
# year_of_birth = input("what is your Year of Birth ? ")

# user_age = datetime.datetime.now().year - int(year_of_birth)
# password = input("what is your secret ?")
# message = f' {name} ,Your Age is {user_age} , your password is {"*" * len(password)} and password length is {len(password)} letters long '
#############################################################################################################
# list somehow is array
li = [0, 1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'd']
li3 = [1, 2, 'a', 'b', True]
# list slicing
# print(li[0::2])  # escaping one every one
# li2 = li
# li2 = li[2:]  # making a new copy of li
# li[0] = 50  # immutable
# print(li2)  # li with modifications as it refers to the same reference in memory
##############################
# matrix is like 2D Array
matrix = [
    [1, 2, 3, 4, 5, 6],
    ['a', 'b', 'c', 'd'],
    [7, 8, 9, 10, 11, 12, 13]
]
# print(matrix[0][0])
##############################
# adding
# new_list = li.append(["HI", "Hello"])  # returns none [0, 1, 2, 3, 4, 5, ['HI', 'Hello']]
# new_list = li.extend(["Hello", 101])  # returns none [0, 1, 2, 3, 4, 5, 'Hello', 101]
# new_list = li.insert(5, "Hello")  # inset at index returns none
# print(li)
# remove
# new_list = li.pop(0)
# new_list = li.remove(0)  # None and removes 0
# new_list = li.pop(0)  # 1 and removes at index 0
# li.clear()
# index
# li2.index('b', 0, 2)
# 'd' in li2  # True
# print('i' in 'Hi')
# print(li2.count('a'))
# new_list = li2.copy()
# li2.sort()  # sort the same ref
# print(sorted(new_list))  # sort and return a new List
# li2.reverse()  # sort the same ref
# print(li2[::-1])  # reverse the list like reverse method
# print(li2)
# print(list(range(1, 100)))
# sentence = "!"  # joined with every item in the list with Join
# new_sentence = sentence.join(["Hi", "my", "name", "is", "Ayman"])
# print(new_sentence)
############################## list Unpacking
a, b, c, *other = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)
# print(b)
# print(c)
# print(other)
################################ none
# weapons = None
