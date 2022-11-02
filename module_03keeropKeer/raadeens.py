import random

poging = 0
ronde = 0
score = 0
AANTAL_RONDES = 20
AANTAL_POGINGEN = 10


while ronde < AANTAL_RONDES:
    raden = input("Wil je een getal raden?: ").lower()

    if raden == "nee":
        print("Oke jammer!")
        print(f"Jou eind score is {score} van de {AANTAL_RONDES} punten!")
        exit()

    num = random.randint(1, 1000)
    print(num)  # dit is om te het testen van de programma makkelijker te maken
    while poging < AANTAL_POGINGEN:  # loop van het getal raden stopt na 10 pogingen
        while True:
            try:  # verplicten van cijfers
                antwoord = int(input("Raad het getal: "))
                break  # loop and a half
            except ValueError:
                print("Cijfers alleen AUB!")

        if antwoord == num:
            print("Je hebt het goed geraden!")
            score += 1
            break
        else:  # abs gebruiken
            verschil = abs(antwoord - num)
            if verschil <= 20:  # berekent hier of het heel warm is of warm
                print("Je bent heel warm!")
            elif verschil <= 50 and verschil >= 20:
                print("Je bent warm!")
        poging += 1

    print(f"Je hebt {score} punt(en)!")
    ronde += 1
    poging = 0


print(f"Jou eind score is {score} van de {AANTAL_RONDES} punten!")

