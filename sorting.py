numbers = [58, 3, 25, 1, 6, 23, 7, 56]

#fabrication de la variable permutation
def permutation(numbers, i) :
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
    return moved +1

moved = 0
sorted = False
    
while sorted == False :
    i = 0
    while i < len(numbers) - 1 :
        if numbers[i+1] < numbers[i] :
            moved = permutation(numbers, i)
        i = i+1
    if moved == 1 or moved == 0 :
        sorted = True
    moved = 0;
        
print(numbers) 





# [58, 3, 25, 1, 6, 23, 7, 56] => 7 permutations
# [3, 25, 1, 6, 23, 7, 56, 58] => 4 permutations
# [3, 1, 6, 23, 7, 25, 56, 58] => 2 permutations
# [1, 3, 6, 7, 23, 25, 56, 58]