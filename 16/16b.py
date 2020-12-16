#16 - Dirty Hungaian Phrasebook
with open('input.txt', 'r') as input:
	inputs = input.readlines()
fields, cf, valids = {}, {}, [[]]
fRow = inputs.index('\n')
nRow = inputs.index('nearby tickets:\n')
yRow = inputs.index('your ticket:\n')
rows,errorRate=0,0
numValids = 0
myTicket = []
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
	elif rows == yRow + 1:
		myTicket = line.split(",")
	elif rows > nRow:
		ticket = line.split(",")
		for fieldNumber in ticket:
			isValid = 0
			check = int(fieldNumber)
			for key in fields.keys():
				cf = fields[key]
				if (cf['min'][0] <= check <= cf['max'][0]) or (cf['min'][1] <= check <= cf['max'][1]):
					isValid = 1
			if isValid == 0: errorRate += check; break
		if isValid == 1:
			valids.append([])
			for f in range(len(fields)):
				valids[numValids].append(ticket[f])
			numValids += 1

	rows+=1
valids.pop()
print ("Error rate is:",errorRate)
allocated= []
while len(allocated) < len(ticket):
	for key in fields.keys():
		cf = fields[key]
		#print ("Checking field",key,"against",cf['min'][0],"-",cf['max'][0], "and ",cf['min'][1],"-",cf['max'][1])
		i = 0
		alloc = -1
		numPoss = 0
		for j in range(len(ticket)):
			if j not in allocated:
				#print ("Checking column", j)
				for vticket in valids:
					vcheck = int(vticket[i])
					couldBe = 1
					if not((cf['min'][0] <= vcheck <= cf['max'][0]) or (cf['min'][1] <= vcheck <= cf['max'][1])):
						couldBe = 0; break
				if couldBe == 1: alloc = j; numPoss += 1
		
			i+=1
		if numPoss == 1: fields[key]['column']= alloc; print ("Column", alloc, "is",key); allocated.append(alloc);
product = 1
for key in fields.keys():
	print (key, "(column", fields[key]['column'],"):",myTicket[fields[key]['column']])
	if key.find("departure") != -1:
		
		product *= int(myTicket[fields[key]['column']])
print ("Final hacked ticket code:",product)