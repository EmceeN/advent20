#07 - Gumby Flower Arranging
input = open('input.txt', 'r')
inputs = input.readlines()
list1 = ['shiny gold']
bagTypes = 0
for i in range(50):
	lastBagTypes = bagTypes
	for line in inputs:
		bag = line.split(' bags ')
		for containedBag in list1:
			bagFoundAt = bag[1].find(containedBag)
			if bagFoundAt > 0:
				print (bag[1], "found at position", bagFoundAt)
				if bag[0] not in list1:
					list1.append(bag[0])
					print (bag[0], "bag can contain", containedBag, "bag")
					bagTypes = bagTypes +1
					
	if lastBagTypes == bagTypes:
		print ("Breaking after", i, "loops")
		break
print (bagTypes, "bags can contain a shiny gold bag")
		