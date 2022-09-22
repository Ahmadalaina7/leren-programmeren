iphone_bedrag = int(input("hoe duur is de iphone telefoon ? "))
samsung_bedrag = int(input("hoe duur is de samsung telefoon ? "))
som1 = iphone_bedrag - samsung_bedrag
som2 = samsung_bedrag - iphone_bedrag

if iphone_bedrag > samsung_bedrag:
    print(f'''De ipohne is het duurste , de telefoon koste {iphone_bedrag} Euro
     De samsung is het duurste de telefoon kost {samsung_bedrag} Euro
     is {som1} Euro duurder''')
    if iphone_bedrag - samsung_bedrag <= 50:
        print(" het advies is om iphone te kopen")
    elif iphone_bedrag - samsung_bedrag > 50:
        print("het advies is om samsung te kopen")

elif iphone_bedrag < samsung_bedrag:
    print(f'''De iphone is het goedkoopst, de telefoon kost {iphone_bedrag} Euro
    en de samsung  is het duurste de telefoon kost {samsung_bedrag} Euro 
    de iphone is {som2} Euro goedkoper''')
  
else:
    print(" de telefoons zijn even duur het advies is om iphone te kopen")
