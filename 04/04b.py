#04 - The Cross-Channel Jump
input = open('input.txt', 'r')
inputs = input.readlines()
passport = ''
failPass = 0
passPass = 0
for line in inputs:
	isFailed = 0
	if line != '\n':
		final = line.strip()
		final = final + " "
		passport = passport + final
	else:
		checkFields=[]
		birthYear = 0
		issueYear = 0
		expYear = 0
		ppFields = passport.split(" ")
		for field in ppFields:
			fieldVal = field.split(":")
			checkField = fieldVal[0]
			#print (checkField, end = ",")
			checkFields.append(checkField)
			if checkField == 'byr':
				birthYear = int(fieldVal[1])
			elif checkField == 'iyr':
				issueYear = int(fieldVal[1])
			elif checkField == 'eyr':
				expYear = int(fieldVal[1])
			elif checkField == 'hgt':
				height = fieldVal[1]
			elif checkField == 'hcl':
				hairColour = fieldVal[1]
			elif checkField == 'ecl':
				eyeColour = fieldVal[1]
			elif checkField == 'pid':
				passportId = fieldVal[1]
		if 'byr' in checkFields and 'iyr' in checkFields and 'eyr' in checkFields and 'hgt' in checkFields and 'hcl' in checkFields and 'ecl' in checkFields and 'pid' in checkFields:
			if birthYear < 1920 or birthYear > 2002:
				isFailed = 1
				#print("Your birth year is incorrect.", birthYear)
			if issueYear < 2010 or issueYear > 2020:
				isFailed = 1
				#print("Your passport issue year is incorrect.", issueYear)
			if expYear < 2020 or expYear > 2030:
				isFailed = 1
				#print("Your passport expiration year is incorrect.", expYear)
			if height.find("cm") > 0:
				height2 = height[:len(height)-2]
				if int(height2) < 150 or int(height2) > 193:
					isFailed = 1
					#print("Your height in centimetres is incorrect.", height)
			elif height.find("in") > 0:
				if int(height[:2]) < 59 or int(height[:2]) > 76:
					isFailed = 1
					#print("Your height in inches is incorrect.", height)	
			else:
				isFailed = 1
				#print("Your height is incorrect.", height)
			if len(hairColour) != 7 or hairColour[:1] != "#":
				isFailed = 1
				#print("Your hair colour is incorrect.", hairColour)
			else:
				hc2 = hairColour[2:7]
				hex_digits = set("0123456789ABCDEFabcdef")
				if not all(c in hex_digits for c in hc2):
					isFailed = 1
					#print("Your hair colour is incorrect.", hairColour)
			if not eyeColour in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
				isFailed = 1
				#print("Your eye colour is incorrect.", eyeColour)
			if len(passportId) != 9 or not passportId.isdigit():
				isFailed = 1
				#print("Your passport ID is incorrect.", passportId)
		else:
			isFailed = 1
		
		if isFailed == 1:	
			#print("Halt. Glory to Arstotzka.")
			failPass = failPass +1
		else:
			print(birthYear, issueYear, expYear, height, hairColour, eyeColour, passportId)
			#print("Proceed, citizen. Glory to Arstotzka.")
			passPass = passPass+1
			
		passport = ''
print ("We processed",passPass,"correct passports and",failPass,"incorrect passports. Glory to Arstotzka.")