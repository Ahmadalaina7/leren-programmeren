# voornaam : Ahmad  
# achternaam : Alaina 
# opdracht : Pizzacalculator
# Vraagt welke grootte pizza

print("welkom bij Newyork pizza")

smallPrijs = 7.99
mediumPrijs = 8.50
largePrijs = 10.00

var = 0
while var == 0:
    try : 
        small_pizza_amount = int(input("Hoe veel small pizza's wilt uw hebben? "))
        var += 1
    except :
        print("vul een heel getal in")
while var == 1:
    try :
         medium_pizza_amount = int(input("Hoe veel medium pizza's wilt uw hebben? "))
         var += 1
    except :
        print("vul een heel getal in")
while var == 2: 
    try :
         large_pizza_amount = int(input("Hoe veel large pizza's wilt uw hebben? "))
         var += 1
    except :
        print("vul een heel getal in")


    totaal = round(small_pizza_amount * smallPrijs + medium_pizza_amount * mediumPrijs + large_pizza_amount * largePrijs , 2)

print(f''' uw heeft {small_pizza_amount} small pizza's, {medium_pizza_amount} medium pizza's, {large_pizza_amount} large pizza's
besteld, €{totaal} euro ''' )
