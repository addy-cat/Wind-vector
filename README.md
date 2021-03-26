# Wind vectors

This program visualizes wind velocity vectors onto a map of Northwest Oregon. These vectors are made up of a speed and direction component, taken from the National Weather Service API. Each vector exists at a specific coordinate on a grid overlaid onto the map. As of right now, everything I wanted to do is done. But this program is sort of ugly... learning OpenGL to make prettier models right now!

Each vector represents a velocity vector for the wind behavior in that longitude and latitude. The colors of the vectors cooresponds to wind directions. Red colors represent a more Northern angle while cooler colors represent a more Southern angle. The colors gradually go from a dark red to a dark blue when going from North to South. The length of a vector cooresponds to the wind speed. A longer vector length indicates a higher wind speed, while a shorter vector length indicates a slower wind speed.

The directionless, speed-less red vectors that can be seen off the coast in the ocean are where the API returns a 404 for the wind data at that location. This is because the API does not gather wind data here. You can also notice an occasional dead vector on land. These are most commonly the API returning 500's because of some error on the APIs part. These are resolved easily but a few are common.

All vectors are placed onto this grid based on specific coordinate values in the form of longitudes and latitudes. Using the National Weather Service API, one could get any collection of coordinates from anywhere in the US. 

As for the map, this is a screenshot of the map data available from ArcGIS. This is a screenshot of Northwest Oregon (it might look like the whole state but its just a little chunk!).

Here is an example run from 3/25/2021:

![Wind Vectors](windVectors.png)
