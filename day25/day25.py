import pandas as pd
import csv
# with open("weather_data.csv", "r") as data_file:
#     # data = weather.read()
#     data = data_file.readlines()
#     print(data)
#     # print(data)

# with open("weather_data.csv", "r") as data_file:
#     # data = weather.read()
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != ' temp':
#             temp = row[1]
#             temp= "".join(temp.strip())
#             temperatures.append(int(temp))
#     print(temperatures)
            
        
data = pd.read_csv("weather_data.csv")
# print(data)
# print(data[" temp"])
# print(data["day"])
# temp_list = data[" temp"].to_list()
# print(len(temp_list))
# total = 0
# sum(temp_list )/len(temp_list)
# print(data[" temp"].max())
# print(data[data.day =="Monday"])
# print(type(data.day))
# print(type (data[data.day]))

print(data.temp.max())
print(data[data.day == "Monday"])
monday = data[data.day =="Monday"]
print(monday.condition)
monday.to_csv("monday.csv", index = False) 
temp_c = monday.temp
print(temp_c)
print(monday)
print(monday.condition)
print(monday.day)
print(monday.temp)
print(temp_c)
print(temp_c/1.5)

# name =input(" maddie is the best cat I have had\n")
# print(name)

# print("hello, this is jia, and what is your name?")
# name = input(" ")
# print("hello, ", name)

# print("hello  dadyy")
# name=input("")
# print("hello" , name)

print("hello maddie")
print("mrow mrow")


