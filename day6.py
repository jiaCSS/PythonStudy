# print("this is jia again and study python")

# number = 6
# while number >0 : 
#     print(number)
#     number -=1
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# guess = input("guess a letter: ").lower()
display = []
print(f"passt, the solution is {chosen_word}: ")
word_length = len(chosen_word)

for _ in range(word_length):
    display += "-"
print(display)
end_of_game = False
lives = 6

while not end_of_game:
    
    guess = input("guess a letter: ").lower()
    if guess in display:
        print(f"you already guessed {guess}")
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
 
    if guess not in chosen_word:
            lives -=1
            print(f"you guessed {guess}, that is not ine the word. you lose a life you only have {lives}to live")
            if lives == 0:
                end_of_game = True
                print("you don't have any lives, you lose the game")
                # break
                  
    print(f"{ ' '.join(display)}")   

    if "-" not in display:
        end_of_game =True
        print("you win.")
        # break

