from random import randint
#(i)
print("dice simulation and analysis program: ")
results = []
frequencies = [0, 0, 0, 0, 0, 0]

for i in range (100):
    throw_result = randint(1, 6)
    results.append(throw_result)
    
    
   #(iii) 
    if throw_result ==1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] +1
    elif throw_result == 3:
        frequencies[2] = frequencies[2] +1
    elif throw_result == 4:
        frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
        frequencies[4] = frequencies[4] +1
    elif throw_result ==6:
        frequencies[5] = frequencies[5] +1
print()
#print("results: ", results)
#(ii)
print("frequencies: ", frequencies)

#(v)
print("dice  frequencie")
for i in frequencies:
    print(i)