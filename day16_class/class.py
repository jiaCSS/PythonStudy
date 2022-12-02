# import turtle
# timmy = turtle.Turtle()
# timmy.color("red")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# print(timmy)
# my_screen.exitonclick()

# class User:
#     def __init__(self, user_id, user_name):
#         self.user_id = user_id
#         self.user_name = user_name
#         self.fowollers = 0
#         self.fowolling = 0
#         print(self, self.user_id, self.user_name)
        
    
#     def fowoller ( self, user ):
#         user.fowollers +=1
#         print(user.fowollers, user.user_id, user.user_name)
#         self.fowolling +=1
#         print(self.fowolling, self.user_id, self.user_name)

    
# user_1 = User("005", "jia")

# user_2 = User("002", "maddie")
# user_1.fowoller(user_2)
# print(user_1.fowollers)
# print(user_1.fowolling)
# print(user_2.fowollers)
# print(user_2.fowolling)

import data
import random
question_data = data.question_data
# print(data.question_data)

# class GuessingGame:
#     def __init__(self, question_data, choice):
#         self.question_data = question_data
#         self.choice = choice
#     def question(self, choice):
#         if choice ==random.choice(question_data):
#             print( "you got right")
#             return True
#         else:
#             return False

# Jia = GuessingGame(question_data, "True")
# result = Jia.choice("True")
# print(Jia)
# print(result)

   


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_question(self):
        return  self.question_number < len(self.question_list)

    def next_question ( self ):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f" Q.{self.question_number}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got right")
            
        else:
            print("that's wrong")
        print(f"the correct answer is: {correct_answer} ")
        print(f"Your current score is : {self.score}/{self.question_number} ")
        print("\n")
        
        



quize_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    quize_bank.append(new_question)
print(quize_bank)
quize = QuizBrain(quize_bank)

while quize.still_has_question():
    quize.next_question()

print("you complete the quiz")
print(f"you total outcome is: {quize.score}/{quize.question_number}")






   
            