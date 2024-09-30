iphone_bedrag = int(input("hoe duur is de iphone telefoon ? "))
samsung_bedrag = int(input("hoe duur is de samsung telefoon ? "))
som1 = iphone_bedrag - samsung_bedrag
som2 = samsung_bedrag - iphone_bedrag
if (iphone_bedrag > 900 and samsung_bedrag > 900):
    print("Het advies is dus geen telefoon te kopen , ze zijn te duur ")
    exit()
    
if iphone_bedrag > samsung_bedrag:
    print(f'''De ipohne is het duurste , de iphone koste {iphone_bedrag} Euro
     De samsung kost {samsung_bedrag} Euro
     is {som1} Euro duurder''')
    if iphone_bedrag - samsung_bedrag < 51:
        print(" het advies is om iphone te kopen")
    elif iphone_bedrag - samsung_bedrag > 51:
        print("het advies is om samsung te kopen")

elif iphone_bedrag < samsung_bedrag:
    print(f'''De iphone is het goedkoopst, de iphone kost {iphone_bedrag} Euro
    en de samsung kost {samsung_bedrag} Euro 
    de iphone is {som2} Euro goedkoper''')
    if iphone_bedrag - samsung_bedrag < 51:
        print(" het advies is om iphone te kopen")
    elif iphone_bedrag - samsung_bedrag > 51:
        print("het advies is om samsung te kopen")

else:
    print(" de telefoons zijn even duur het advies is om de telefoon met een betere kwaliteiten te kiezen")
