#18 - The Meaning of Liff 3D
with open('input.txt', 'r') as input:
	inputs = input.readlines()
answer = 0

def operate(pieces, n, cb):
	if cb == 1:
		print (pieces)
		a=-1
		print (len(pieces))
		for i in range(len(pieces)):
			print ("%%",i)
			if pieces[i] == "(": a = i; print (a,i,pieces[i],"^^^^")
			print ("**",a)
		if a >= 0: nextStep = pieces[a+1:];pieces = pieces[:a]
		else: nextStep = pieces; pieces = []
		print (nextStep, pieces)
		for piece in nextStep:
			if piece != "*": n *= int(piece)
	while pieces:
		if pieces[-1] == '(' or pieces[-1] == "*": break
		#print (pieces[-2],pieces[-1],n, "*")
		if pieces[-1] == '+': print ("+"); n += int(pieces[-2])
		
		pieces = pieces[:-2]
		
	pieces.append(n)
	return pieces

def evaluate(line):
	pieces, chara = [], 0
	numPieces = len(line)
	while chara < numPieces:
		print(line[chara],"checking")
		if line[chara].isdigit() : pieces = operate(pieces,int(line[chara]),0)
		elif line[chara] == ")":
			n = pieces[-1]
			pieces = pieces[:-1]
			pieces = operate(pieces,n,1)
		elif line[chara] != " ": pieces.append(line[chara])
		
		print (":",pieces,":")
		chara+=1
	if len(pieces) > 1:
		pieces = operate(pieces[:-1], int(pieces[-1]), 1)

	return int(pieces[0])
	
for line in inputs:
	line=line.strip()
	ans = evaluate(line)
	print (line,"=", ans )
	answer +=ans

print (answer)
	