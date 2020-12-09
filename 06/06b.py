#06 - Yes it is! No it isn't!
input = open('input.txt', 'r')
inputs = input.readlines()
list1 = ''
final = ''
answerCount = 0
lineCount = 0
for line in inputs:
	if line != '\n':
		final = line.strip()
		list1 = list1 + final
		lineCount = lineCount + 1
	else:
		print(list1)
		lookupPos = 0
		groupACount = 0
		print ("People in group:",lineCount)
		print ("Found letters:", end = "")
		for letter in list1:
			if list1.find(letter) == lookupPos:
				letterCount = list1.count(letter)
				if letterCount == lineCount:
					groupACount = groupACount+1
					print (letter, "(",letterCount,")", end = ",")
			lookupPos = lookupPos +1
		list1 = ''
		print (groupACount)
		answerCount = answerCount + groupACount
		lineCount = 0
print ("Total number of arguments in this sketch: ", answerCount)
		
		