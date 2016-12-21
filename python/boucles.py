#Les boucles
#by Paul Personne
#BeWeb Lunel

iteration = 10

while iteration >= 0 :
	print("Iteration actuelle : " + str(iteration))
	iteration -= 1

pluie = True
eclair = False
vitesseDeLaLumiere = 5

while pluie :
	if vitesseDeLaLumiere == 0 :
		print("BOOM")
		eclair = True
	if eclair :
		print("STOP PLUIE")
		pluie = False
	if pluie :
		print("chanter sous la pluie")
		vitesseDeLaLumiere -= 1
		print("Vitesse de la lumiere : " + str(vitesseDeLaLumiere))

print
print("la boucle for : ")

for i in range(5) : #pour i allant de 0 a 4
	print("la valeur de i : " + str(i))

print
print("Meme effet avec une boucle while : ")

i = 0
while i < 5 :
	print("la valeur de i : " + str(i))
	i +=1
