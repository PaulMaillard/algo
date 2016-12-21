    
birthYear = 1979
birthMonth = 9
birthDay = 15
currentYear = 2016
currentMonth = 11
currentDay = 13
age = currentYear-birthYear

if currentMonth < birthMonth or currentMonth == birthMonth and currentDay < birthDay :
    age = age-1
    
print("the captain is " + str(age) + " years old.")