numbers = [3, 25, 1, 6, 23, 56]

#fabrication de la variable permutation
def permutation(numbers,i)
    temp = numbers[i]                   #la variable temp prend la valeur de l'index courant
    numbers[i] = numbers[i+1]           #l'index courant prend la valeur de l'index suivant
    numbers[i+1] = temp                 #l'index suivant prend la valeur de la variable temp
    return true                         #la fonction retourne vrai
end

sorted = false                          #j'initialise une variable sorted en faux

while sorted == false                   #tant que la variable sorted retourne faux
    moved = false                       #j'initialise une variable moved à faux
    i = 0                               #et une variable i à 0)
    while i < numbers.length - 1        #tant que la variable i est inferieure à la longueur du tableau - 1
        if numbers[i+1] < numbers[i]    #si le nombre de l'index suivant est plus grand que le nombre de l'index actuel
            moved = permutation(numbers,i) #la fonction permutation s'execute, et son retoune = vrai s'applique à la fonction moved
        end
    i += 1                              #(toujours tant que la variable sorted retourne faux) la fonction i augmente de 1
    end                         

        if moved == false               #si la fonction moved retourne faux, notre algo n'a pas dû permuter de valeur dans le tableau, donc le tableau est classé
            sorted = true               #la fonction sorted devient vrai, et on sort de la boucle tantque de la ligne 13
        end
end

print(numbers)
puts