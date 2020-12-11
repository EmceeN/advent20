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
		i +=1
			
def checkSeat(seatX, seatY, dir):
	x = y = 0
	numRows = len(gameOfLife)-1; numCols = len(gameOfLife[0])
	
	if dir == "N": edgeX, edgeY, dirX, dirY = -1,0,-1,0
	if dir == "NW": edgeX, edgeY, dirX, dirY = -1,-1,-1,-1
	if dir == "W": edgeX, edgeY, dirX, dirY = 0,-1,0,-1
	if dir == "SW": edgeX, edgeY, dirX, dirY = numRows, -1, 1, -1
	if dir == "S": edgeX, edgeY, dirX, dirY = numRows, 0, 1, 0
	if dir == "SE": edgeX, edgeY, dirX, dirY = numRows, numCols, 1, 1
	if dir == "E": edgeX, edgeY, dirX, dirY = 0, numCols, 0, 1
	if dir == "NE": edgeX, edgeY, dirX, dirY = -1, numCols, -1, 1
	
	if dirX != 0 and dirY == 0:
		for x in range(seatX, edgeX, dirX):				
			if gameOfLife[x][seatY] == "#" and x != seatX: return 1
			if gameOfLife[x][seatY] == "L" and x != seatX: return 0
	elif dirY != 0 and dirX == 0:
		for y in range(seatY, edgeY, dirY):
			if gameOfLife[seatX][y] == "#" and y != seatY: return 1
			if gameOfLife[seatX][y] == "L" and y != seatY: return 0
	elif dirX != 0 and dirY != 0:
		x, y, ans = seatX, seatY, 0
		if dir == "NW":
			while x > edgeX and y > edgeY:
				if gameOfLife[x][y] == "#" and x != seatX: return 1
				if gameOfLife[x][y] == "L" and x != seatX: return 0
				x -= 1; y -= 1
			return ans
		elif dir == "SW":
			while x < edgeX and y > edgeY:
				if gameOfLife[x][y] == "#" and x != seatX: return 1
				if gameOfLife[x][y] == "L" and x != seatX: return 0
				x += 1; y -= 1
			return ans
		elif dir == "SE":
			while x < edgeX and y < edgeY:
				if gameOfLife[x][y] == "#" and x != seatX: return 1
				if gameOfLife[x][y] == "L" and x != seatX: return 0
				x += 1; y += 1
			return ans
		elif dir == "NE":
			while x > edgeX and y < edgeY:
				if gameOfLife[x][y] == "#" and x != seatX: return 1
				if gameOfLife[x][y] == "L" and x != seatX: return 0
				x -= 1; y += 1
			return ans
	else: return 0
	return 0
def iterate():
	numRows = len(gameOfLife)-1; numCols = len(gameOfLife[0])
	nextStep = [[]]
	change = 0
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
			if gameOfLife[i][j] != ".":
				neighbours += checkSeat(i, j, "N")
				neighbours += checkSeat(i, j, "NW") #NW
				neighbours += checkSeat(i, j, "W") #W
				neighbours += checkSeat(i, j, "SW") #SW
				neighbours += checkSeat(i, j, "S") #S
				neighbours += checkSeat(i, j, "SE") #SE
				neighbours += checkSeat(i, j, "E") #E
				neighbours += checkSeat(i, j, "NE") #NE
				
				if neighbours == 0 and gameOfLife[i][j] == "L": nextStep[i][j] = "#"; change += 1
				if neighbours >= 5 and gameOfLife[i][j] == "#": nextStep[i][j] = "L"; change += 1
	numSeats = 0
	for row in range (numRows):
		for col in range(numCols):
			gameOfLife[row][col] = nextStep[row][col]
			if gameOfLife[row][col] == "#": numSeats +=1
	print (numSeats)
	return change
createSeats()	
change = iterate()
numIterations = 1
while change > 0:
	change = iterate()
	numIterations += 1
	print (numIterations, '%')
	