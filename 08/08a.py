#08 - Inspector So-and-so of the Yard

input = open('input2.txt', 'r')
inputs = input.readlines()
opcode = ""
innerOpCode = ""
arg = 0
accumulator = 0
instruction = {}
visited = []
i = 0
for line in inputs:
	instruction[i] = {}
	lineSplit = line.split(" ")
	opcode = str(lineSplit[0])
	arg = int(lineSplit[1])
	instruction[i][opcode] = arg
	i+=1

op = 0
while op not in visited:
	for innerOpCode in instruction[op]:
		
		visited.append(op)
		arg = instruction[op][innerOpCode]
		print (op, ":", innerOpCode, arg)
		if innerOpCode == 'acc':
			accumulator += arg
			op += 1
		if innerOpCode == 'jmp':
			op += arg
		if innerOpCode == 'nop':
			op += 1
		
print (len(instruction))
print ("Inspector So-and-so of the Yard accumulated", accumulator, "silliness")