#12 - The Crimson Permanent Assurance (reprise)
with open('input.txt', 'r') as input:
	inputs = input.readlines()

position=[0,0]
xDir, yDir, xTemp, yTemp, facing, turns  = 1, 0, 0, 0, 0, 0
fourCardinals = ["E","S","W","N"]
def GetTemps(dir):
	if dir == "E": xTemp = 1; yTemp = 0
	if dir == "S": xTemp = 0; yTemp = -1
	if dir == "W": xTemp = -1; yTemp = 0
	if dir == "N": xTemp = 0; yTemp = 1
	return xTemp, yTemp

def Move(x,y,a):
	position[0] += x*a; position[1] += y*a

		
	return xTemp,yTemp
for instruction in inputs:
	dir = instruction[0]
	amount = int(instruction[1:])
	print (dir, amount,",facing ", fourCardinals[facing])
	if dir in fourCardinals: xDir, yDir = GetTemps(dir); Move(xDir,yDir, amount)
	elif dir == "F": xDir, yDir = GetTemps(fourCardinals[facing]); Move(xDir,yDir, amount)
	elif dir == "L": turns = int(amount / 90);facing = (facing - turns + 4) % 4; 
	elif dir == "R": turns = int(amount / 90); facing = (facing + turns) % 4;
			
print ("Final Position is", position[0],position[1],": Manhattan number is",abs(position[0])+abs(position[1]))

	
	