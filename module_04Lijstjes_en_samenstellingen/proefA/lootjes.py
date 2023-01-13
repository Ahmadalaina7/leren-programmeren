import random
namen = []
lootjes = {}
while True:
    naam = input("Wat zijn de namen van de spelers?  ").lower()
    if naam in namen:
        print("dit heeft u al gekozen")
    else:
        namen.append(naam)
    if len(namen) >= 3:
        vraag = input("wilt u nog een naam invoeren ? ")
        if vraag == "nee":
            break
shuffling = True
while shuffling:
    namen_shuffle = random.sample(namen, len(namen))
    shuffling = False
    for i in range(len(namen)):
        if namen_shuffle[i] == namen[i]:
            shuffling = True

for i in range(len(namen)):
    lootjes.update({namen[i]: namen_shuffle[i]})

print(lootjes)
