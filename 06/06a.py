#06 - Yes it is! No it isn't!
input = open('input.txt', 'r')
inputs = input.readlines()
list1 = ''
final = ''
answerCount = 0
for line in inputs:
	isFailed = 0
	if line != '\n':
		final = line.strip()
		list1 = list1 + final
	else:
		print(list1)
		lookupPos = 0
		groupACount = 0
		print ("Found letters:", end = "")
		for letter in list1:
			if list1.find(letter) == lookupPos:
				groupACount = groupACount+1
				print (letter, end = ",")
			lookupPos = lookupPos +1
		list1 = ''
		print (groupACount)
		answerCount = answerCount + groupACount
print ("Total number of arguments in this sketch: ", answerCount)
		
		