def vraag_bolletjes():
    while True:
        try:
            bolletjes = int(input("aantal bolletjes "))
            if bolletjes <= 0:
                print('Vul een getal groter dan 0')
            elif bolletjes <= 8:
                break
            else:
                print('Sorry, zulke grote bakken hebben we niet')
        except:
            print("Vul een cijfer in")
    return bolletjes

def vraag_bakje(bolletjes):
    hoorntje_of_bakje = 'bakje'
    if bolletjes <= 3:
        while True:
            try:
                hoorntje_of_bakje = input(f'Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? ')
                if hoorntje_of_bakje in ('hoorntje', 'bakje'):
                    break
                else:
                    print('Sorry, dat begrijp ik niet. Kies tussen "hoorntje" of "bakje".')
            except:
                print("Sorry, dat begrijp ik niet. Kies tussen 'hoorntje' of 'bakje'.")
    print(f"Hier is uw {hoorntje_of_bakje} met {bolletjes} bolletje(s)")
    return hoorntje_of_bakje

def vraag_meer_bestellen():
    while True:
        meerBestellen = input("Wilt u meer bestellen? ")
        if meerBestellen.lower() == "ja":
            return True
        elif meerBestellen.lower() == "nee":
            return False
        else:
            print("Sorry, dat begrijp ik niet. Typ 'ja' of 'nee'.")

def vraag_smaken(bolletjes , smaken_teller):
    for i in range(bolletjes):
        while True:
            smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
            if smaak.upper() in ("A", "C", "M", "V"):
                if smaak.upper() == "A":
                    smaak_naam = "Aardbei"
                elif smaak.upper() == "C":
                    smaak_naam = "Chocolade"
                elif smaak.upper() == "M":
                    smaak_naam = "Munt"
                elif smaak.upper() == "V":
                    smaak_naam = "Vanille"
                
                if smaak_naam in smaken_teller:
                    smaken_teller[smaak_naam] += 1
                else:
                    smaken_teller[smaak_naam] = 1
                
                # smaken.append(smaak_naam)
                break
            else:
                print("Sorry, dat begrijp ik niet. Probeer het opnieuw.")

def vraag_topping(hoorntje_of_bakje, topping_teller , aantal_bolletjes):
    
    while True:
        topping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
        if topping.upper() in ("A", "B", "C", "D"):
            if topping.upper() == "A":
                topping_naam = "Geen"
            elif topping.upper() == "B":
                topping_naam = "Slagroom"
            elif topping.upper() == "C":
                topping_naam = "Sprinkels"

            elif topping.upper() == "D":
                topping_naam = "Caramel saus " + hoorntje_of_bakje

            aantal_eenheden = 1
            if topping_naam == "Sprinkels":
                aantal_eenheden = aantal_bolletjes
                
            if topping_naam in topping_teller:
                topping_teller[topping_naam] += aantal_eenheden
            else:
                topping_teller[topping_naam] = aantal_eenheden

            break
        else:
            print("Sorry, dat begrijp ik niet. Probeer het opnieuw.")


def maak_een_bon(aantal_bolletjes, aantal_bakjes, aantal_hoorntjes, smaken_teller, topping_teller):
    prijs_per_bolletje = 1.10
    prijs_per_hoorntje = 1.25
    prijs_per_bakje = 0.75
    prijs_Topping_Slagroom = 0.50
    prijs_Topping_Sprinkels = 0.30
    prijs_Topping_caramelSaus_Bakje = 0.90
    prijs_Topping_caramelSaus_hoorntje = 0.60
    geen_topping = 0.00
    totaal_topping = 0
    # bereken totaal caramel in een bakje
    if "Caramel saus bakje" in topping_teller:
        totaal_caramel_bakje = prijs_Topping_caramelSaus_Bakje * topping_teller["Caramel saus bakje"]
        totaal_topping += totaal_caramel_bakje
    #bereken totaal caramel in een hoorntje
    if "Caramel saus hoorntje" in topping_teller:
        totale_caramel_hoorntje = prijs_Topping_caramelSaus_hoorntje * topping_teller["Caramel saus hoorntje"]
        totaal_topping += totale_caramel_hoorntje
    #bereken totaal slagroom
    if "Slagroom" in topping_teller:
        totaal_slagroom = prijs_Topping_Slagroom * topping_teller["Slagroom"]
        totaal_topping += totaal_slagroom
    #bereken totaal Sprinkel
    if "Sprinkels" in topping_teller:
        totaal_sprinkels = prijs_Topping_Sprinkels * topping_teller["Sprinkels"]
        totaal_topping += totaal_sprinkels
    #geen topping is geen extra kosten
    # if "Geen" in topping_teller:
    #     geen_gekozen_topping = geen_topping * topping_teller["Geen"]
    #     totaal_topping += geen_gekozen_topping


    totale_prijs_hoorntjes = aantal_hoorntjes * prijs_per_hoorntje
    totale_prijs_bakjes = aantal_bakjes * prijs_per_bakje
    totale_prijs_bolletjes = aantal_bolletjes * prijs_per_bolletje

    totale_prijs = totale_prijs_hoorntjes + totale_prijs_bakjes + totale_prijs_bolletjes + totaal_topping

    print("-------- BON --------")
    # print(f"Aantal bolletjes: {aantal_bolletjes} x €{prijs_per_bolletje:.2f} = €{totale_prijs_bolletjes:.2f}")
    print(f"Hoorntjes: {aantal_hoorntjes} x €{prijs_per_hoorntje:.2f} = €{totale_prijs_hoorntjes:.2f}")
    print(f"Bakjes: {aantal_bakjes} x €{prijs_per_bakje:.2f} = €{totale_prijs_bakjes:.2f}")
    
    for smaak in smaken_teller:
        print(f"{smaak}: {smaken_teller[smaak]} x €{prijs_per_bolletje:.2f} = €{smaken_teller[smaak] * prijs_per_bolletje:.2f}")
    if totaal_topping > 0.00 :
        print(f"Topping:  €{totaal_topping:.2f}" )

    print("---------------------+")
    print(f"Totale prijs: €{totale_prijs:.2f}")
    print("Bedankt voor uw bestelling!")
    print("---------------------")

