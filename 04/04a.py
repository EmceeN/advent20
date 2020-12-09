#04 - The Cross-Channel Jump
input = open('input.txt', 'r')
inputs = input.readlines()
passport = ''
failPass = 0
passPass = 0
for line in inputs:
	if line != '\n':
		final = line.strip()
		final = final + " "
		passport = passport + final
	else:
		checkFields=[]
		ppFields = passport.split(" ")
		for field in ppFields:
			checkField = field[:3]
			print (checkField, end = ",")
			checkFields.append(checkField)
		if 'byr' in checkFields and 'iyr' in checkFields and 'eyr' in checkFields and 'hgt' in checkFields and 'hcl' in checkFields and 'ecl' in checkFields and 'pid' in checkFields:
			print("Proceed, citizen. Glory to Arstotzka!")
			passPass = passPass +1
		else:
			print("Halt. Glory to Arstotzka.")
			failPass = failPass +1
		    
		passport = ''
print ("We processed",passPass,"correct passports and",failPass,"incorrect passports. Glory to Arstotzka.")