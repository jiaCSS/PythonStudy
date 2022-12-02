# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# print("this is jia again and study python for day 1")
#
#
# name = input("what is your name")
#
# print(name + ", your name has ")
# print(len(name))

# a = input("a: ")
# b = input("b: ")
# a, b = b, a
# print(a)
# print(b)

d = [0,5,4,9,-10]
print(d)
print(sorted(d))

d[0], d[1] = d[1], d[0]
print(d)
print(sorted(d))
print(sorted(d, reverse=True))

time_until = "5"
print("this are " + time_until + " hours until midnight")
print("this are "+time_until+" hours until midnight")

# city = input("what is name of the city you grew up in?")
# petname = input("what is your pet's name?")
# print(city)
# print(petname)
# print("your band name could be:" + city + " " + petname)



# c = a
# print("c is : " + c)
# a = b
# print("a is : " + a)
# print("b is : " + b)
# b = c
# print("c is :" + c)
# print("b is :" + b)

# day2
# print("welcome to the tip calculator")
# bill = input("what was the total bill?")
# convert_bill = int(bill)
# person = input("how many people to split the bill?")
# convert_person = int(person)
#
# tip = input("what percentage tip would you like to give? 10, 12, or 15?")
# convert_tip = int(tip)
#
# each_person = (convert_bill+(convert_bill*convert_tip/100))/convert_person
#
# new_person = str(each_person)
# print("each person should pay: " + new_person)
print("hello"[0])
print("123" + "456")
print(132+456)
print(123_456_456_9)
print(float(3.256))

# length = len("123")
# print(length)
#
# num1 = 20
# num2 = 30
# string_num1 = str(num1)[0]
#
# input_num = input("please input a two digits number: ")
# convert_input_num = int(input_num)
# total = int(input_num[0]) + int(input_num[1])
# convert_sum = str(total)
# print(convert_sum)

name = "geek"
# for i in name:
#     print(i, end=' ')
# print("\n")
# for v in range(0, len(name)):
#     print(name[v])
#
# print("\n")
#
# # using enumerate()
# for i, g in enumerate(name):
#     print(g)
#
# print("\n")

# for element in name[::1]:
#     print(element)

# for ele in range(0, len(name)):
#     print(name[ele])

# for ele in range(0, 4)[::-1]:
#     print(name[ele])
#
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = round(int(weight)/pow(float(height), 2), 2)
#
# print("your bmi is: " + str(bmi))
#
# print(f"your bmi is {height}, {bmi}")

# input_year = input("what is your current age?")
# print(input_year)
#
# left_days = (90 - int(input_year))*365
#
# left_weeks = (90 - int(input_year))*52
#
# left_months = (90-int(input_year))*12
#
# print(f"You have {left_days}days, {left_weeks} weeks, and {left_months} months left.")


# numb = input("enter a number: ")
# if int(numb) % 2 == 0:
#     print("your number is even")
# else:
#     print("your number is old")

# hei = input("enter your height in cm: ");
# if int(hei) >= 120:
#     print("you can ride the rollercoaster!")
#     age = int(input("what is your age?"))
#     if age <= 12:
#         print("please pay $5.")
#     elif age <= 18:
#         print("please pay $8")
#     else:
#         print("pay $12")
# else:
#     print(" you are not taller enough to rollercoaster")


# year = int(input("which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
#
# else:
#     print("this is not leap year")
#
# height = int(input("enter your height in cm: "))
# bill = 0
#
# if height > 120:
#     print("you are qualified going rollercoaster")
#     age = int(input("enter your age: "))
#     if age < 12:
#         bill = 5
#     elif age < 18:
#         bill = 7
#     else:
#         bill = 12
#
#     photo = input("do you want to take photos, y: yes, n: no")
#     if photo =="y":
#         bill += 3
#         # print(f"your bill is {bill}")
#     print(f"your total bill is {bill} ")
#
# else:
#     print("you are not taller enough")

# print(" welcome to python pizza deliveries!")
# size = input("what size pizza do you want? S, M, L")
# add_pepperoni = input("do you want peperoni? Y, N")
# extra_cheese = input("do you want extra cheese? Y, N")
#
# bill = 0
#
# if size == "S":
#     bill = 15
#     if add_pepperoni == "Y":
#         bill += 2
#     if extra_cheese == "Y":
#         bill += 1
#
# elif size == "M":
#     bill = 20
#     if add_pepperoni == "Y":
#         bill += 3
#     if extra_cheese == "Y":
#         bill += 1
# else:
#     bill = 25
#     if extra_cheese == "Y":
#         bill += 1
#
# print(f"you total bill is {bill}")
# print("this is jia again")
# num1 = input("the first name: ")
# num2 = input("the second name: ")
# name = num1.lower() +num2.lower()

# t = name.count("t")
# r = name.count("r")
# u = name.count("u")
# e = name.count("e")

# true = t+r+u+e
# print(true)
# print(type(true))


