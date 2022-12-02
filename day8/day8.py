# function in input arguents and paramaters
import math
def greet(name):
    print(f"hello {name}")
    print("how do you do?")
    print("what is weather today")

greet("Maddie")
# do not forget " " not only Maddie

def greet_name_place(name, place):
    if name == "Maddie":
        print("hello", name, "you live in: ", place)
    else: 
        print("you are not Maddie")
    

greet_name_place("Maddie", "ann arbor")
greet_name_place("caddie", "ann arbor")

def cans_paint (height, width):
    cans = height*width/5
    round = math.ceil(cans)
    print("the number of cans you need to buy is : ", cans, round)

cans_paint(2.3, 5)




def check_prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0: 
            is_prime = False
            print(is_prime)
        
    if is_prime:
        print("this is prime number")
    else:
        print("it is not a prime number")
        
# check_prime(8)
check_prime(8)
# check_prime(6)

# encode and decode
texts = input("enter a string: ")

alp = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h','i','j', 'k', 'l','m','n','o','p','q', 'r','s', 't', 'u', 'v', 'w','x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f','g', 'h','i','g', 'k', 'l','m','n','o','p','q', 'r','s', 't', 'u', 'v', 'w','x', 'y', 'z']
shift = int (input("shift number: "))
en_de = input("enter encode or decode: ")

def encode_decode(texts, shift, en_de):
    endtext = " "
    
    for char in texts:
        if char in alp:
            position = alp.index(char)
            if en_de =="encode":
                new_position = position + shift
                endtext += alp[new_position]
            else:
                new_position = position - shift
                endtext += alp[new_position]
        else:
            endtext += char
    print(endtext)
 
encode_decode(texts, shift, en_de)


should_continue = True
while should_continue:
    texts = input("enter a string: ")
    shift: int(input("shift: "))
    en_de: input("enter encode or decode:")
    encode_decode(texts, shift, en_de)
    
    result = input("type yes to want again no to exit")
    if result == "yes":
        should_continue = True
    else:
        should_continue = False


         
            
    
    
        


# alp.index  it is to find a index of alp in a giving word
# def encode(   ):
    
#     for text in texts:
#         text_list.append(text)
#     print(text_list)
    
#     for index in range(len(alp)):
#         for index_text_list in range(len(text_list)):
#             if text_list[index_text_list] == alp[index]:
#                 text_list[index_text_list] = alp[index-shift] 
#                 print(text_list)
            
            
#     print(f"{ ' '.join(text_list)}")    

# encode()


