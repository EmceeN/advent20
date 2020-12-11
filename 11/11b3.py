#11 - The Meaning of Liff
input = open('input.txt', 'r')
inputs = input.readlines()
gameOfLife = [[]]
nextGame = [[]]
numIterations, numSeats = 1,0
def createSeats():
	i = 0
	for line in inputs:
		line = line.strip()
		gameOfLife.append([])
		for character in line:
			gameOfLife[i].append(character)
		i +=1
def checkDiag(x, y, seatX):
	if gameOfLife[x][y] == "#" and x != seatX: return 1
	if gameOfLife[x][y] == "L" and x != seatX: return 0
	return 2
	
def checkSeat(seatX, seatY, dir):
	x = y = edgeX = edgeY = dirX = dirY = 0
	numRows = len(gameOfLife)-1; numCols = len(gameOfLife[0])
	if dir.find("N") >= 0: edgeX = -1; dirX = -1
	elif dir.find("S") >= 0: edgeX = numRows; dirX = 1
	if dir.find("W") >= 0: edgeY = -1; dirY = -1
	elif dir.find("E") >= 0: edgeY = numCols; dirY = 1
	if dirX != 0 and dirY == 0:
		for x in range(seatX, edgeX, dirX):				
			if gameOfLife[x][seatY] == "#" and x != seatX: return 1
			if gameOfLife[x][seatY] == "L" and x != seatX: return 0
	elif dirY != 0 and dirX == 0:
		for y in range(seatY, edgeY, dirY):
			if gameOfLife[seatX][y] == "#" and y != seatY: return 1
			if gameOfLife[seatX][y] == "L" and y != seatY: return 0
	elif dirX != 0 and dirY != 0:
		x, y, ans = seatX, seatY, 2
		if dir == "NW":
			while x > edgeX and y > edgeY and ans == 2:
				ans = checkDiag(x,y,seatX); x -= 1; y -= 1
		elif dir == "SW":
			while x < edgeX and y > edgeY and ans == 2:
				ans = checkDiag(x,y,seatX); x += 1; y -= 1			
		elif dir == "SE":
			while x < edgeX and y < edgeY and ans == 2:
				ans = checkDiag(x,y,seatX);	x += 1; y += 1
		elif dir == "NE":
			while x > edgeX and y < edgeY and ans == 2:
				ans = checkDiag(x,y,seatX);	x -= 1; y += 1
		if ans < 2: return ans
	else: return 0
	return 0
def iterate():
	numRows = len(gameOfLife)-1; numCols = len(gameOfLife[0])
	nextStep = [[]]
	change, numSeats = 0, 0
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
			neighbours = 0
			cardinals = ["N","NW","W","SW","S","SE","E","NE"]
			if gameOfLife[i][j] != ".":
				for dir in cardinals: neighbours += checkSeat(i, j, dir)
				if neighbours == 0 and gameOfLife[i][j] == "L": nextStep[i][j] = "#"; change += 1
				if neighbours >= 5 and gameOfLife[i][j] == "#": nextStep[i][j] = "L"; change += 1
	for row in range (numRows):
		for col in range(numCols):
			gameOfLife[row][col] = nextStep[row][col]
			if gameOfLife[row][col] == "#": numSeats +=1
	return change, numSeats
createSeats()	
change, numSeats = iterate()
while change > 0:
	change, numSeats = iterate()
	numIterations += 1
print (numSeats, "seats are full after", numIterations, "iterations")

	