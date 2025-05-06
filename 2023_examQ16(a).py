#question 16(a)
from random import randint

def guess_game(max_guesses_allowed):
    #(v)
    level =input("enter the difficulty you would like. (H)ard or (E)asy")
    if level == "H":
        lvl =(100)
    else:
        lvl =(5)
        
    secret_number = randint(1,  lvl)
    guess_count = 0
    user_guess = 0
    
    #(iv)
    max_guesses_allowed = int(input("how many guesses do you want"))
    print(secret_number)
    print(max_guesses_allowed)
    print(guess_count)
    guesses =[]
    #(iii)
    while (user_guess != secret_number and max_guesses_allowed > guess_count) :
        #(ii)
        user_guess =int(input("enter your guess: "))
        if user_guess < secret_number:
            print("sorry! your guess was too low")
            if  user_guess == user_guess:
                print("you have already guessed this number.")
        elif user_guess > secret_number:
            print("sorry! your guess was too high")
            if user_guess == user_guess:
                print("you have already guessed this number.")
        #elif user_guess == user_guess:
           # print("you have already guessed this number.")
        guess_count += 1 #increase guess_count by 1
    else:
        #(i)
        print("congradulations!! you win!! it took you",guess_count,"guesses")

print("welcom to the guessing game!")
guess_game(3)