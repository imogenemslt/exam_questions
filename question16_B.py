#Question 16(b)
#Student name:
import random
ticket = []
#(i)
counter = 0
while counter < 3:
    counter +=1
    user_number = int(input("Please pick a number between 1 and 10: "))
    ticket.append(user_number)



print("Your ticket is: ",ticket)
print("The draw will start now, good luck!")
drum = [1,2,3,4,5,6,7,8,9,10]
result = []
def lotto(ticket):
    for times in range(3):
        draw = drum[random.randint(0,len(drum))-1]
        #(iii)
        drum.remove(draw)
        result.append(draw)
    print("The draw was: ",result)

lotto(ticket)
#(ii)
def ticket_num():
    for i in ticket:
        return(i)
def result_num():
    for item in result:
        return(item)

#ticket_num()
if ticket_num() == result_num():
    print("you win!")
else:
    print("you lose!")
