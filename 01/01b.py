# 01a - The Crimson Permanent Assurance
input = open('input.txt', 'r')
inputList = input.readlines()
isAnswered = 0
for entry in inputList:
	entry = int(entry)
	#print(entry, '*')	
	#print(match)
	for entry2 in inputList:
		entry2 = int(entry2)
		match = 2020 - entry - entry2
		#if match > 0:
			#print (match)
		for entry3 in inputList:
			entry3 = int(entry3)
			if entry3 == match:
				answer = entry*entry2*match
				print('****ANSWER: ', entry, ' * ', entry2, ' * ', match, ' = ', answer)
				isAnswered = 1
				break
		if isAnswered == 1:
			break
			
		
				
		