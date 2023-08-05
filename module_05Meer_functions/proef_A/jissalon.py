from function import*
print('Welkom bij Papi Gelato')

aantal_bakjes = 0
aantal_hoorntjes = 0
aantal_bolletjes = 0

smaken_teller = {}
topping_teller= {}

while True:
    bolletjes = vraag_bolletjes()
    hoorntje_of_bakje = vraag_bakje(bolletjes)
    aantal_bolletjes += bolletjes
    vraag_smaken(bolletjes , smaken_teller)

    vraag_topping(hoorntje_of_bakje, topping_teller , bolletjes)
    
    if hoorntje_of_bakje == "bakje":
        aantal_bakjes += 1
    else:
        aantal_hoorntjes += 1
    
    print(bolletjes, hoorntje_of_bakje)
    
    meer_bestellen = vraag_meer_bestellen()
    
    if not meer_bestellen:
        break
maak_een_bon(aantal_bolletjes, aantal_bakjes, aantal_hoorntjes,smaken_teller , topping_teller )
