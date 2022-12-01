from fruitmand import fruitmand
naam = ''
kleur = ''
gewicht = 0
letters = 0
longFruit = fruitmand[0]
for fruit in fruitmand:
    if len(longFruit['name']) < len(fruit['name']):
        longfruit = fruit
        naam = fruit['name']
        kleur = fruit['color']
        gewicht = fruit['weight']
        letters = len(fruit['name'])
print(f"De {naam} ({letters}) heeft een {kleur} kleur en een gewicht van {gewicht / 1000} kg.")