# def vraag_topping(hoorntje_of_bakje):
#     toppings = []
#     topping_teller = {}
#     while True:
#         topping = input(
#             f"Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
#         if topping.upper() in ("A", "B", "C", "D"):
#             if topping.upper() == "A":
#                 topping_naam = "Geen"
#             elif topping.upper() == "B":
#                 topping_naam = "Slagroom"
#             elif topping.upper() == "C":
#                 topping_naam = "Sprinkels"
#             elif topping.upper() == "D":
#                 topping_naam = "Caramel saus" +  hoorntje_of_bakje

#             if topping_naam in topping_teller:
#                 topping_teller[topping_naam] += 1
#             else:
#                 topping_teller[topping_naam] = 1

#             toppings.append(topping_naam)
#             break
#         else:
#             print("Sorry, dat begrijp ik niet. Probeer het opnieuw.")
#     return toppings, topping_teller


# def maak_een_bon(aantal_bolletjes, aantal_bakjes, aantal_hoorntjes,smaken_teller , vraag_topping):
#     prijs_per_bolletje = 1.10
#     prijs_per_hoorntje = 1.25
#     prijs_per_bakje = 0.75
#     prijs_Topping_Slagroom = 0.50
#     prijs_Topping_Sprinkels= 0.30
#     if vraag_topping == "bakje":
#         prijs_Topping_caramelSaus = 0.90
#     else vraag_topping == "hoorntje":
#         prijs_Topping_caramelSaus = 0.60
        

#     totale_prijs_hoorntjes = aantal_hoorntjes * prijs_per_hoorntje
#     totale_prijs_bakjes = aantal_bakjes * prijs_per_bakje
#     totale_prijs_bolletjes = aantal_bolletjes * prijs_per_bolletje

#     totale_prijs = totale_prijs_hoorntjes + totale_prijs_bakjes + totale_prijs_bolletjes

#     print("-------- BON --------")
#     print(f"Aantal bolletjes: {aantal_bolletjes} x €{prijs_per_bolletje:.2f} = €{totale_prijs_bolletjes:.2f}")
#     print(f"Hoorntjes: {aantal_hoorntjes} x €{prijs_per_hoorntje:.2f} = €{totale_prijs_hoorntjes:.2f}")
#     print(f"Bakjes: {aantal_bakjes} x €{prijs_per_bakje:.2f} = €{totale_prijs_bakjes:.2f}")
    
#     for smaak in smaken_teller:
#         print(f"{smaak}: {smaken_teller[smaak]} x €{prijs_per_bolletje:.2f} = €{smaken_teller[smaak] * prijs_per_bolletje:.2f}")

#     print("---------------------+")
#     print(f"Totale prijs: €{totale_prijs:.2f}")
#     print("Bedankt voor uw bestelling!")
#     print("---------------------")

# def vraag_bolletjes():
#     while True:
#         try:
#             bolletjes = int(input("aantal bolletjes "))
#             if bolletjes <= 0:
#                 print('Vul getal groter dan 0')
#             elif bolletjes <= 8:
#                 break 
#             else:
#                 print('Sorry, zulke grotebakken hebben we niet')
#         except:
#             print("vul een cijfer in")
#     return bolletjes
# def vraag_bakje(bolletjes):
#     hoorntje_of_bakje = 'bakje'
#     if bolletjes <= 3:
#             while True:
#                 try:
#                     hoorntje_of_bakje = str(input(f'Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje? '))
#                     if hoorntje_of_bakje in('hoorntje' , 'bakje') :
#                         break
#                     else:
#                         print('sorry ik snap het niet')
#                 except:
#                     print("Je kan allen kiezen tussen hoorntje of bakje")
#     print(f"hier is uw {hoorntje_of_bakje} met {bolletjes} bolletje(s)")
#     return hoorntje_of_bakje

