#02 - There are some who call me Tim
input = open('input.txt', 'r')
inputList = input.readlines()
failPass = 0
goodPass = 0
for entry in inputList:
	entryList = entry.split(" ")
	passStrengths = entryList[0].split("-")
	passLetter = entryList[1][:1]
	countLetter = 0
	#for token in passStrengths:
		#print (token, end = ",")
	#print(passLetter)
	for letter in entryList[2]:
		if letter == passLetter:
			countLetter = countLetter + 1
	print (countLetter, passLetter)
	minStrength = int(passStrengths[0])
	maxStrength = int(passStrengths[1])
	if countLetter >= minStrength and countLetter <= maxStrength:
		print("WHAT... is your favourite colour?")
		goodPass = goodPass + 1
	else:
		print("WHAT... is the airspeed velocity of an unladen swallow?")
		print("You need between", passStrengths[0], "and", passStrengths[1], "instances of", passLetter)
		failPass = failPass + 1
print("Tim claimed", failPass, "seekers of the Grail.")
print("Tim allowed through", goodPass, "seekers of the Grail.")
	