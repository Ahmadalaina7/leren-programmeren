import random
kleur = ("oranje", "blauw", "groen", "bruin")

(oranje, blauw, groen, bruin) = kleur

vraag = int(input("Hoeveel M&M's moeten in de zak? "))

set = (random.choices(kleur, k=vraag))

print("in de zak met M&M's zit: ")
print(set)