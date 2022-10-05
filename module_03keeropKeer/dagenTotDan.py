dagen = ["maandag","dinsdag", "woensdag" , "donderdag" , "vrijdag" , "zaterdag" , "zondag"]

while True :
    dag = input("kies een dag van de week uit ? ").lower()
    if dag in dagen: 
        break

    else:
        print(" voer de naam van de dag goed in!")

index = 0

while True:
    print(dagen[index])
    if dagen[index] == dag:
        break

    index += 1
