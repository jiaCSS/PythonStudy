# creating a calculator


# def add(num1, num2):
#     result = num1 + num2
#     print("the addtion is : ", result)
#     return result

# def sub(num1, num2):
#     result = num1 - num2
#     print("the subtraction is : ", result)
#     return result

# def mul(num1, num2):
#     result = num1 * num2
#     print("the diviction is : ", result)
#     return result

# def div(num1, num2):
#     result = num1 / num2
#     print("the diviction is : ", result)
#     return result


# while True:
#     num1 = int (input("numb 1: "))
#     num2 = int (input("numb 2: "))
#     op = input("operator: ")
    
#     if op =="+":
#         add(num1, num2)
#     elif op =="-":
#         sub(num1, num2)
#     elif op =="*":
#         mul(num1, num2)
#     else:
#         div(num1, num2)
    
#     continue_calculator = input("more operation to do? yes, no")
#     if continue_calculator =="yes":
#         True
#     else:
#         False   
   


# def formate_name(first, last):
#     print(first.title())
#     print(last.title())

# formate_name("jia", "ken")

# title()is already a return function

def formate_title(first, last):
    first_name = first.title()
    last_name = last.title()
    print(first_name, last_name)
    return first_name, last_name

formate_title("jia", "ken")

def is_leap(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year % 400 == 0:
                print("leap year")
                return True
            else:
                print("not leap year")
                return False
        else:
            print("leap year")
            return True
    
    else:
        print("not leap year")
        return False
    
    
    
# is_leap(2000)

def days_in_month(year, month):
    month_days = [31, 28, 31,30,31,30,31,31,30,31,30,31]
    days = 0
    if month == 2:
        
        if is_leap(year) == True:
            days = 29
            print(year, "is leap year" and "have: ", days)
            return days
        else:
            days = month_days[month-1]
            print(year, "is not leap year",  "have: ", days)
            return days
    else:
        days = month_days[month -1]
        return days
    
days = days_in_month(2022, 2)
     