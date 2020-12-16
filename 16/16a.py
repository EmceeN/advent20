#16 - Dirty Hungaian Phrasebook
with open('input3.txt', 'r') as input:
	inputs = input.readlines()
	print (inputs)
fields, cf = {}, {}
fRow = inputs.index('\n')
nRow = inputs.index('nearby tickets:\n')
rows,errorRate=0,0
for line in (inputs):
	line = line.strip()
	if rows < fRow:
		field = line.split(":")
		fieldName = field[0]
		fields[fieldName] = {}
		ranges = field[1].split(" or ")
		i = 0
		mins, maxes = [], []
		for r in ranges:
			min, max = int(r.split("-")[0]),int(r.split("-")[1])
			mins.append(min); maxes.append(max)
			i+=1
		fields[fieldName]['min'] = mins; fields[fieldName]['max'] = maxes
	elif rows > nRow:
		ticket = line.split(",")
		
		for fieldNumber in ticket:
			isValid = 0
			check = int(fieldNumber)
			print (isValid)
			for key in fields.keys():
				cf = fields[key]
				print ("Checking",check,"against",cf['min'][0],"-",cf['max'][0], "and ",cf['min'][1],"-",cf['max'][1])		
				if (check >= cf['min'][0] and check <= cf['max'][0]) or (check >= cf['min'][1] and check <= cf['max'][1]):
					print ("Match!")
					isValid = 1
			print (isValid)
			if isValid == 0: print ("is invalid!"); errorRate += check	
	rows+=1
#print (fields)
print (errorRate)
print (fields)
		