scoreE = int(input("vul uw score in van de excellente acties "))
scoreP = int(input("vul uw score in van de professionele acties "))
scoreO = int(input("vul uw score in van de onprofessionele acties "))
scoreS = int(input("vul uw score in van de slechte acties "))

totale_score = scoreE + scoreP - scoreO - scoreS
if scoreP == 8 and scoreE > 4 and scoreO == 0 and scoreS == 0:
    print(f" uw uitslag is Goed score  {totale_score} ")

elif (scoreS == 0 and totale_score > 7 and totale_score < 13) or (scoreS == 1 and totale_score > 9):
    print(f" uw uitslag is Voldoende score  {totale_score} ")

else:
    print(f" uw uitslag is helaas Onvoldoende score  {totale_score} ")
