
birthYear = 1979
birthMonth = 9
birthDay = 15
currentYear = 2016
currentMonth = 11
currentDay = 13
age = currentYear-birthYear

if currentMonth < birthMonth || currentMonth == birthMonth && currentDay < birthDay
    age = age-1
end
	
print "The captain is #{age} years old.\n"