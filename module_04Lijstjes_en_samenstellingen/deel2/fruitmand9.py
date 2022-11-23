from fruitmand import fruitmand
druifIndex =-1
for index in range (len(fruitmand)):
    if fruitmand[index]["name"] == "druif":
        druifIndex = index

if druifIndex != -1:
    fruitmand.pop(druifIndex)
    print(fruitmand)
colors = []
for fruit in fruitmand:
    if(fruit["color"]) not in colors:
        colors.append(fruit["color"])
print (colors)