#17 - The Meaning of Liff 3D
input = open('input.txt', 'r')
inputs = input.readlines()
gameOfLife = {}
x=y=0
def createSeats():
	x = 0
	gameOfLife[0] = {}
	for line in inputs:
		line = line.strip()
		print(line)
		gameOfLife[0][x]={}
		y = 0
		for character in line:
			gameOfLife[0][x][y] = character
			y+=1
		x +=1
	print (gameOfLife)
	
def checkCell(z,x,y):
	cell = "."
	slice = gameOfLife.get(z)
	if slice:
		row = gameOfLife[z].get(x)
		if row: cell = gameOfLife[z][x].get(y, ".")
	return cell

def iterate():
	nextStep = {}
	changes = 0
	minZ = min(gameOfLife.keys()); maxZ = max(gameOfLife.keys())
	minX = min(gameOfLife[0].keys()); maxX = max(gameOfLife[0].keys())
	minY = min(gameOfLife[0][0].keys()); maxY = max(gameOfLife[0][0].keys())
	#print (minZ, maxZ, minX, maxX, minY, maxY)
	for k in range(minZ-1,maxZ+2):
		nextStep[k]={}
		
		for i in range(minX-1,maxX+2):
			nextStep[k][i] ={}
			for j in range(minY-1,maxY+2):
				try: nextStep[k][i][j] = gameOfLife[k][i][j]
				except: nextStep[k][i][j] = "."
				#print("Checking cell:",k,i,j)
				neighbours = 0
				for z in range (k-1,k+2):
					for x in range(i-1,i+2):				
						for y in range (j-1,j+2):
							if not (x == i and y == j and z == k):
								cell = checkCell(z,x,y)
								if cell == "#": neighbours += 1 ;#print (z,x,y,"is a neighbour")
				cell = checkCell(k,i,j)
				if neighbours == 3 and cell == ".": nextStep[k][i][j] = "#"; changes += 1; #print("making active")
				elif (neighbours < 2 or neighbours > 3) and cell == "#": nextStep[k][i][j] = "."; changes += 1;  #print("making inactive"); 
	numSeats = 0
	for z in range (minZ-1,maxZ+2):
		if not gameOfLife.get(z): gameOfLife[z] = {}
		#print ("z=",z)
		for x in range(minX-1,maxX+2):
			if not gameOfLife[z].get(x): gameOfLife[z][x] = {}
			#print("x=",x,end=" ")
			for y in range (minY-1,maxY+2):
				gameOfLife[z][x][y] = nextStep[z][x][y]
				#print(gameOfLife[z][x][y], end = "")
				if gameOfLife[z][x][y] == "#": numSeats +=1
			#print("")
		#print("")
	return numSeats
createSeats()	
for iteration in range(6):
	print ("Iteration", iteration+1, "of 6")
	answer = iterate()
print (answer, "cubes active in the pocket dimension")