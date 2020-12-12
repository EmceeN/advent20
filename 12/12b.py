#12 - The Crimson Permanent Assurance (reprise)
with open('input.txt', 'r') as input:
	inputs = input.readlines()

position=[0,0]
waypoint = [10,1]
xDir, yDir, xTemp, yTemp, facing, turns  = 1, 0, 0, 0, 0 ,0
fourCardinals = ["E","S","W","N"]
def GetTemps(dir):
	if dir == "E": xTemp = 1; yTemp = 0
	elif dir == "S": xTemp = 0; yTemp = -1
	elif dir == "W": xTemp = -1; yTemp = 0
	elif dir == "N": xTemp = 0; yTemp = 1
	return xTemp, yTemp

def Move(x,y,a,d):
	if d == "F":
		position[0] += waypoint[0]*a; position[1] += waypoint[1]*a
		print ("Moving ship by ", waypoint[0]*a, waypoint[1]*a)
	else: 
		waypoint[0] += x*a; waypoint[1] += y*a
		print ("Moving waypoint by ", x*a, y*a)

def TurnWaypoint(t):
	x1, y1 = waypoint[0], waypoint[1]
	if t < 0: t += 4
	if t % 2 == 1: waypoint[0] = y1; waypoint[1] = x1*-1
	if t >= 2: waypoint[0] *= -1; waypoint[1] *= -1
	print ("making ", t, "turns")
		
for instruction in inputs:
	dir = instruction[0]
	amount = int(instruction[1:])
	xDir, yDir = 0,0
	print (dir, amount)
	if dir in fourCardinals: xDir, yDir = GetTemps(dir); Move(xDir,yDir, amount, dir)
	elif dir == "F": Move(xDir,yDir, amount, dir)
	elif dir == "L": turns = int(amount / 90) * -1; TurnWaypoint(turns) 
	elif dir == "R": turns = int(amount / 90); facing = (facing + turns) % 4; TurnWaypoint(turns)		
	print (position[0],position[1],": waypoint in",waypoint[0],waypoint[1])
print ("Final Position is", position[0],position[1],": Manhattan number is",abs(position[0])+abs(position[1]))

	
	