#08 - Inspector So-and-so of the Yard
# Runs through a basic assembly-type program
# to find and fix an infinite loop

input = open('input.txt', 'r')
inputs = input.readlines()
jmpList = []

def runProgram(isFirstRun):
	opcode = ""
	innerOpCode = "" 			
	arg = 0
	accumulator = 0
	instruction = {} 			
	visited = []
	i = 0
	isFinished = 0
	
	for line in inputs:
		instruction[i] = {}
		lineSplit = line.split(" ") 			
		opcode = str(lineSplit[0]) 
		arg = int(lineSplit[1]) 
		instruction[i][opcode] = arg 
		i+=1 
		if isFirstRun == 1 and opcode == 'jmp': 
			jmpList.append(i-1)

	op = 0 
	while op not in visited:				
		print (op, ":", innerOpCode, arg)	
		
		if op >= len(instruction):			
			print("You're nicked, chum!")
			isFinished = 1					 
			break
		else:
			for innerOpCode in instruction[op]:		
				visited.append(op)					
				arg = instruction[op][innerOpCode]	
			
				if innerOpCode == 'acc':			
					accumulator += arg
					op += 1
				if innerOpCode == 'jmp':			
					op += arg					
				if innerOpCode == 'nop':			
					op += 1
		
	print ("Inspector So-and-so of the Yard accumulated", accumulator, "silliness") 
	return isFinished								

finishedProgram = runProgram(1)						

j=0
while finishedProgram == 0:				
	nextTry = jmpList[j]
	print(jmpList[j], "::", inputs[nextTry])		
	inputs[nextTry] = inputs[nextTry].replace("jmp","nop")	
	finishedProgram = runProgram(0)							
	inputs[nextTry] = inputs[nextTry].replace("nop","jmp")	
	j += 1																