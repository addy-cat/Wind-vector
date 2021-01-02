import turtle 
from windVectors import *
from turtle import Turtle, Screen

vectors = []

screen = Screen()
#screen.setup(900, 800)

turtle.setworldcoordinates((44.845110 - 45) * 100, (-124.012927 + 121) * 100, (45.753357 - 45) * 100, (-121.990759 + 121) * 100)

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

	vector.hideturtle()
	vector.speed(0)
	coord_components = coordinates[i].split(',')
	x = int((float(coord_components[0]) - 45) * 1000) - 200
	y = int((float(coord_components[1]) + 122) * 1000)
	print("Coord components: ", coord_components, " X coordinate: ", x, " Y coordinate: ", y)
	vector.penup()
	vector.setpos(x,y)
	vector.left(directions[i])
	vector.pendown()
	vector.forward(int(wind_speeds[i]) * 3)

turtle.done()
