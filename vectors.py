import turtle 
from windVectors import *

vectors = []

turtle.setup(400, 300, 400, 300)
turtle.setworldcoordinates((45.459813 - 45) * 750, (-122.526185 + 121) * 750, (45.753357 - 45) * 750, (-121.990759 + 121) * 750)

for i in range(len(wind_speeds) - 1):
	vectors.append(turtle.Turtle())
	vector = vectors[i]
	vector.speed(10)
	coord_components = coordinates[i].split(',')
	x = int((float(coord_components[0]) - 45) * 1000)
	y = int((float(coord_components[1]) + 122) * 1000)
	print("Coord components: ", coord_components, " X coordinate: ", x, " Y coordinate: ", y)
	vector.penup()
	vector.setpos(x,y)
	vector.left(directions[i])
	vector.pendown()
	vector.forward(int(wind_speeds[i]) * 10)

turtle.done()
