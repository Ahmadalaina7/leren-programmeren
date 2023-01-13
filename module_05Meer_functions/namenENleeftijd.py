# def naamENleeftijd():
#     namen = []
#     leeftijd = []

#     while True:
#         vraagNaam = input("wat is jou naam ?  vul stop in als je klaar bent ! ")
#         if vraagNaam == "stop":
#             break
#         vraagLeeftijd = input("wat is jou leeftijd ? vul stop in als je klaar bent !")
#         if vraagLeeftijd == "stop":
#             break
#         namen.append(vraagNaam)
#         leeftijd.append(vraagLeeftijd)
#     x = zip(namen , leeftijd)
#     return x

# for n , l in naamENleeftijd():
#     print(f"{n} is {l} jaar oud ")
def print_age_and_name(age, name):
  print(f"{name} is {age} jaar oud ")
while True:
    age = input("Please enter your age: ")
    if age == "stop": 
        break
    name = input("Please enter your name: ")
    if name == "stop":
        break
    print_age_and_name(age, name)
