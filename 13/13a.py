#13
with open('input.txt', 'r') as input:
	inputs = input.readlines()
nextBus = 0
print (inputs)
myTime = int(inputs[0])
buses = inputs[1].split(",")
busToCatch, waiting, busCatchTime = 0, 0, 0
for bus in buses:
	isInt = 1
	try: bus = int(bus)
	except: isInt = 0
	if isInt == 1: 
		nextBus = (int(myTime / bus) + 1)*bus; 
		print ("Next", bus, "bus leaves at", nextBus)
		if busToCatch == 0 or nextBus < busCatchTime: busToCatch = bus; busCatchTime = nextBus; waiting = nextBus - myTime
print ("Catch", busToCatch, "bus in", waiting, "minutes. Ticket number is", busToCatch*waiting)
