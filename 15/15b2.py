#15 - When he says a bed is two foot long, it is infact sixty foot long
from datetime import datetime
with open('input.txt', 'r') as input:
	inputs = input.readlines()
nums = inputs[0].split(","); 
numDict = {}
i = 0
for num in nums:
	numDict[int(num)] = i
	i += 1
print (numDict)
lastFound = 0
turn = len(nums)
start = datetime.now()
print (start)
print (nums)
limit = 30000000
print (turn)
lastNum = int(nums[-1])
lastTime  = turn - 1
while turn < limit:
	isFound = 0
	#print ("###Turn",turn+1,": Guessing number", lastNum)
	#print ("Last time was", lastTime)
	if lastNum in numDict: 
		lastFound = numDict[lastNum]
		#print ("found at", lastFound)
		if lastFound > lastTime: isFound = 1; lastNum = lastFound - lastTime
	if isFound == 0: lastNum = 0
	try: lastTime = numDict[lastNum]
	except: lastTime = turn
	numDict[lastNum] = turn
	#print (numDict, lastTime)
	#time = datetime.now()-start
	#if turn % 1000000 == 0: print ("Guessing number", turn, time)
	turn+=1
	#print (i, lastNum,)
print ("We got tired after",limit,"turns, the last number was", lastNum)	
time = datetime.now()-start
print (time)
