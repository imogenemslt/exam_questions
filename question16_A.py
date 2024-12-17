# Question 16(a)
# Student name:imogene
import random
#(iv)
def dice_game():
    print("welcome to the dice game!!")
    return()
dice_game()
your_name = input("Please enter your name: ")
#(ii)
lucky_number = int(input("please selectc a lucky number between 1 and 6: "))
#(i)
# initialize computer number
computer_die_roll = random.randint(1,6)
#(iii)
print(your_name ,"lucky number was", lucky_number) 
print("The computer rolled: ",computer_die_roll)

#(v)
if lucky_number > computer_die_roll:
    print("you guessed to high")
elif lucky_number < computer_die_roll:
    print("you guessed to low")
else:
    print("you guessed correct, well done!")

