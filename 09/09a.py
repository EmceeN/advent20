#09 - Thou Must Count To Three

input = open('input.txt', 'r')
inputs = input.readlines()
preamble = []
preambleLen = 25
i, testNum, target, operand = 0, 0, 0, 0
testArray = []
for line in inputs:
	preamble.append(line.strip())
	if i >= preambleLen:
		isValid = False
		testNum = int(line)
		for j in range(0,preambleLen-1):
			operand = preamble[j]
			target = testNum - int(operand)
			print (testNum,"-",operand,"=",target)
			print (preamble[j+1:preambleLen])
			if str(target) in preamble:
				print ("Valid number found:",target)
				isValid = True
				break
		if isValid == False:
			print ("Thou must count to", testNum)
			break
		preamble.pop(0)
	i += 1

