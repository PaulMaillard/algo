#Les conditions
#by Paul Personne
#BeWeb

a = False

if a == True :
	print("ok")

if a :
	print("ok")

a = 10
b = 10

if a < b :
	print("a inferieur a b")
elif a == b :
	print("a egal a b")
else :
	print("a superieur a b")

momentJournee = "nuit"
etatLumiere = "allumee"
sommeil = True

#conditions avec les operateurs logiques ( ET OU NON )
if momentJournee == "jour" and etatLumiere == "allumee" :
	print("il fait jour")
	print("j'eteins ma lumiere")
elif momentJournee == "jour" and etatLumiere == "eteinte" :
	print("il fait jour")
	print("j'allume une clope")
elif momentJournee == "nuit" and etatLumiere == "eteinte" :
	print("il fait nuit")
	print("j'allume ma lumiere")
elif momentJournee == "nuit" and etatLumiere == "allumee" :
	print("il fait nuit")
	if sommeil :
		print("j'eteins ma lumiere")
	else :
		print("j'emmerde le monde")

#equivalent au precedent en conditions imbriquees
if momentJournee == "jour" :
	print("il fait jour")
	if etatLumiere == "allumee" :
		print("j'eteins ma lumiere")
	elif etatLumiere == "eteinte" :
		print("j'allume une clope")
elif momentJournee == "nuit" :
	print("il fait nuit")
	if etatLumiere == "allumee" :
		if sommeil :
			print("j'eteins ma lumiere")
		else :
			print("j'emmerde le monde")
	elif etatLumiere == "eteinte" :
		print("j'allume ma lumiere")
