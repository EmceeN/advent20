#03 - The Larch
input = open('input.txt', 'r')
slope = input.readlines()
numLarch = 0
slopeWidth = len(slope[0]) - 1
slopeHeight = len(slope)
sledPos = 0
sledMove = 0
print("The slope is",slopeHeight,"metres high.")
for metre in slope:
	print (slopeWidth)
	sledPos = (3 * sledMove) % slopeWidth
	print (sledMove, sledPos)
	if slope[sledMove][sledPos:sledPos+1] == "#":
		numLarch = numLarch+1
		print ("Number", numLarch,". The Larch")
	sledMove = sledMove +1
print("You encountered", numLarch, "larches.")