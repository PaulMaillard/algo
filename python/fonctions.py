#Les fonctions
#by Paul Personne
#Beweb Lunel

evenement = ["pleut", "beau", "neige", "grele"]

def affichageDuTemps(temps) :
	if temps == "beau" :
		temps = "fait " + temps
	print("Il " + temps)

longueurDuTableau = len(evenement)

for i in range(longueurDuTableau) : #pour i = 0 a i < longueur du tableau
	event = evenement[i]	#valeur pointee par l'index
	affichageDuTemps(event)
