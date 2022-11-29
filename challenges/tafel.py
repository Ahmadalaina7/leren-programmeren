# tafels = [1,2,3,4,5,6,7,8,9,10]

# for x in range (1,14):
#     print(f"tafel van : {x}")
#     for i in tafels:
#         print(f"{i} x {x} = {x*i}")
# opdracht 2-----------------------------------
# lijst = [5,12,19,27,3]
# lijst.append(25)
# opdracht 3----------------------------------
# lijst = [5,12,19,27,3]
# lijst.append(25)
# print (lijst)
#  opdracht 4----------------------------------
# lijst = [5,12,19,27,3]
# lijst.append(25)
# print ((len(lijst)))
#  opdracht 5----------------------------------
# lijst = [5,12,19,27,3]
# lijst.append(25)
# lijst.remove(12)
# print (lijst)
#  opdracht 6----------------------------------
# lijst = [5,12,19,27,3]
# lijst.append(25)
# lijst.remove(12)
# lijst.remove(5)
# print (lijst)
#  opdracht 7----------------------------------
# lijst = [5,12,19,27,3]
# lijst.insert(0,36)
# lijst.append(25)
# lijst.remove(12)
# lijst.remove(5)
# print (lijst)
#  opdracht 8----------------------------------
# lijst = [36,19,27,3,25]
# print(sum(lijst))
#  opdracht 9----------------------------------
# lijst = [36,19,27,3,25]
# lijst.clear()
# print(lijst)
#  opdracht 10----------------------------------
# lijst = []
# lijst.extend([1,2,3])
# print(lijst)
#  opdracht 11----------------------------------
# lijst = [1,2,3]
# for x in range(4,51):
#     lijst.append(x)
# print(lijst)
#  opdracht 12----------------------------------
# lijst = [1,2,3]
# for x in range(4,51):
#     lijst.append(x)
# print(lijst)
# print(lijst.index(25))
#  opdracht 13----------------------------------
# lijst = [1,2,3]
# for x in range(4,51):
#     lijst.append(x)
#     lijst.reverse()
# print(lijst)
#  opdracht 14---------------------------------
lijst = [1,"aap",2,"apen",3,"watermeloen",15,27,15,"lekkerbezig","6"]
numbers = [1 , 2 , 3 , 15 , 27 ,15]
for item in lijst:
    for subitem in item.split():
        if(subitem.isdigit()):
            numbers.append(subitem)
print(numbers)