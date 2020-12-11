#11 - The Meaning of Liff
input = open('input.txt', 'r')
inputs = input.readlines()
gameOfLife = [[]]
nextGame = [[]]
def createSeats():
	i = 0
	for line in inputs:
		line = line.strip()
		gameOfLife.append([])
		for character in line:
			gameOfLife[i].append(character)
		#print (gameOfLife[i])
		i +=1



def iterate():
	numRows = len(gameOfLife)-1; numCols = len(gameOfLife[0])
	print(numRows,numCols)
	nextStep = [[]]
	changes = 0
	for i in range(numRows):
		nextStep.append([])
		firstX,lastX = i-1,i+1
		if firstX == -1: firstX = i
		if lastX == numRows: lastX = numRows-1
		for j in range(numCols):
			nextStep[i].append(gameOfLife[i][j])
			firstY,lastY = j-1,j+1
			if firstY == -1: firstY = 0
			if lastY == numCols: lastY = numCols-1
			x = y = 0
			neighbours = 0
			for x in range(firstX,lastX+1):				
				for y in range (firstY,lastY+1):
					if not (x == i and y == j):
						#print (x,y, numRows, numCols)
						if gameOfLife[x][y] == "#": neighbours += 1
				#print ("")
				
			#print ("*",neighbours,"*")
			if neighbours == 0 and gameOfLife[i][j] == "L": nextStep[i][j] = "#"; changes += 1
			if neighbours >= 4 and gameOfLife[i][j] == "#": nextStep[i][j] = "L"; changes += 1
	#print (len(nextStep)-1,len(nextStep[0]))
	numSeats = 0
	for row in range (numRows):
		for col in range(numCols):
			# print(row, col)
			gameOfLife[row][col] = nextStep[row][col]
			if gameOfLife[row][col] == "#": numSeats +=1
		#print (gameOfLife[row])
	print (numSeats)
	return changes
createSeats()	
change = iterate()	
numIterations = 1
while change > 0:
	change = iterate()
	numIterations += 1
#print (numIterations)