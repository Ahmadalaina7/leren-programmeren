geel = input("is de kaas geel ? (ja/nee) ")
if geel == "nee":
    schimmel = input("heeft de kaas blauwe schimmel?(ja/Nee) ")

    if schimmel == "ja":
        korst = input("heeft de kaas een korst? (ja/Nee) ")

        if korst == "ja":
            print("Blue de Rochbaron")

        else:
            print("Foume d'Ambert")

    else:
        korst1 = input("heeft de kaas een korst? (ja/nee) ")

        if korst1 == "ja":
            ## als de kaas stinkt dan is het camembert
            print("Camembert") 
            

        else:
            print("Mozzarella")

if geel == "ja":
    gaten = input("Zitten er gaten in? (ja/nee) ")

    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? (ja/Nee) ")

        if duur == "ja":
            print("Emmenthaler")

        else:
            print("Leerdammer")

    else:
        steen = input("Is de kaas hard als steen? (ja/Nee) ")

        if steen == "ja":
            print("Parmigiano Reggiano")

        else:
            print("Goudse kaas")
