#17 - The Meaning of Liff 3D
from datetime import datetime
with open('input.txt', 'r') as input:
	inputs = input.readlines()
gameOfLife = {}
start = datetime.now()
print (start)
def createSeats():
	x = 0
	gameOfLife[0] = {}
	gameOfLife[0][0] = {}
	for line in inputs:
		line = line.strip()
		print(line)
		gameOfLife[0][0][x]={}
		y = 0
		for character in line:
			gameOfLife[0][0][x][y] = character
			y+=1
		x +=1
		
def checkCell(w,z,x,y):
	cell = "."
	cube = gameOfLife.get(w)
	if cube: 
		slice = gameOfLife[w].get(z)
		if slice:
			row = gameOfLife[w][z].get(x)
			if row: cell = gameOfLife[w][z][x].get(y, ".")
	return cell
	
def iterate():
	nextStep = {}
	minW = min(gameOfLife.keys()); maxW = max(gameOfLife.keys())
	minZ = min(gameOfLife[0].keys()); maxZ = max(gameOfLife[0].keys())
	minX = min(gameOfLife[0][0].keys()); maxX = max(gameOfLife[0][0].keys())
	minY = min(gameOfLife[0][0][0].keys()); maxY = max(gameOfLife[0][0][0].keys())
	for h in range(minW-1,maxW+2):
		nextStep[h]={}
		for k in range(minZ-1,maxZ+2):
			nextStep[h][k]={}
			for i in range(minX-1,maxX+2):
				nextStep[h][k][i] ={}
				for j in range(minY-1,maxY+2):
					try: nextStep[h][k][i][j] = gameOfLife[h][k][i][j]
					except: nextStep[h][k][i][j] = "."
					neighbours = 0
					for w in range (h-1,h+2):
						for z in range (k-1,k+2):
							for x in range(i-1,i+2):				
								for y in range (j-1,j+2):
									if not (w == h and x == i and y == j and z == k):
										cell = checkCell(w,z,x,y)
										if cell == "#": neighbours += 1 
					cell = checkCell(h,k,i,j)
					if neighbours == 3 and cell == ".": nextStep[h][k][i][j] = "#"
					elif (neighbours < 2 or neighbours > 3) and cell == "#": nextStep[h][k][i][j] = "."	
	numSeats = 0
	for w in range (minW-1,maxW+2):
		if not gameOfLife.get(w): gameOfLife[w] = {}
		for z in range (minZ-1,maxZ+2):
			if not gameOfLife[w].get(z): gameOfLife[w][z] = {}
			for x in range(minX-1,maxX+2):
				if not gameOfLife[w][z].get(x): gameOfLife[w][z][x] = {}
				for y in range (minY-1,maxY+2):
					gameOfLife[w][z][x][y] = nextStep[w][z][x][y]
					if gameOfLife[w][z][x][y] == "#": numSeats +=1
	return numSeats

createSeats()	
for iteration in range(6):
	print ("Iteration", iteration+1, "of 6")
	answer = iterate()
print (answer, "cubes active in the pocket dimension")
time = datetime.now()-start
print (time)
