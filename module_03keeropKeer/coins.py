# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # hier wordt met een input gevraagd naar het bedraag wat betaald moeten worden.
paid = int(float(input('Paid amount: ')) * 100) # hier wordt met een input ook gevraagd naar de betaalde bedraag.
change = paid - toPay # hier wordt het wisselgeld berekend
receipte = " "
if change > 0: # Als de wisselgeld meer dan 0 is begint de programma.
  coinValue = 500 # begin value van een coin
  
  while change > 0 and coinValue > 0: # start van de while loop stopt pas als alle wissel geld is gegeven
    nrCoins = change // coinValue # berekening change gedeeld door de coinvalue dan krijg je nrCoins

    if nrCoins > 0: # als er nog coin gegeven moet worden start de if
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # hier laat je zien hoeveel munten je van een coinvalue kan geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier vraagt die hoeveel coins je wilt treug geven 
      change -= nrCoinsReturned * coinValue # Change is - De aantal coins dat ingevoerd is keer de coinvalue
      Row = f' given {nrCoinsReturned} of {coinValue} cents \n '
      receipte = receipte + Row
# comment on code below: 
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

print(f"{receipte}")
if change > 0: # Hier laat hij de change zien dat is ingevuld + als de change niet is compleet terug gegeven
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')