from fruitmand1 import fruitmand
import random

aantal = int(input("Hoeveel fruit wilt u?: "))
for f in range(aantal):
    # print(fruitmand[randint(0,len(fruitmand)-1)]["name"])
    print(random.choice(fruitmand))
