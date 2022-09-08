# voornaam : Ahmad  
# achternaam : Alaina 
# opdracht : Pizzacalculator
# Vraagt welke grootte pizza

print("welkom bij Newyork pizaa")

small = 7.99
medium = 8.50
large = 10.00

small_pizza_size = int(input("Hoe veel small pizza's wilt uw hebben?"))
medium_pizza_size = int(input("Hoe veel medium pizza's wilt uw hebben?"))
large_pizza_size = int(input("Hoe veel large pizza's wilt uw hebben?"))

totaal = small_pizza_size * small + medium_pizza_size * medium + large_pizza_size * large

print(f''' uw heeft {small_pizza_size} small pizza's, {medium_pizza_size} medium pizza's, {large_pizza_size} large pizza's
besteld, {totaal} bedrag is euro ''' )
