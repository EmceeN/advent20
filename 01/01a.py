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
		match = 2020 - entry
		if entry2 == match:
				answer = entry*match
				print('****ANSWER: ', entry, ' * ', match, ' = ', answer)
				isAnswered = 1
				break
		if isAnswered == 1:
			break
			
		
				
		