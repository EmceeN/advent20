#08 - Inspector So-and-so of the Yard
# Runs through a basic assembly-type program
# to find and fix an infinite loop

#Init: file opening and declarations
input = open('input.txt', 'r')
inputs = input.readlines()
jmpList = []
instruction = []

#Runs the assembly program
def runProgram(isFirstRun):
	#Declarations
	opcode = ""
	innerOpCode = "" 			#the opCode being investigated inside the loop
	arg = 0
	accumulator = 0
	instruction = {} 			#a dictionary
	visited = []
	i = 0
	isFinished = 0
	
	#Parse the input file into a dict
	for line in inputs:
		instruction[i] = {}
		lineSplit = line.split(" ") 			#lines are of format e.g. nop 0, so split on " "
		opcode = str(lineSplit[0]) #nop
		arg = int(lineSplit[1]) #0
		#in dictionary "instruction", entry number "i", assign the key "opcode" the value of "arg"
		instruction[i][opcode] = arg 
		i+=1 									#iterate
		if isFirstRun == 1 and opcode == 'jmp': #on the first pass through, suck up all jmp codes
			jmpList.append(i-1)

	op = 0 
	while op not in visited:				#loop until we hit a visited instruction
		print (op, ":", innerOpCode, arg)	
		if op >= len(instruction):			#did we reach the end?
			print("You're nicked, chum!")
			isFinished = 1					#mark as completed 
			break
		else:
			for innerOpCode in instruction[op]:		#loop through each operation
				visited.append(op)					#mark that we've been here
				arg = instruction[op][innerOpCode]	
			
				if innerOpCode == 'acc':			#AC-CU-MU-LATE
					accumulator += arg
					op += 1
				if innerOpCode == 'jmp':			#Go ahead, jump!
					op += arg					
				if innerOpCode == 'nop':			#Noping out
					op += 1
		
	print ("Inspector So-and-so of the Yard accumulated", accumulator, "silliness") #The result
	return isFinished								#did we win?

#Procedure detailed, now let's do that first run and build the jmp list	
finishedProgram = runProgram(1)						

j=0
while finishedProgram == 0:				#loop through the jump list to try to find the faulty line
	nextTry = jmpList[j]
	print(jmpList[j], "::", inputs[nextTry])		
	inputs[nextTry] = inputs[nextTry].replace("jmp","nop")	#making our replacement
	finishedProgram = runProgram(0)							#try the program again
	inputs[nextTry] = inputs[nextTry].replace("nop","jmp")	#put the list back the way it was
	j += 1																