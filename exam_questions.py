# num = 7%2
# print (num)
# Question 16(a)
# Examination Number:

from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0
    user_guess = 0
#(iv)
    trys = int(input("how many trys you want? :"))
#(v)
    level = input("enter dificulty level (E)asy or (H)ard:")
    if level == "H":
        secret_number = radiant(1, 101)
    else:
        secret_number = secret_number
#(iii)
    while (user_guess != secret_number and guess_count != trys):
        user_guess = int(input("Enter your guess: "))
        guess_count += 1  # Increase guess_count by 1
        if user_guess == secret_number:
            print("Congratulations! You win!")
            #(i)
            print("it took you",guess_count,"guesses")
            #(ii)
        elif user_guess > secret_number:
            print("oops number too high")
        elif user_guess < secret_number:
            print("oops your number is too low")
        else:
            print("out of guesses")

print("Welcome to the guessing game!")
guess_game(3)