# def vraag_meer_bestellen():
#     while True:
#         meerBestellen = str(input("wilt u meer bestellen?"))
#         if meerBestellen in ("ja"):
#             return True
#         elif meerBestellen in("nee"):
#             return False
#         else:
#             print("sorry dit antwoord snap ik niet type ja of nee")
# def vraag_smaken(bolletjes):
#     smaken = []
#     smaken_teller = 0
#     for i in range(bolletjes):
#         while True:
#             smaak = input(f"Welke smaak wilt u voor bolletje nummer {i+1}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? ")
#             if smaak.upper() in ("A", "C", "M", "V"):
#                 if smaak.upper() == "A":
#                     if smaak in smaken:
#                         smaken_teller =+1
#                     else: 
#                         smaken_teller = 1 
#                     smaken.append("Aardbei")
#                 elif smaak.upper() == "C":
#                     if smaak in smaken:
#                         smaken_teller =+1
#                     else: 
#                         smaken_teller = 1
#                     smaken.append("Chocolade")
#                 elif smaak.upper() == "M":
#                     if smaak in smaken:
#                         smaken_teller =+1
#                     else: 
#                         smaken_teller = 1
#                     smaken.append("Munt")
#                 elif smaak.upper() == "V":
#                     if smaak in smaken:
#                         smaken_teller =+1
#                     else: 
#                         smaken_teller = 1
#                     smaken.append("Vanille")
#                 break
#             else:
#                 print("Sorry, dat begrijp ik niet. Probeer het opnieuw.")
#     return smaken , smaken_teller
# def maak_een_bon(aantal_bolletjes, aantal_bakjes, aantal_hoorntjes, smaken , smaken_teller):
#     prijs_per_bolletje = 1.10
#     prijs_per_hoorntje = 1.25
#     prijs_per_bakje = 0.75
#     totale_prijs_hoorntjes = aantal_hoorntjes * prijs_per_hoorntje
#     totale_prijs_bakjes = aantal_bakjes * prijs_per_bakje
#     totale_prijs_bolletjes = aantal_bolletjes * prijs_per_bolletje

#     totale_prijs = totale_prijs_hoorntjes + totale_prijs_bakjes + totale_prijs_bolletjes

#     print("-------- BON --------")
#     print(f"Aantal bolletjes: {aantal_bolletjes} x €{prijs_per_bolletje:.2f} = €{totale_prijs_bolletjes:.2f}")
#     print(f"Hoorntjes: {aantal_hoorntjes} x €{prijs_per_hoorntje:.2f} = €{totale_prijs_hoorntjes:.2f}")
#     print(f"Bakjes: {aantal_bakjes} x €{prijs_per_bakje:.2f} = €{totale_prijs_bakjes:.2f}")
#     for smaak in smaken:
#         print(f"{smaak} {smaken_teller} x €{prijs_per_bolletje:.2f} = €{prijs_per_bolletje:.2f}")
#     print("---------------------+")
#     print(f"Totale prijs: €{totale_prijs:.2f}")
#     print("Bedankt voor uw bestelling!")
#     print("---------------------")




# # def maak_een_bon(aantal_bolletjes, aantal_bakjes, aantal_hoorntjes , smaken):
# #     prijs_per_bolletje = 1.50
# #     prijs_per_hoorntje = 1.25
# #     prijs_per_bakje = 0.75
# #     totale_prijs_hoorntje =  aantal_hoorntjes * prijs_per_hoorntje
# #     totale_prijs_bakje = aantal_bakjes * prijs_per_bakje
# #     totale_prijs_bolletjes= aantal_bolletjes * prijs_per_bolletje

# #     totale_prijs = totale_prijs_hoorntje + totale_prijs_bakje + totale_prijs_bolletjes

# #     print("-------- BON --------")
# #     print(f"Aantal bolletjes: {aantal_bolletjes} x €{prijs_per_bolletje:.2f} = €{totale_prijs_bolletjes:.2f}")
# #     print(f"hoorntjes: {aantal_hoorntjes} x €{prijs_per_hoorntje:.2f} = €{totale_prijs_hoorntje:.2f}")
# #     print(f"bakjes: {aantal_bakjes} x €{prijs_per_bakje:.2f} = €{totale_prijs_bakje:.2f}")
# #     print(f"{smaken}")
# #     print("---------------------+")
# #     print(f"Totale prijs: €{totale_prijs:.2f}")
# #     print("Bedankt voor uw bestelling!")
# #     print("---------------------")
   