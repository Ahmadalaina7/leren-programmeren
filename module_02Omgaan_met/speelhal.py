aantal_personen = int(input('voor hoeveel personen?'))

entree = aantal_personen * 7.45

vr = int(input('hoeveel minuten wilt uw VIP-VRGameSeat?'))

vrminuten = vr / 5

vr_totaal = vrminuten * 0.37 * aantal_personen

totaal= vr_totaal + entree * 100

totaal_Af = round (totaal,0) #euro afronden

print(f'''Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {vr} minuten VR kost je maar {totaal_Af} cent''')