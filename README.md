# Wind vectors

This program visualizes wind velocity vectors onto a map of Northwest Oregon (bottom left is near Lincoln City Oregon, top right is Southern Washington). These vectors are made up of a speed and direction component, taken from the National Weather Service API. Each vector exists at a specific coordinate on a grid overlaid onto the map. As of right now, everything I wanted to do is done. But this program is sort of ugly... learning OpenGL to make prettier models right now!

This program uses Python3 and the "turtles" library to draw the vectors. This "turtles" library is really mainly a tool used for education and introductory Python practice. It is basically impossible to make the vectors look or act any nicer because this library is very basic. This is the primary reason I will not be updating the project as I want to move on to learning OpenGL for modelling my data. However, using this library was a great introduction to modelling data.

Each vector represents a velocity vector for the wind behavior in that longitude and latitude. The colors of the vectors cooresponds to wind directions. Red colors represent a more Northern angle while cooler colors represent a more Southern angle. The colors gradually go from a dark red to a dark blue when going from North to South. The length of a vector cooresponds to the wind speed. A longer vector length indicates a higher wind speed, while a shorter vector length indicates a slower wind speed.

The directionless, speed-less red vectors that can be seen off the coast in the ocean are where the API returns a 404 for the wind data at that location. This is because the API does not gather wind data here. You can also notice an occasional dead vector on land. These are most commonly the API returning 500's because of some error on the APIs part. These are resolved easily but a few are common.

All vectors are placed onto this grid based on specific coordinate values in the form of longitudes and latitudes. Using the National Weather Service API, one could get any collection of coordinates from anywhere in the US. 

As for the map, this is a screenshot of the map data available from ArcGIS. This is a screenshot of Northwest Oregon (it might look like the whole state but its just a little chunk!).

Theoretically I could have made many more vectors than shown below, maybe even for the whole US, you would simply need to specify more coordinates in the included coordinates.txt file. I felt this was enough vectors to get the message across.

Here is an example run from 3/25/2021:

![Wind Vectors](windVectors.png)
