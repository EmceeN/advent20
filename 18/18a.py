#18 - The Meaning of Liff 3D
with open('input.txt', 'r') as input:
	inputs = input.readlines()
answer = 0

def evaluate(line):
	pieces, chara = [], 0
	numPieces = len(line)
	while chara < numPieces:
		if line[chara].isdigit() or (line[chara] == ")" and pieces[-2] == "(") :
			if line[chara].isdigit(): n = int(line[chara])
			while pieces:
				if pieces[-1] == '(': break
				if pieces[-1] == '+': n += pieces[-2]
				elif pieces[-1] == '*': n *= pieces[-2]
				pieces = pieces[:-2]
			pieces.append(n)
		elif line[chara] != " " and line[chara] != ")":pieces.append(line[chara])
		
		
		chara+=1
		
	return n
	
for line in inputs:
	line=line.strip()
	ans = evaluate(line)
	print (line,"=", ans )
	answer +=ans

print (answer)
	