import random

tableau = [0,0,0,0]
tableausecour01 = 0

for i in range (0,4) :
    tableau[i] = random.randint(0,10)
    

print (tableau)
tableausecour01 = tableau [1]
tableausecour02 = tableau [2]

tableau [1] = tableau [2]
tableau [2] = tableausecour01

print (tableau)