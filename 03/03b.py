#03 - The Larch
input = open('input.txt', 'r')
slope = input.readlines()
def tobogganRun(Xmove,Ymove):
	numLarch = 0
	slopeWidth = len(slope[0]) - 1
	slopeHeight = len(slope)
	sledPos = 0
	sledMove = 0
	#print("The slope is",slopeHeight,"metres high.")
	for metre in slope:
		#print (slopeWidth)
		#print (sledMove % Ymove)
		if sledMove % Ymove == 0:
			sledPos = int(Xmove * sledMove / Ymove) % slopeWidth
			print (sledMove, sledPos)
			if slope[sledMove][sledPos:sledPos+1] == "#":
				numLarch = numLarch+1
				print ("Number", numLarch,". The Larch")
		sledMove = sledMove + 1
	#print("Moving ",Xmove,"metres right per",Ymove,"metres down, you encountered", numLarch, "larches.")
	return numLarch

#tobogganRun(1,2)
numLarches = [tobogganRun(1,1),tobogganRun(3,1),tobogganRun(5,1),tobogganRun(7,1),tobogganRun(1,2)]
print ("1,1:",numLarches[0])
print ("3,1:",numLarches[1])
print ("5,1:",numLarches[2])
print ("7,1:",numLarches[3])
print ("1,2:",numLarches[4])
print ("The answer is",numLarches[0]*numLarches[1]*numLarches[2]*numLarches[3]*numLarches[4])
