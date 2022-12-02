MENU = {   
    "espresson": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.4,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}


report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0,
}


def report_fun(report):
    for key in report:
        value = report[key]
        if key =='Water' or key == 'Milk':
            print(f"{key}, {value}ml")
        elif key == 'Coffee':
            print(f"{key}, {value}g")
        else:
            print(f"{key}, {value}")
 

def sufficient_inredients (report, MENU):
    
    report_water = report["Water"]
    report_milk = report["Milk"]
    report_coffee = report["Coffee"]
    
    
    espresson_water =MENU["espresson"]["ingredients"]["water"]
    latte_water =MENU["latte"]["ingredients"]["water"]
    cappuccino_water =MENU["cappuccino"]["ingredients"]["water"]
    
    espresson_coffee = MENU["espresson"]["ingredients"]["coffee"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    if report_water < espresson_water or report_water < latte_water or      report_water < cappuccino_water:
        print("do not have sufficient water")
        return False
        
    
    elif  report_coffee < espresson_coffee or report_coffee < latte_coffee or report_coffee < cappuccino_coffee:
        print("do not have sufficient coffee")
        return False
        
    elif  report_milk < latte_milk or report_milk < cappuccino_milk:
        print("do not have sufficient milk")
        return False
    
    else:
        # print("continue order")
        return True
     
def sufficient_money(quarters, dimes, nickles, pennies, MENU):
    total = quarters *0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    cappuccino_cost = MENU["cappuccino"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    espresson_cost = MENU["espresson"]["cost"]

    return total
        


    
chosen = input("what would you like? espresson/latte/cappuccino: ").lower()
print("please insert coins: ")
quarters = float(input("how many quarters? : "))
dimes = float(input("how many dimes? : "))
nickles = float(input("how many nickles? : "))
pennies = float(input("how many pennies? : "))


def choice_function (chosen, MENU, report):
    
    espresson_water =MENU["espresson"]["ingredients"]["water"]
    espresson_coffee = MENU["espresson"]["ingredients"]["coffee"]
    espresson_cost = MENU["espresson"]["cost"]
    
    latte_water =MENU["latte"]["ingredients"]["water"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_cost = MENU["latte"]["cost"]
    
    cappuccino_water =MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    
    insert_total = sufficient_money(quarters, dimes, nickles, pennies, MENU)
    inredients = sufficient_inredients(report, MENU)
    
    if chosen == "espresson":
        
        if insert_total >= espresson_cost and inredients ==True :
            
            water_left = report["Water"] - espresson_water
            report["Water"] = water_left
            print(water_left)

            coffee_left = report["Milk"] - espresson_coffee
            report["Coffee"] = coffee_left
            print(coffee_left)
            change = insert_total - espresson_cost
            report ["Money"] = espresson_cost
            report_fun(report)
            
            print(f"here is ${change} in change \nhere is your {chosen} enjoy!")
        
        else:
            if insert_total < espresson_cost:
                money_need = espresson_cost - insert_total
                print(f"you need put ${money_need} to order {chosen} coffee")
            elif inredients ==False:
                print(" do not have enough ingredients")
        
    elif chosen == "latte":
        
        if insert_total >= latte_cost and inredients ==True:

            water_left = report["Water"]-latte_water
            report["Water"] = water_left
            print(water_left)
            
            milk_left = report["Milk"]-latte_milk
            report["Milk"] = milk_left
            print(milk_left)
            
            coffee_left = report["Coffee"]-latte_coffee
            report["Coffee"] = coffee_left
            print(coffee_left)
            report_fun(report)
        
        else:
            print("please put enough money or ingrediants")      
            
    else:
        
        if insert_total >= latte_cost and inredients ==True:
        
            water_left = report["Water"]-cappuccino_water
            report["Water"] = water_left
            print(water_left)
            
            milk_left = report["Milk"]-cappuccino_milk
            report["Milk"] = milk_left
            print(milk_left)
            
            coffee_left = report["Coffee"]-cappuccino_coffee
            report["Coffee"] = coffee_left
            print(coffee_left)
            report_fun(report)

        else:
            print("please put enough money or ingrediants")      

choice_function(chosen, MENU, report)