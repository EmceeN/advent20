#10 - Sir Lancelot's Charge
input = open('input.txt', 'r')
inputs = input.readlines()
inputInts = [int(i) for i in inputs]
inputInts.sort()
numAdapters = len(inputInts)
inputInts.append(inputInts[numAdapters-1] +3)
i, oneJolt, threeJolts, highJoltage = 0,0,0,0
permutations, withinThree = 1,0
inARow = 0
permutations = 1

def GetPermutations(n):
	tList = [0,0,1]
	t1, t2, t3 = 0, 0, 0
	if n < 2: return 1
	elif n == 2: return 2
	else:
		for i in range(3,n+3):
			t1, t2, t3 = int(tList[i-3]),int(tList[i-2]),int(tList[i-1])
			tList.append(t1+t2+t3)
	return tList[-1]
for adaptor in inputInts:
	lastJoltage = 0
	thisJoltage = adaptor
	if i > 0: lastJoltage = inputInts[i-1]
	diff = thisJoltage - lastJoltage
	if diff == 1: 
		oneJolt += 1
		inARow += 1
	if diff == 3: 
		threeJolts += 1
		permutations *= GetPermutations(inARow)
		inARow =  0
	i+=1
highJoltage = oneJolt * threeJolts
print (highJoltage, "jolts")
print (oneJolt, threeJolts)
print (permutations)
