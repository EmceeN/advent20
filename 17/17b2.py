#17 - The Meaning of Liff 3D
input = open('input.txt', 'r')
inputs = input.readlines()
gameOfLife = {}
x=y=0
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
	print (gameOfLife)

def iterate():
	nextStep = {}
	changes = 0
	minW = min(gameOfLife.keys()); maxW = max(gameOfLife.keys())
	minZ = min(gameOfLife[0].keys()); maxZ = max(gameOfLife.keys())
	minX = min(gameOfLife[0][0].keys()); maxX = max(gameOfLife[0][0].keys())
	minY = min(gameOfLife[0][0][0].keys()); maxY = max(gameOfLife[0][0][0].keys())
	print ("Iteration", maxW+1, "of 6")
	for h in range(minW-1,maxW+2):
		nextStep[h]={}
		for k in range(minZ-1,maxZ+2):
			nextStep[h][k]={}
			for i in range(minX-1,maxX+2):
				nextStep[h][k][i] ={}
				for j in range(minY-1,maxY+2):
					try: nextStep[h][k][i][j] = gameOfLife[h][k][i][j]
					except: nextStep[h][k][i][j] = "."
					#print("Checking cell:",h,k,i,j)
					neighbours = 0
					for w in range (h-1,h+2):
						for z in range (k-1,k+2):
							for x in range(i-1,i+2):				
								for y in range (j-1,j+2):
									if not (w == h and x == i and y == j and z == k):
										
										cell = "."
										cube = gameOfLife.get(w)
										if cube: 
											slice = gameOfLife[w].get(z)
											if slice:
												row = gameOfLife[w][z].get(x)
												if row: cell = gameOfLife[w][z][x].get(y, ".")
											if cell == "#": neighbours += 1 
					
					cell = "."
					cube = gameOfLife.get(h)
					if cube:
						slice = gameOfLife[h].get(k)
						if slice:
							row = gameOfLife[h][k].get(i)
							if row: cell = gameOfLife[h][k][i].get(j, ".")
					#print (h,k,i,j,":",cell, neighbours)
					if neighbours == 3 and cell == ".": nextStep[h][k][i][j] = "#"; changes += 1
					elif (neighbours < 2 or neighbours > 3) and cell == "#": nextStep[h][k][i][j] = "."; changes += 1
	#print (len(nextStep)-1,len(nextStep[0]))
	
	numSeats = 0
	for w in range (minW-1,maxW+2):
		if not gameOfLife.get(w): gameOfLife[w] = {}
		#print ("w=",w)
		for z in range (minZ-1,maxZ+2):
			if not gameOfLife[w].get(z): gameOfLife[w][z] = {}
			#print (" z=",z)
			for x in range(minX-1,maxX+2):
				if not gameOfLife[w][z].get(x): gameOfLife[w][z][x] = {}
				#print("  x=",x,end=" ")
				for y in range (minY-1,maxY+2):
					gameOfLife[w][z][x][y] = nextStep[w][z][x][y]
					#print(gameOfLife[w][z][x][y], end = "")
					if gameOfLife[w][z][x][y] == "#": numSeats +=1
	print(numSeats)

createSeats()	
for iteration in range(0,6):
	iterate()

