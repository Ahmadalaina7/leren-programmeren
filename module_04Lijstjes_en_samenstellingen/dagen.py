dagen_van_de_week = ("maandag" , "dinsdag" , "woensdag" , "donderdag" , "vrijdag" , "zaterdag" , "zondag")
werkdagen = 0
print("-----------------------\n""dagen van de week\n""---------------------")
for i in range (6,-1,-1):
    print( dagen_van_de_week[i])
print("-----------------------\n""werkdagen\n""---------------------")
for werkdagen in range (5):
    print( dagen_van_de_week [werkdagen])
print("-----------------------\n""weekendagen\n""---------------------")
for weekenddagen in range (5,7):
    print( dagen_van_de_week [weekenddagen])
print("-----------------------\n""dagen van de week omgekeerd\n""---------------------")
for x in dagen_van_de_week[7:0:-1]:
    print(x)

print("-----------------------\n""werkdagen omgekeerd\n""---------------------")
for w in dagen_van_de_week[4::-1]:
    print(w)

print("-----------------------\n""weekenddagen omgekeerd\n""---------------------")
for w in dagen_van_de_week[6:4:-1]:
    print(w)