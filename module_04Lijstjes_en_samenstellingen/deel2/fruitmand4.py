from fruitmand1 import fruitmand
from random import randint

aantal = int(input("Hoeveel fruit wilt u?: "))
for f in range(aantal):
    print(fruitmand[randint(0,len(fruitmand)-1)]["name"])
