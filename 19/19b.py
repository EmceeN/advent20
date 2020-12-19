#19 - the Rabbit of Caerbannog
import re
with open('inputb.txt', 'r') as input:
	inputs = input.readlines()

rules = {}

def matchLines(tLine):
	tLine = tLine.strip()
	ans = re.search(checkRule,tLine)	
	if ans:
		if ans.start() == 0 and ans.end() == len(tLine): return 1
		else: return 0
	else: return 0
	
matches = 0
for line in inputs:
	if line[0].isdigit():
		line = line.strip()
		ruleSet = line.split(": ")
		rules[ruleSet[0]] = ruleSet[1]
		if rules[ruleSet[0]].find("|") > -1: rules[ruleSet[0]]="( "+rules[ruleSet[0]]+" )"
	elif line == "\n":
		print ("Beginning substitution...")
		tokens, k, recur8, recur11 = rules["0"].split(" "), 0, 0, 0
		stop8, stop11 = False, False
		while any(item.isdigit() for item in tokens):
			for token in tokens:
				if token.isdigit():
					if int(token) == 8:
						recur8 += 1; print ("Recursion #",recur8,"for 8")
						if recur8 >= 8: print ("Ending recursion on 8 after 8"); stop8 = True
					if int(token) == 11:
						recur11 += 1; print ("Recursion #",recur11,"for 11")
						if recur11 >= 11: print ("Ending recursion on 11 after 11"); stop11 = True
					tIndex = tokens.index(token)
					if not stop8 and not stop11:
						newTokens = rules[token].split(" ")
						tokens.pop(tIndex)
						for newToken in range(len(newTokens)): tokens.insert(tIndex+newToken, newTokens[newToken]);
					elif stop8: tokens.pop(tIndex);	stop8 =False
					elif stop11: tokens.pop(tIndex); stop11 =False
			if k >10000: print ("Breaking at 10k..."); break
			k+=1
		checkRule = ""
		for token in tokens:
			if token.find('"') >= 0: token = token.replace('"','')
			checkRule += token
		print ("Matching against:", checkRule)
	elif line[0] in 'ab': matches += matchLines(line)
print (matches,"matches found!")