import turtle 

#For now comment out the file that gets us data, because we have it all
#in a textfile for now. When you want the data this file uses to be updated,
#be sure to uncomment this out and get new data from windVectors:
#from windVectors import *

wind_speeds = []
directions = []
coordinates = []

#Open the three files containing the data we need to draw vectors:
wind_speed_file = open("wind_speeds.txt", "r")
directions_file = open("directions.txt", "r")
coordinates_parsed_file = open("coordinates_parsed.txt", "r")

for line in wind_speed_file:
	wind_speeds.append(float(line[0:-1]))

for line in directions_file:
	directions.append(int(line[0:-1]))

for line in coordinates_parsed_file:
	coordinates.append(line[0:-1])

vectors = []



#turtle.setworldcoordinates((44.845110 - 45) * 100, (-124.012927 + 121) * 100, (45.753357 - 45) * 100, (-121.990759 + 121) * 100)

turtle.setworldcoordinates(-100, -60, 60, -30)


for i in range(len(wind_speeds) - 1):
	vectors.append(turtle.Turtle())
	vector = vectors[i]
	if directions[i] == 0:
		vector.color("maroon")
	elif directions[i] == 90:
		vector.color("lime")
	elif directions[i] == 180:
		vector.color("dark blue")
	elif directions[i] == 270:
		vector.color("lime")
	elif directions[i] == 45:
		vector.color("dark orange")
	elif directions[i] == 135:
		vector.color("blue")
	elif directions[i] == 225:
		vector.color("cyan")
	elif directions[i] == 315:
		vector.color("dark orange")
	elif directions[i] == 248:
		vector.color("aquamarine")
	elif directions[i] == 203:
		vector.color("deep sky blue")
	elif directions[i] == 293:
		vector.color("yellow")
	elif directions[i] == 338:
		vector.color("crimson")
	elif directions[i] == 23:
		vector.color("crimson")
	elif directions[i] == 68:
		vector.color("yellow")
	elif directions[i] == 113:
		vector.color("cyan")
	elif directions[i] == 158:
		vector.color("royal blue")

#	vector.hideturtle()
	vector.speed(0)
	coord_components = coordinates[i].split(',')
	y = int((float(coord_components[0]) - 45) * 1000) - 330
	x = int((float(coord_components[1]) + 122) * 1000) + 1000
	print("Coord components: ", coord_components, " X coordinate: ", x, " Y coordinate: ", y)
	vector.penup()
	vector.setpos(x,y)
	vector.left(directions[i] + 90)
	vector.pendown()
	vector.forward(int(wind_speeds[i]) * 5)

turtle.done()
