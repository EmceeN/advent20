#14
with open('input.txt', 'r') as input:
	inputs = input.readlines()
mask = 0
bitValues = {}
mem = {}

def ChangeBit (val, pos, bin):
	#print ("Changing value",val, "bit", pos, "to", bin)
	mask = 1 << pos; #print ("Setting",mask,"bit to 0")	# set the bit to change: at position
	val = val & ~mask;  # change it to a 0 (with ~)
	mask = (bin << pos) & mask #put the right bit in the right position, and add it to the mask 
	val |= mask; #print("Value becomes",val)
	return val


for line in inputs:
	if line[:4] == "mask":
		bitValues = {}
		mask = line.split(" = ")[1].strip()
		a=len(mask)
		for value in mask:
			if value != 'X':
				bitValues[str(a-1)]=value
			a-=1
		print (mask)
	else:
		inst = line.split(" = ")
		memPtr = int(inst[0].split("[")[1][:-1])
		writeVal = wroteVal = int(inst[1])
		for bit in bitValues.keys():
			writeVal = ChangeBit(writeVal, int(bit), int(bitValues[bit]))
		mem[str(memPtr)] = writeVal
		print (memPtr, wroteVal, writeVal)
		
memValues = 0
i = 0
for value in mem:
	memValues += int(mem[value])
	#print (value, mem[value])
	i += 1
print (memValues)