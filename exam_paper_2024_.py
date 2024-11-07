from random import choice
fruits = ["apple", "cherry", "orange"]

random_fruits_1 = choice (fruits)
#(i)
print("random fruit 1:", random_fruits_1)
#(ii)
random_fruits_2 = choice(fruits)
random_fruits_3 = choice(fruits)
print("random fruit 2:", random_fruits_2)
print("random fruit 3:", random_fruits_3)
#(iii)
if random_fruits_1 == ("cherry"):
    print("first fruit is cherry")
#(iv)
if random_fruits_1 == random_fruits_2:
    print("first pair match")
#(v)
if random_fruits_1 ==("cherry") and random_fruits_2 == ("cherry"):
    print("first pair is cherries")
#(vi)
if random_fruits_1 == random_fruits_2 or random_fruits_1  == random_fruits_3 or random_fruits_2 == random_fruits_3:
    print("matching pair")
#(vii)
counter = 0
apple = 0
cherry = 0
orange = 0
while counter < 101:
    random_fruits_1 = choice(fruits)
    random_fruits_2 = choice(fruits)
    random_fruits_3 = choice(fruits)
    if random_fruits_1 == ("cherry") or random_fruits_2 == ("cherry") or random_fruits_3 == ("cherry"):
        cherry += 1
    elif random_fruits_1 == ("orange") or random_fruits_2 == ("orange") or random_fruits_3 == ("orange"):
        orange += 1
    else:
        random_fruits_1 == ("apple") or random_fruits_2 ==("apple") or random_fruits_3 == ("apple")
        apple += 1
    counter += 1
print("orange:",orange)
print("cherry",cherry)
print("apple",apple)



#(b)
fruits = ["apple","orange","cherry"]
extra = input("enter an additional fruit to the list: ")
fruits.append(extra)
print("the list of 4 fruits is", fruits)
winner = input("nominate a winning fruit in the list above: ")
while winner not in fruits:
    print("error try again")
    winner = input("nominate a winning fruit in the list above :")
print("the winning fruit you nominated is", winner)

counter = 0
random_f_1 = choice(fruits)
random_f_2 = choice(fruits)
random_f_3 = choice(fruits)
while random_f_1 != random_f_2 or random_f_1 !=random_f_3 or random_f_2 != random_f_3 or random_f_1 != winner:
    random_f_1 = choice(fruits)
    random_f_2 = choice(fruits)
    random_f_3 = choice(fruits)
    counter += 1
print("winner after",counter,"tries")
