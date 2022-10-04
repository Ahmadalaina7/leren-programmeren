print('speeltuin entree')

# welkom voor kinderen van 12 of onder de 12, maar alleen met een begeleider van 20 of ouder
# of welkom als ze onder de 14 zijn en een speeltuinpasje hebben
# of welkom als ze een begeleider hebben met de naam Vladimir 
leeftijd = int(input(" Wat is je leeftijd ? "))
pasje = input(" heb je een pasje ? ")
begeleider = input(" heb je een begeleider ? ")
if begeleider == 'ja': 
  leeftijd_begeleider = int(input(" Wat is de leeftijd van je begeleider ? "))
  naam_begeleider = input(" Wat is de naam van je begeleider ? ")
else:
  pass
if leeftijd >= 12 and begeleider == "ja" and leeftijd_begeleider >= 20 or leeftijd <= 14 and pasje == "ja12" or begeleider == 'vladmir': 
  print('welkom')
else:
  print('sorry, niet welkom')

