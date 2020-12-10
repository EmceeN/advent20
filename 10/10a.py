#10 - Sir Lancelot's Charge
input = open('input.txt', 'r')
inputs = input.readlines()
inputInts = [int(i) for i in inputs]
inputInts.sort()
numAdapters = len(inputInts)
inputInts.append(inputInts[numAdapters-1] +3)
#inputInts.append(inputInts
print (inputInts)
i, oneJolt, threeJolts, highJoltage = 0,0,0,0
for adaptor in inputInts:
	print (i, "#")
	lastJoltage = 0
	thisJoltage = adaptor
	if i > 0: lastJoltage = inputInts[i-1]
	diff = thisJoltage - lastJoltage
	print (thisJoltage, "-", lastJoltage, "=", diff)
	if diff == 1: oneJolt += 1
	if diff == 3: threeJolts +=1
	i += 1
highJoltage = oneJolt * threeJolts
print (highJoltage, "jolts")
  
	