import random
print("welcome to the guessing game")
welcome = input("type 1 to begin or anything else to exit :")

if welcome == "1" :
    x=[1,2,3,4,5,6,7,8,9,0]
    y=[1,2,3,4,5,6,7,8,9,0]
    guess1 =str(random.choice(x))
    guess2 =str(random.choice(y))
    guess3 = guess1 + guess2
    people_guess=str(input("write the number you guessed :"))
    while not people_guess == guess3 :
        print("you guessed it wrong")
        people_guess=str(input("guess again or exit to exit"))
        if people_guess==guess3:
            print("you did it congrats")
            break
        elif people_guess=="exit" or people_guess=="Exit" :
            print("program exited")
            break
        else :
            continue
else:
    print("program exited ")
    
