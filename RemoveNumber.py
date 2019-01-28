import re
inputfile = open("trips.txt")                    
outputfile = open("output.txt","w+")

for line in inputfile:
	line = line.split(',')
	trip = line[3]
	if trip != "" and re.search(r'\d', trip):
		trip = re.split(r'(\d+)', trip)
		del trip[0:2]
		trip = ''.join(trip)
		trip = trip[1:]
		line[3] = trip
		print(trip)
	line = ','.join(line)
	outputfile.write(line)


	