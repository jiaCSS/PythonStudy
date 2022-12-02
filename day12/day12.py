import random
chosen_num = random.randint(1, 101)
print(chosen_num)
print("Welcome to the number guessing game!")
print("think of a number between 1 and 100")
difficulty = input("choose a difficulty, easy or hard: ")
def guessing_game(chosen_num, difficulty):
    # attemps = 0
    if difficulty == "easy":
        for attemps in reversed(range(10)): 
            guess = int(input("make a guess: "))
            if guess > chosen_num:
                print("too height ")
                print(f"you have {attemps}attemps ")
            elif guess < chosen_num:
                
                print("too low")
                print(f"you have {attemps}attemps ")
            else:
                print("You get right")
                break
    else:
        for attemps in reversed(range(5)): 
            guess = int(input("make a guess: "))
            if guess > chosen_num:
                print("too height ")
                print(f"you have {attemps}attemps ")
            elif guess < chosen_num:
                
                print("too low")
                print(f"you have {attemps}attemps ")
            else:
                print("You get right")
                break

guessing_game(chosen_num, difficulty)    
    
