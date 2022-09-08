print('Hello, typ je besteling in')
croissantjes = int(input('hoeveel croissantjes wilt u?'))
crtotaal = croissantjes * 0.39
stokbrood = int(input('hoeveel stokbrood wilt u?'))
stoktotaal = stokbrood * 2.78
aantal_kortingsbonen = int(input('hoeveel kortings bonnen heeft uw?'))
korting = int(input('hoeveel cent zijn ze waard?'))
korting_total = aantal_kortingsbonen * korting / 100

17
totaal= stoktotaal + crtotaal - korting_total
totaal_cent = totaal * 100
totaal_af = round(totaal_cent,0)
print(f'''De feestlunch kost je bij de bakker {totaal_af} cent voor de {croissantjes}  croissantjes en de {stokbrood} stokbroden als de {aantal_kortingsbonen} kortingsbonnen nog geldig zijn!''')