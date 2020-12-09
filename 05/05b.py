#05 - Flying Cir-cuss
input = open('input.txt', 'r')
inputList = input.readlines()
maxbin = 0
def binInt2dec(binParam):
	binplace= 1
	binStr = str(binParam)

	digits = []
	
	decval = 0
	for digit in binStr:
		digits.append(digit)
	for digit2 in reversed(digits):
		decval = decval + int(digit2) * binplace
		binplace = binplace * 2
	return decval

filledSeats = []
for entry in inputList:
	binEntry = entry.replace("F","0")
	binEntry = binEntry.replace("B","1")
	binEntry = binEntry.replace("L","0")
	binEntry = binEntry.replace("R","1")
	binEntry2 = int(binEntry)
	#print (binEntry2)
	if binEntry2 > maxbin:
		maxbin = binEntry2
		print ("New maximum:", maxbin)
	decSeat = binInt2dec(binEntry2)
	filledSeats.append(decSeat)

decval2 = binInt2dec(maxbin)
print ("Max seat ID is:", decval2)
print ("Empty seats:")
for i in range(decval2):
	if i not in filledSeats:
		print(i)
		

	
	