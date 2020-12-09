#09 - Thou Must Count To Three

input = open('input.txt', 'r')
inputs = input.readlines()
preambleLen = 25
i, testNum, target, operand, answer = 0, 0, 0, 0, 0
preamble = []
testArray = []
for line in inputs:
	preamble.append(line.strip())
	if i >= preambleLen:
		isValid = False
		testNum = int(line)
		for j in range(0,preambleLen-1):
			operand = preamble[j]
			target = testNum - int(operand)
			if str(target) in preamble:
				#print ("Valid number found:",target)
				isValid = True
				break
		if isValid == False:
			#print ("Thou must count to", testNum)
			i2 = 0
			for baseNum in inputs:
				addArray = [int(baseNum)]
				baseNum = int(inputs[i2])
				testSum = baseNum
				j2 = i2+1
				
				while testSum < testNum:
					addArray.append(int(inputs[j2]))
					testSum = testSum + int(inputs[j2])
					#print (baseNum, testSum)
					j2 += 1
					
				if testSum == testNum:
					print ("Matching sum found!")
					#print (addArray)
					answer = max(addArray)+min(addArray)
					print (max(addArray), "+", min(addArray), "=", answer)
					break
				i2 += 1	
			
			break
		preamble.pop(0)
	i += 1

