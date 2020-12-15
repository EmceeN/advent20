#15 - When he says a bed is two foot long, it is infact sixty foot long
with open('input.txt', 'r') as input:
	inputs = input.readlines()
nums = inputs[0].split(","); 
numDict = {}
i = 0
for num in nums:
	numDict[int(num)] = i
	i += 1
lastFound = 0
turn = len(nums)
limit = 30000000
lastNum = int(nums[-1])
lastTime  = turn - 1
while turn < limit:
	isFound = 0
	if lastNum in numDict: 
		lastFound = numDict[lastNum]
		if lastFound > lastTime: isFound = 1; lastNum = lastFound - lastTime
	if isFound == 0: lastNum = 0
	try: lastTime = numDict[lastNum]
	except: numDict[lastNum] = lastTime = turn
	numDict[lastNum] = turn
	turn+=1
print ("We got tired after",limit,"turns, the last number was", lastNum)	

