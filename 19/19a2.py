#18 - The Meaning of Liff 3D
import re
with open('input.txt', 'r') as input:
	inputs = input.readlines()

rules = {}
def matchLines(tLine):
	tLine = tLine.strip()
	print ("Line is", len(tLine), "characters long")
	
	ans = re.search(checkRule,tLine)	
	print (tLine,end = " ")
	if ans:
		print ("found from",ans.start(),"to",ans.end(),"...")
		if ans.start() == 0 and ans.end() == len(tLine):
			print ("which makes it a match!")
			return 1
		else:
			print ("but there's other data, so it's not a match!")
			return 0
	else:
		print ("not found!")
		return 0
		
	
	
matches = 0
for line in inputs:
	if line[0].isdigit():
		line = line.strip()
		ruleSet = line.split(": ")
		rules[ruleSet[0]] = ruleSet[1]
		if rules[ruleSet[0]].find("|") > -1: print ("OR found"); rules[ruleSet[0]]="( "+rules[ruleSet[0]]+" )"
	elif line == "\n":
		print ("Beginning substitution...")
		tokens = rules["0"].split(" ")
		print (tokens, type(tokens))
		k = 0
		while any(item.isdigit() for item in tokens):
			for token in tokens:
				if token.isdigit():
					tIndex = tokens.index(token)
					print ("token", token, tIndex)
					newTokens = rules[token].split(" ")
					tokens.pop(tIndex)
					print (tokens, type(tokens))
					for newToken in range(len(newTokens)): tokens.insert(tIndex+newToken, newTokens[newToken]); print(tokens,type(tokens))
					
			
			if k >10000: print ("Breaking at 10k..."); break
			k+=1
			
		
	
		checkRule = ""
		for token in tokens:
			if token.find('"') >= 0:
				token = token.replace('"','')
			checkRule += token
	
		
		print (checkRule)
	elif line[0] in 'ab':
		matches += matchLines(line)

print (matches," matches found!")