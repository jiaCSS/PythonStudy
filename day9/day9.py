# python dictionries and nesting

# programming_dictionary = {
#     "Bug": "adrordfddfd",
#     "best": "this is maddie",
#     "maddie": "this is maddie cat"
# }
# programming_dictionary["Bug"]

# # add more items
# programming_dictionary ["nellie"] ="this is my daugther"
# print(programming_dictionary)

# # creat an empty dictionary

# empty_dictionary = {}

# # wipe an existing dictionary
# # programming_dictionary = {}
# # print (programming_dictionary)
# bug_value = programming_dictionary["Bug"]
# print(bug_value)

# programming_dictionary ["bug"] = bug_value
# del programming_dictionary["Bug"]
# print(programming_dictionary)

# # loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
    
# student_scores = {
#     "Harry": 78,
#     "Ken": 98,
#     "Jia": 89,
#     "Maddie": 100,
# }

# student_grades = {}
# def student_grades_dic(student_scores):
    
#     for key in student_scores:
#         if student_scores[key] > 91 and student_scores[key]  <= 100:
#             student_grades[key]= "Outstanding"
#             print(student_grades)
#         elif student_scores[key] > 81 and student_scores[key] < 91:
#             student_grades[key]= "excedds expectations"
#             print(student_grades)
#         else:
#             student_grades[key]= "acceptable"
#             print(student_grades)
#     print(student_grades)
 
# student_grades_dic(student_scores)

# capitals = {
#     "France": "Pairs",
#     "German": "Berline"
# }

# travel_log = {
#     "France": ["Pairs", "Lille", "Dijon"],
#     "German": ["Berline", "Ann Arbor"]
# }

# travel_log_time = {
#     "America": {"cities_visited": ["New Yeark", "Chicago", "Sanfancsco"], "Year come to us": 2015, "living": "ann arbor", "family": ["nellie", "jia", "Ken", "Maddie"]}
# }

# value = travel_log_time["America"]["family"]
# print(value)

# # put in a list

# travel_city = [
#     {
#         "country": "France", 
#         "city_visited": ["Pairs", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "America", 
#         "city_visited": ["New Yeark", "Chicago", "Sanfancsco"], 
#         "total_visits": 2
#     }, 
    
# ]

# new_list = ("Russia", 2, ["Mosco","Petersbuge"])

# travel_city.append({})
# # print(travel_city[2])
# # print (new_list[0])

# # travel_city[2]["country"] = new_list[0]
# # travel_city[2]["city_visited"] = new_list[1]
# # travel_city[2]["total_visits"] = new_list[2]

# for var in travel_city[0]:
#     if var == "country":
#         travel_city[2][var] = new_list[0]
#     elif var =="city_visited":
#         travel_city[2][var] = new_list[2]
#     else:
#         travel_city[2][var] = new_list[1]
# print(travel_city)

# # the teacher's way

# def add_new_country(country, times_visited, cities_visited):
#     new_dict = {}
#     new_dict["country"] = country;
#     new_dict["times_visited"] = times_visited;
#     new_dict["cities_visited"] = cities_visited;
    
#     travel_city.append(new_dict)
#     print(travel_city)

# add_new_country("Russia", 2, ["ann arbor", "Chicago"])


bid_dic = {}
continue_bid = True

def bid_function(bid_dic):
    price = bid_dic[name]
    height_price = 0
    # this is important to put in the function but outside of loop, so can be used in later for loop
    for key in bid_dic:
        if height_price < price:
            height_price = price
    print(f" the winner is : {key}, the price is: {price}")

# while loop to loop through it 
while continue_bid:
    name = input("what is your name: ")
    price = int(input("what is your price: "))
    bid_dic[name] = price
    
    result = input("are there any other bidders? yes, no")
    if result =="no":
        continue_bid = False
        bid_function(bid_dic)
    else:
        continue_bid= True
