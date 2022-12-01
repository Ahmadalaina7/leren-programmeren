from fruitmand import fruitmand

kleuren = []

for fruit in fruitmand:
    kleuren.append(fruit["color"])

while True:
    kleur = input("Voer hier een kleur in: ").lower()
    if kleur in kleuren:
        break
    else:
        print(f"De kleur {kleur} zit er niet in de fruitmand")

rond, niet_rond,= 0, 0
print(fruitmand)
for fruit in fruitmand:
    test = fruit["color"]
    if test == kleur:
        if fruit["round"]:
            rond += 1
        else:
            niet_rond += 1
print(rond)
print(niet_rond)
if rond > niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
elif rond < niet_rond:
    print(f"Er zijn {niet_rond - rond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}")
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}")
