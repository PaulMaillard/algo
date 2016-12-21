numbers = [3, 25, 1, 6, 23, 56]

#fabrication de la variable permutation
def permutation(numbers, i) :
    temp = numbers[i]
    numbers[i] = numbers[i+1]
    numbers[i+1] = temp
    return True

sorted = False
    
while sorted == False :
    moved = False
    i = 0
    while i < len(numbers) - 1 :
        if numbers[i+1] < numbers[i] :
            moved = permutation(numbers, i)
        i = i+1
    if moved == False :
        sorted = True
        
print(numbers) 