#section c
from random import choice

fruits = ["apple", "cherry", "orange"]
#(vii)
counter = 0
Acounter = 0
Ccounter = 0
Ocounter = 0
while counter <100:
    random_fruits_1 = choice(fruits)
    #(i)
    print("random fruit 1:", random_fruits_1)
    #(ii)
    random_fruits_2 = choice(fruits)
    random_fruits_3 = choice(fruits)
    print("random fruit 2:", random_fruits_2)
    print("random fruit 3:", random_fruits_3)
    #(iii)
    print("first fruit is",random_fruits_1)
    #(iv)
    if random_fruits_1 == random_fruits_2:
        print("first pair match")
        #(v)*****
        if random_fruits_1 == ("cherry") and random_fruits_2 ==("cherry"):
            print("first pair are cherries")
    #(vi)
    if random_fruits_1 == random_fruits_2 or random_fruits_1 == random_fruits_3 or random_fruits_2 == random_fruits_3:
        print("matching pair")
    #(vii)
    counter +=1
    if random_fruits_1 == ("apple") or random_fruits_2 == ("apple") or random_fruits_3 == ("apple"):
        Acounter +=1
    if random_fruits_1 == ("cherry")or random_fruits_2 == ("cherry") or random_fruits_3 == ("cherry"):
        Ccounter +=1
    if random_fruits_1 == ("orange")or random_fruits_2 ==("orange") or random_fruits_3 == ("orange"):
        Ocounter +=1
print("cherries",Ccounter)
print("apples",Acounter)
print("oranges",Ocounter)
    

    
