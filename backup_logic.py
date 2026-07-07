import random
import math

cards = {"AD": ("R", 1, "D"), "AH": ("R", 1, "H"), "AS": ("B", 1, "S"), "AC": ("B", 1, "C"),
         
         "2D": ("R", 2, "D"), "2H": ("R", 2, "H"), "2S": ("B", 2, "S"), "2C": ("B", 2, "C"),
         "3D": ("R", 3, "D"), "3H": ("R", 3, "H"), "3S": ("B", 3, "S"), "3C": ("B", 3, "C"),
         "4D": ("R", 4, "D"), "4H": ("R", 4, "H"), "4S": ("B", 4, "S"), "4C": ("B", 4, "C"),
         "5D": ("R", 5, "D"), "5H": ("R", 5, "H"), "5S": ("B", 5, "S"), "5C": ("B", 5, "C"),
         "6D": ("R", 6, "D"), "6H": ("R", 6, "H"), "6S": ("B", 6, "S"), "6C": ("B", 6, "C"),
         "7D": ("R", 7, "D"), "7H": ("R", 7, "H"), "7S": ("B", 7, "S"), "7C": ("B", 7, "C"),
         "8D": ("R", 8, "D"), "8H": ("R", 8, "H"), "8S": ("B", 8, "S"), "8C": ("B", 8, "C"),
         "9D": ("R", 9, "D"), "9H": ("R", 9, "H"), "9S": ("B", 9, "S"), "9C": ("B", 9, "C"),
         "10D": ("R", 10, "D"), "10H": ("R", 10, "H"), "10S": ("B", 10, "S"), "10C": ("B", 10, "C"),
         
         "JD": ("R", 11, "D"), "JH": ("R", 11, "H"), "JS": ("B", 11, "S"), "JC": ("B", 11, "C"),
         "QD": ("R", 12, "D"), "QH": ("R", 12, "H"), "QS": ("B", 12, "S"), "QC": ("B", 12, "C"),
         "KD": ("R", 13, "D"), "KH": ("R", 13, "H"), "KS": ("B", 13, "S"), "KC": ("B", 13, "C"),
        
        }

#rk = Random key, # following rk = round
#comp (means computer AKA card drawn), # following comp = round

#Check count to make sure there are cards in deck
def check_count():
    if len(cards) == 0:
        print("Chug!")
        return True

#First card logic
def first_card():
    red_or_black = input("1st Card -- R or B? : ")
    rk1 = random.choice(list(cards.keys()))
    comp1 = cards[rk1][0]
    comp1_num = cards[rk1][1]

    return rk1, comp1, comp1_num, red_or_black

#Second card logic
def second_card(rk1):
    #If equal, remove card from deck and move on
    cards.pop(rk1)
    print(f"Next! The card was {rk1}. There are {len(cards)} cards left.")

    #Ask user for higher/lower -- 2ND CARD
    higher_or_lower = input("2nd Card -- Higher or Lower? : ")

    #Random number for 2ND CARD
    rk2 = random.choice(list(cards.keys()))
    comp2 = cards[rk2][1]

    return rk2, comp2, higher_or_lower

#Third card logic
def third_card(rk2):
    cards.pop(rk2)
    print(f"Next! The card was {rk2}. There are {len(cards)} cards left.")

    #Collect user input for between or outside card 1 and card 2
    between_outside = input("3rd Card -- In Between or Outside? : ")

    #Random number for 3RD CARD
    rk3 = random.choice(list(cards.keys()))
    comp3 = cards[rk3][1]

    return rk3, comp3, between_outside

#Fourth card logic
def fourth_card(rk3):
    cards.pop(rk3)
    print(f"Next! The card was {rk3}. There are {len(cards)} cards left.")

    #Ask user for suit
    choice_suit = input("4th Card -- What is the suit? : ")

    #Random number for 4TH CARD
    rk4 = random.choice(list(cards.keys()))
    comp4 = cards[rk4][2]

    return rk4, comp4, choice_suit

#State variable
current_round = 1

#Stay on bus logic (else logic)
def stay_on_bus(rk):
    global current_round
    current_round = 1

    cards.pop(rk)
    print(f"You staying on the bus! The card was {rk}. There are {len(cards)} cards left.")

#BEGIN LOOP
while True:
    #If the deck runs out
    if check_count():
        break

    #FIRST CARD
    if current_round == 1:
        if check_count():
            break

        #Call first card function
        rk1, comp1, comp1_num, red_or_black = first_card()

        #Check equality
        if red_or_black.upper() == comp1:
            current_round = 2

        #Reset back to round 1 if not equal
        else:
            stay_on_bus(rk1)

    #SECOND CARD
    elif current_round == 2:
        if check_count():
            break

        #Call second card function
        rk2, comp2, higher_or_lower = second_card(rk1)

        #If cards are equal, go again
        if comp2 == comp1_num:
            if check_count():
                break
            cards.pop(rk2)
        
        #Check equality
        elif (higher_or_lower.lower() == "higher") and (comp2 > comp1_num):
            if check_count():
                break
            
            current_round = 3
        
        #Check equality
        elif (higher_or_lower.lower() == "lower") and (comp2 < comp1_num):
            if check_count():
                break
            
            current_round = 3
        
        #Back to round 1 if not equal
        else:
            stay_on_bus(rk2)

    #THIRD CARD
    elif current_round == 3:
        #If user is between, then check if number is between first two
        rk3, comp3, between_outside = third_card(rk2)

        #Check if cards are equal on upper & lower bounds
        if (comp3 == comp1_num) or (comp3 == comp2):
            if check_count():
                break
            cards.pop(rk3)

        #Check equality
        elif (between_outside.lower() == "between") and (comp1_num < comp3 < comp2 or comp2 < comp3 < comp1_num):
            if check_count():
                break

            current_round = 4
        
        #Check equality
        elif (between_outside.lower() == "outside") and not (comp1_num < comp3 < comp2 or comp2 < comp3 < comp1_num):
            if check_count():
                break

            current_round = 4
        
        #If not equal, return to first round
        else:
            stay_on_bus(rk3)

    #FOURTH CARD
    elif current_round == 4:
        rk4, comp4, choice_suit = fourth_card(rk3)

        #Check if suit is equal
        if choice_suit.upper() == comp4:
            if check_count():
                break
            
            cards.pop(rk4)
            print(f"Congrats! You have gotten off of the bus! The card was {rk4}, and it took you {52 - len(cards)} cards to win.")
            break

        #If not equal, return to first round
        else:
            stay_on_bus(rk4)
