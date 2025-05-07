play =()
user_score = 0
while play != "n":
    from random import randint
    sectret_num = randint(1, 100)
    #print(sectret_num)
    user_guess = int(input("enter a number: "))
    calculation = sectret_num - user_guess
    print("the secret number was: ",sectret_num,"the number you chose was: ", user_guess,"the diffrence is",calculation)

    if calculation == 0:
        user_score= user_score +100
    elif calculation <=20 and calculation > 0:
        user_score = user_score + 20
        print("you gained 20 points")
    elif calculation >= -20 and calculation <0:
        user_score = user_score + 20
        print("you gained 20 pints")
    elif calculation <= -20:
        user_score = user_score -30
        print("you lost 30 points")
    elif calculation > 20:
        user_score = user_score - 30
        print("you lost 30 points")
    print(user_score)
    play = input("would you like to play again (n)o or (y)es")
        
