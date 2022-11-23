import random
kleuren = ("oranje", "blauw", "groen", "bruin")

aantal = int(input("Hoeveel M&M's moeten in de zak? "))

set = (random.choices(kleuren, k = aantal))

print("in de zak met M&M's zit: ")
print(set)