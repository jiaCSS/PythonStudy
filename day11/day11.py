cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
def blackjack( cards):
    player =[]
    dealer = []
    sum_player = 0
    sum_dealer = 0
    
    for _ in range(0, 2):
        player_num = random.choice(cards)
        print(player_num)
        player.append(player_num)
        sum_player += player_num
        
    print(player)   
    for _ in range(0, 2):
        dealer_num = random.choice(cards)
        dealer.append(dealer_num)
        sum_dealer += dealer_num
    print(dealer)   
    
    get_cards = True
    while get_cards:
        continue_game = input("does player want more cards, yes, no: ")
        if continue_game =="yes":
            player_num3 = random.choice(cards)
            player.append(player_num3)
            sum_player += player_num3
            print(sum_player)
            if sum_player == 21:
                print("player lose game")
                get_cards = False
        else:
            get_cards=False
    
    get_cards_dealer = True
    while get_cards_dealer:
        continue_game = input("does dealer want more cards, yes, no: ")
        if continue_game =="yes":
            dealer_num3 = random.choice(cards)
            dealer.append(dealer_num3)
            sum_dealer += dealer_num3  
            print(sum_dealer)
        else:
           get_cards_dealer = False
    
    if sum_player <= 21 and sum_dealer <= 21:
        
        if sum_player == 21 :
            print(" dealer win and the scores is: " , sum_dealer)
        if sum_dealer == 21 :
            print(" play win and the scores is: " , sum_player)
        elif sum_player > sum_dealer:
            print(" player win and the scores is: " , sum_player)
        elif sum_player < sum_dealer:
            print(" dealer win and the scores is: " , sum_dealer)
        else:
            print("with draw")
    else:
        if sum_player>21:
            print("dealer wins", sum_dealer)
        elif sum_dealer > 21:
            print("player wins", sum_player)
            
           
    
    # if sum_player < 15:
    #     player_num3 = random.choic(cards)
    #     player.append(player_num3)
    #     new_sum_player = sum_player + player_num3
    #     if new_sum_player > sum_dealer:
    #         print("player wins")
    #     elif new_sum_player == sum_dealer:
    #         print("draw")
    #     else:
    #         print("dealer wins")
    # elif sum_player <= 21:
    #     if sum_player > 
        
    #     print("player wins and the scores is: ", sum_player)
    # else:
    #     print(" the dealer wins")
    
    
        
    
        
        


blackjack(cards)