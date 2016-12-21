#Exercice sur les variables
#Written by Paul Personne
#Beweb Lunel

print("*****affichage + typage*****")
#affichage des variables sur la sortie standard
#les variables sont typees dynamiquement
#affectation d'une chaine de caracteres (string)
maVariable = "Hello World!"
#envoi sur la sortie standard
print(maVariable)
#affectation d'une valeur numerique (integer/entier)
maVariable = 255
#envoi de la nouvelle valeur de ma variable sur la sortie standard
print(maVariable)

print("***********calcul***********")
#calcul sur les variables numeriques (type integer)
a = 10
b = 20
resultat = 0

print(resultat)
resultat = a + b
print(resultat)
resultat += 1
print(resultat)
resultat -= a
print(resultat)

print("***concatenation de chaine***")
#concatenation de chaine
maChaine = "Hello World!"
myNumber = 1258
maChaine2 = " Go fuck yourself World!"
#attention impossible de traiter par operation une chaine de caracteres (string)
#et un nombre (integer)
chaineAAfficher = maChaine + maChaine2
print(chaineAAfficher)
print(maChaine + maChaine2)

chaineAAfficher += " You piece of shit"
print(chaineAAfficher)

print("affichage de la valeur de la variable resultat du debut du code: " + str (resultat))




