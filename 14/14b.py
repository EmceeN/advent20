#14
with open('input.txt', 'r') as input:
	inputs = input.readlines()
mask = 0
bitValues = {}
mem = {}
val = 0
check = 0
def ChangeBit (val, pos, bin):
	mask = 1 << pos; 	# set the bit to change: at position
	val = val & ~mask;  # change it to a 0 (with ~)
	mask = (bin << pos) & mask #put the right bit in the right position, and add it to the mask 
	val |= mask; 
	return val
def ChangeArray(i,val):
	if i < len(changeArray): 
		val0 = ChangeBit(val,changeArray[i],0)
		val1 = ChangeBit(val,changeArray[i],1)
		if i == len(changeArray)-1: memChanges.append(val0); memChanges.append(val1)
		ChangeArray(i+1,val0)
		ChangeArray(i+1,val1)
	else: return
	i+=1
for line in inputs:
	if line[:4] == "mask":
		bitValues = {}
		mask = line.split(" = ")[1].strip()
		a=len(mask)
		for value in mask:
			bitValues[str(a-1)]=value
			a-=1
	else:
		changeArray,memChanges=[],[]
		inst = line.split(" = ")
		memPtr = int(inst[0].split("[")[1][:-1])
		writeVal = int(inst[1])
		for bit in bitValues.keys():
			if bitValues[bit] == "X": changeArray.append(int(bit))
			elif bitValues[bit] == "1": memPtr = ChangeBit(memPtr,int(bit),1)
		i=0
		memValues,changeMem = 1, []
		ChangeArray(i,memPtr)	
		for addr in memChanges: mem[str(addr)] = writeVal
memValues = 0
for value in mem: memValues += int(mem[value])
print("Docking code is", memValues)