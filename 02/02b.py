#02 - There are some who call me Tim
input = open('input.txt', 'r')
inputList = input.readlines()
failPass = 0
goodPass = 0
for entry in inputList:
	entryList = entry.split(" ")
	passPositions = entryList[0].split("-")
	pos1 = int(passPositions[0]) - 1
	pos2 = int(passPositions[1]) - 1
	passLetter = entryList[1][:1]
	countLetter = 0
	#for token in passStrengths:
		#print (token, end = ",")
	#print(passLetter)
	print(entryList[2][pos1:pos1+1], entryList[2][pos2:pos2+1], "*")
	firstChar = entryList[2][pos1:pos1+1] 
	secondChar = entryList[2][pos2:pos2+1]
	
	
	
	print (countLetter, passLetter)
	
	if (firstChar == passLetter) ^ (secondChar == passLetter):
		print("WHAT... is your favourite colour?")
		goodPass = goodPass + 1
	else:
		print("WHAT... is the airspeed velocity of an unladen swallow?")
		failPass = failPass + 1
print("Tim claimed", failPass, "seekers of the Grail.")
print("Tim allowed through", goodPass, "seekers of the Grail.")
	