from ast import If
import random

myTable = [0,0,0,0]

print ("Exercice 1")

tableausecour01 = 0
tableausecour02 = 0

for i in range (0,4) :
    myTable[i] = random.randint(0,10)
    

print (myTable)
tableausecour01 = myTable [1]
tableausecour02 = myTable [2]

myTable [1] = myTable [2]
myTable [2] = tableausecour01

print (myTable)


print ("Exercice 2")

myTable2 = [0,0,0,0]
tableausecour01 = 0
tableausecour02 = 0


for i in range (0,4) :
    myTable2[i] = random.randint(0,10)
    
print (myTable2)

for i in range (0 , len (myTable2)): 
    if (myTable2[i] < myTable2[3]):
        tableausecour01 = myTable2 [0]
        tableausecour02 = myTable2 [3]
        myTable2 [0] = myTable2 [3]
        myTable2 [3] = tableausecour01


print (myTable2)

print ("Exercice 3")

myTable3 = [0,0,0,0]
petitnombre = 11
placeindicepetit = 0


for i in range (0,4) :
    myTable3[i] = random.randint(0,10)

print (myTable3)

for i in range (0 , len (myTable3)): 
    for a in range (i , len (myTable3)):
       
        if (myTable3[a] < myTable3 [placeindicepetit]) : # placeindice petit, comme vaut 0, 0 est la place dans le tableau PAS LA VALEUR
            placeindicepetit = a # change le numero de la case par a, comme place = 0 elle changera forcement sauf si la case 0 et le plus petit

    petitnombre = myTable3[placeindicepetit]
    myTable3[placeindicepetit] = myTable3[i]
    myTable3[i] = petitnombre

    placeindicepetit = i+1 # réinitialise placeindice petit et rajoute 1 pour ne plus regarder les case deja passer


print (myTable3)


print ("Exercice 4")

#Le tri à bulles est considéré comme lent car il regarde chaque élements d'un tableau pour les comparer, et ainsi de suite selon le nombre de fois que l'on lui demande.
#Je ne pense pas que l'on puisse avoir une idée du temps nécessaire à son execution. Mais l'on sais qu'il va s'activer une fois pour chaque éléments d'un tableau fois le nombre de fois que l'on lui demande de re trier le tableau.

print ("Lire le commentaire")


print ("Partie 2 - Tic tac toe")


print ("Exercice 1")


ligneA = "* * *"
ligneB = "* * *"
ligneC = "* * *"

print(ligneA)
print(ligneB)
print(ligneC)

print ("Exercice 2")

ligneChoisi = input("Ligne ? 1 ? 2? 3 ?")
coloneChoisie = input ("Colone ? 1? 2? 3?")
if (ligneChoisi == 1):
    if (coloneChoisie == 1):
        ligneA = "X * *"
    
    if (coloneChoisie == 2):
        ligneA = "* X *"

    if (coloneChoisie == 3):
        ligneA = "* * X"

if (ligneChoisi == 2):
    if (coloneChoisie == 1):
        ligneB = "X * *"
    
    if (coloneChoisie == 2):
        ligneB = "* X *"

    if (coloneChoisie == 3):
        ligneB = "* * X"

if (ligneChoisi == 3):
    if (coloneChoisie == 1):
        ligneC = "X * *"
    
    if (coloneChoisie == 2):
        ligneC = "* X *"

    if (coloneChoisie == 3):
        ligneC = "* * X"

print(ligneA)
print(ligneB)
print(ligneC)

print("Exercice 3")

if (ligneA =="x x x" ):
    print("Félicitation vous avez gagnez")

if (ligneB =="x x x" ):
    print("Félicitation vous avez gagnez")

if (ligneC =="x x x" ):
    print("Félicitation vous avez gagnez")

if (ligneA == "X * *") # Ne fonctionne plus, sinon je doit crée une verification pour chaque possibilité de jeu.

print ("Exercice 4")

if (ligneA != "* * *") :
    if (ligneB != "* * *"):
        if (ligneC != "* * *"):
            print("La grille est complète")
 

print ("Exercice 5")


ligneA = "***"
ligneB = "***"
ligneC = "***"



print ("Tour de joueur 1")
print(ligneA)
print(ligneB)
print(ligneC)

while True:

    ligneChoisi = input("Ligne ?")
    coloneChoisie = input ("Colone ?")

    if(ligneChoisi == "A"):
        newLine = ""
        for i in range (0,2):
            if(i == coloneChoisie):
                newLine = "X"
            else:
                newLine = ligneA[i]
        ligneA = newLine
        while (newLine == ligneA) == False :

    if(ligneChoisi == "B"):
        newLine = ""
        for i in range (0,2):
            if(i == coloneChoisie):
                newLine = "X"
            else:
                newLine = ligneB[i]
        ligneB = newLine
    False
    
    if(ligneChoisi == "C"):
        newLine = ""
        for i in range (0,2):
            if(i == coloneChoisie):
                newLine = "X"
            else:
                newLine = ligneC[i]
        ligneC = newLine
    False

    print(ligneA)
    print(ligneB)
    print(ligneC)


    print ("Exercice 6")

# Pour faire un puissance 4 il faudra agrandir la taille de la grille, faire que la fonctionnalité qui regarde les ligne de trois regarde maintenant les lignes entièrement et regarde si 4 symboles identiques sont coter à coter.

    print("lire les commentaires")