# l=name.count("l")
# o=name.count("o")
# v=name.count("v")
# love = l+o+v

# total = true + love
# percentage = total / len(name)*100
# print( f"your total score is : {percentage}" )

# if percentage >10 and percentage <40:
#     print("your are not ok")
# elif percentage >50 and percentage<80:
#     print("you are ok")
# else:
#     print("you are super")

# fruit = ["apple", "pears", "ban   ana"]
# veges = ["spinach", "kale", "cabage"]
# people = ["Jia", "nellie", "Ken"]

# together = [fruit, veges, people]
# print(together)
# print(together[0])
# print(together[1])
# print(together[0][1])
# position = input("where do you want to put treasure")
# horizontal = int(position[0])
# vertical = int(position[1])

# # seclected_row = together[vertical -1]
# # seclected_row[horizontal-1] = "X"

# together[horizontal-1][vertical-1] ="X"
# print(f"{fruit}\n{veges}\n{people}")

# import random
# ran1 =int(input("please input number: type 0 for rock, 1 for paper, 2 for scissors"))
# ran2 = random.randint(0, 2)
# print(ran2)
# if ran1 >= 3 or ran1 <= 0:
#     print("this is invalid ")
# elif ran1 ==0:
#     if ran2 ==0:
#         print("no one wins")
#     elif ran2 ==1:
#         print("ran2 is the winner")
#     else:
#         print("ran1 wins")
# elif ran1 ==1:
#     if ran2 == 0:
#         print("ran1 wins")
#     elif ran2 ==1:
#         print("no one wins")
#     else:
#         print("ran2 wins")
# else:
#     if ran2 ==0:
#         print("ran2 wins")
#     elif ran2 == 1:
#         print("ran2 wins")
#     else:
#         print("no non wins")
    
# day 5 loop
# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)

# avg = 0
# total = 0
# number_students = 0
# for height in student_heights:
#     total += height
#     print(total)

# for student in student_heights:
#     number_students += 1
#     print(number_students)

# student_heights = [180, 160,178,190,180,185,175]

# heightest_student = 0
# for height in student_heights:
#     if height > heightest_student:
#         heightest_student = height
# print(heightest_student)

# # for number in range(1, 10)
# for numnber in range(1, 10, 2):
#     print(numnber)

# total =0 
# for number in range( 1, 10):
#     total += number
# print(total)

# sum = 0

# for number in range ( 2, 101, 2):
#     sum += number
#     print(number)
# print(sum)

# sum1 = 0 
# for number in range ( 1, 101):
#     if number  % 2 ==0:
#         sum1 +=number
# print(sum1)
# count = 0
# for number in range ( 1, 101):
#     if  number % 5 == 0 and number % 3 == 0:
#         count+= 1
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0 :
#         print ("Buzz")
#     else:
#         print(number)
# print(count)


import random
import string

# letter = chr ( random.choices(ord("a"), ord("z")))
# print(letter)

# def get_random_password (length):
#     letters = string.ascii_lowercase
#     result_str = ' '.join(random.choice(letters)  for i in range(length))
#     print(result_str)

# def get_password(length):
#     result_str = ' '.join(random.choice(string.ascii_letters)  for i in range(length))
#     print(result_str)

# get_password(14)
# get_random_password(14)

# letters = ' '
# for i in random.choice(string.ascii_letters):
#     letters += i
#     print(letters)
    
# for i in range ( 14 ):
#     letters = random.choice(string.ascii_letters)
#     # print(letters)
#     join_str = " ".join(letters)
#     print(join_str)
    
letters1 = random.choice(string.ascii_letters)
print(letters1)

letters = " "
result_str = " "

random_list = [" ".join(random.choice(string.ascii_letters)  for i in range (14))]

print(random_list)
import random
import string

symbols = ['!', "*", '&', '^', '%', '#']
letters = ['a', 'b', 'c', 'd', 'e', 'f']
numbers = ['1', '2', '3']


number = random.sample(numbers, 2)
letter = random.sample(letters, 2)
symbol= random.sample(symbols, 4)
join = number + letter+symbol
print(join)
joins = random.sample(join, 8 )
print(joins)

# teacher's veision

password = ""

for char in range ( 1, 5):
    password += random.choice(letters)
for char in range ( 1, 3):
    password += random.choice(symbols)
for char in range ( 1, 3):
    password += random.choice(numbers)
    
    
password_list = []
for char in range ( 1, 5):
    password_list += random.choice(letters)
for char in range ( 1, 3):
    password_list += random.choice(numbers)
for char in range ( 1, 3):
    password_list += random.choice(symbols)

print(password_list)   
# change a list to string
random.shuffle(password_list)

password_str = ""

for char in password_list:
    password_str += char
# print(password_str)



# randomize password list 



# avg = int(total / len(student_heights))
# avg = round(total / len(student_heights), 2)
# avg = int( total / number_students)
# print(f"average of students is : {avg}")







