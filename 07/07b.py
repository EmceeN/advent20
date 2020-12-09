#07 - Gumby Flower Arranging
import re
input = open('input.txt', 'r')
inputs = input.readlines()
bags = {}
for line in inputs:
	bagSplitter = re.split(' bags contain| bag[s]?.| bag[s]?,',line)
	bagType = bagSplitter[0]
	n = len(bagSplitter)
	bags[bagType] = {}
	for i in range (1, n-1):
		#print(bagSplitter[i])
		if bagSplitter[1].find("no other") == -1: 
			innerBag = re.search('[a-z]+ [a-z]+', bagSplitter[i])
			innerBagQty = re.search('[0-9]+', bagSplitter[i])
			#print (innerBag.group(),": ",innerBagQty.group())
			bags[bagType][innerBag.group()] = int(innerBagQty.group())

def getBags(bagType, parentBags): 
	numBags = 0	
	for bag in bags[bagType].keys(): 
		newBags = bags[bagType][bag]
		multiBags = newBags*parentBags
		numBags += getBags(bag, multiBags) 
	numBags += parentBags
	return numBags
	
bagType = 'shiny gold'
numBags, multiBags = 0, 0
for bag in bags[bagType].keys():		
	newBags = bags[bagType][bag]
	numBags = numBags + getBags(bag, newBags)
print (numBags, "BAGS! GET IN!!")