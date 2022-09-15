# voornaam : Ahmad  
# achternaam : Alaina 
# opdracht : Pizzacalculator
# Vraagt welke grootte pizza

print("welkom bij Newyork pizaa")

small = 7.99
medium = 8.50
large = 10.00

var = 0
while var == 0:
    try : 
        small_pizza_size = int(input("Hoe veel small pizza's wilt uw hebben? "))
        var += 1
    except :
        print("vul een heel getal in")
while var == 1:
    try :
         medium_pizza_size = int(input("Hoe veel medium pizza's wilt uw hebben? "))
         var += 1
    except :
        print("vul een heel getal in")
while var == 2: 
    try :
         large_pizza_size = int(input("Hoe veel large pizza's wilt uw hebben? "))
         var += 1
    except :
        print("vul een heel getal in")


    totaal = round(small_pizza_size * small + medium_pizza_size * medium + large_pizza_size * large , 2)

print(f''' uw heeft {small_pizza_size} small pizza's, {medium_pizza_size} medium pizza's, {large_pizza_size} large pizza's
besteld, €{totaal} euro ''' )
