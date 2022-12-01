from operator import itemgetter
from fruitmand import fruitmand
# fruitmand = sorted(fruitmand , key = itemgetter('weight', 'name'), reverse=True)

# for fruit in fruitmand: 
#     print(fruit['weight'], fruit['name'])

fruitmand.sort(reverse = True, key = lambda fruit : fruit['weight'] )
print(fruitmand)