#13
with open('input.txt', 'r') as input:
	inputs = input.readlines()
nextBus = 0
myTime = int(inputs[0])
buses = inputs[1].split(",")
busNumbers = []
busToCatch, waiting, busCatchTime, a, i, b, step = 0, 0, 0, 0, 0, 0, 1
for bus in buses:
	isInt = 1
	try: bus = int(bus)
	except: isInt = 0; 
	if isInt == 1: 
		busNumbers.append(bus)
		buses[a]=buses[a].strip()
		nextBus = (int(myTime / bus) + 1)*bus; 
		print ("Next", bus, "bus leaves at", nextBus)
		if busToCatch == 0 or nextBus < busCatchTime: busToCatch = bus; busCatchTime = nextBus; waiting = nextBus - myTime
	else : bus = 1
	a+=1

print ("Catch", busToCatch, "bus in", waiting, "minutes. Ticket number is", busToCatch*waiting)
busesOnTime = False
next = 0
while not busesOnTime:
	for bus in busNumbers[next:]:
		b = buses.index(str(bus))
		if (i+b) % bus != 0: break
		else:
			step*=bus
			if next == len(busNumbers)-1: busesOnTime = True;
			next+=1
	i+=step
	if i> 10000000000000000: print("Alright, something is clearly wrong here, wrap it up."); break
answer = i-step
print ("It woud take", answer, "steps for every bus to turn up at the designated schedule")
