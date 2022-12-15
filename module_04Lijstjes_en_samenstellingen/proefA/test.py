import random

# create empty list for names
names = []

# loop until user is done entering names
while True:
    name = input("Enter a name: ")  # get user input for name
    names.append(name)  # add name to list
    response = input("Do you want to enter another name? (yes/no) ")  # ask user if they want to enter more names
    if response.lower() == "no":  # exit loop if user does not want to enter more names
        break

# shuffle names using random.sample() function
shuffled_names = random.sample(names, len(names))

print(shuffled_names)  # print shuffled names




