bag = {}
vraag = input("Wil je een product toevoegen?: ").lower()    
while vraag == "ja":
    
    product = input("Welke product wil je?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    

    if product not in bag:
        bag.update({product: aantal})    
    else:
        bag[product] += aantal
    vraag2 = input("Wil je nog een product toevoegen?: ").lower()
    if vraag2 == "nee":
        break

print("-[ BOODSCHAPPENLIJST ]-")
for a , p in bag.items():
    print(f"{a} x {p}")
print("-----------------------")
   