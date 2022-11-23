bag = {}
extra_invoegen = "ja"
while extra_invoegen == "ja":
    product = input("Welke product wil je?: ").lower()
    aantal = int(input(f"Hoeveel {product} wil je?: "))
    if product not in bag:
        bag.update({product: aantal})    
    else:
        bag[product] += aantal
    extra_invoegen = input("Wil je nog een product toevoegen?: ").lower()
print("-[ BOODSCHAPPENLIJST ]-")
for a , p in bag.items():
    print(f"{a} x {p}")
print("-----------------------")
   