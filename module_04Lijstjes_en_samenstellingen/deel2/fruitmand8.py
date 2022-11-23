from fruitmand import fruitmand

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2000,
    'color' : 'green',
    'round' : True
}

)
totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht= totaal_gewicht + fruit["weight"]
print(f"{totaal_gewicht} gram")