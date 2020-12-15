#15 - When he says a bed is two foot long, it is infact sixty foot long
with open('input.txt', 'r') as input:
	inputs = input.readlines()

nums = inputs[0].split(","); nums.reverse()
x = 0
a= 0
i = len(nums)
while i < 2020:
	lastNum = nums[0]
	if lastNum in nums[1:]: 
		x = nums[1:].index(lastNum)
		nums.insert(0, str(x+1))
	else: nums.insert(0,'0'); x = -1
	i+=1
	#print (i, lastNum, i-1, x, nums[0])
print ("We got tired after 2,020 turns, the last number was", nums[0])	
	