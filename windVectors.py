
import numpy as np
import requests
import json
import math
import turtle


coordinate_file = open("coordinates.txt", "r")
for line in coordinate_file:
	coordinates = line[0:-1].split(' ')

print(len(coordinates))

wind_speeds = []
wind_direction = []

for coords in coordinates:
	response = requests.get("https://api.weather.gov/points/" + coords)
	#find the forecast component of the above file (have to go thru properties first):
	response = response.json()['properties']
	response = response['forecast']
	#new API call on response, where response is now in the correct URL format
	response_gridpoints = requests.get(response)

	#The above line will also retrieve coordinates that are in the ocean,
	#which the API has no windspeed or wind direction data for. This leads
	#to a 404 for that URL. We need to catch these 404's:

	print(response_gridpoints.status_code)

	if response_gridpoints.status_code == 200:
		response_gridpoints = response_gridpoints.json()['properties']
		response_gridpoints = response_gridpoints['periods']
		#We have now found location of "windSpeed", need to add this data to
		#the wind_speeds array defined on line 12
		before_parse_speed = response_gridpoints[0]['windSpeed'][0:-4]
		if len(before_parse_speed) <= 5:
			wind_speeds.append(int(before_parse_speed))
		else:
			speed_components = before_parse_speed.split(' ')
			first_num = speed_components[0]
			sec_num = speed_components[2]
			#find average of the two wind speeds
			wind_speeds.append((int(first_num) + int(sec_num))/2)
		
		wind_direction.append(response_gridpoints[0]['windDirection'])
	else:
		#if API returns a 500, 503, 404 or anything other than
		#200, put in a zero for that call because we don't want it
		wind_speeds.append(0)
		wind_direction.append('N')


#Right now the wind directions are in cardinal mode. Need to change these
#to degrees so we can make wind vectors. Overwrite the previous direction array:

directions = []

for direction in wind_direction:
        if direction == 'N':
                directions.append(0)
        elif direction == 'E':
                directions.append(90)
        elif direction == 'S':
                directions.append(180)
        elif direction == 'W':
                directions.append(270)
        elif direction == 'NE':
                directions.append(45)
        elif direction == 'SE':
                directions.append(135)
        elif direction == 'SW':
                directions.append(225)
        elif direction == 'NW':
                directions.append(315)
        elif direction == 'WSW':
                directions.append(248)
        elif direction == 'SSW':
                directions.append(203)
        elif direction == 'WNW':
                directions.append(293)
        elif direction == 'NNW':
                directions.append(338)
        elif direction == 'NNE':
                directions.append(23)
        elif direction == 'ENE':
                directions.append(68)
        elif direction == 'ESE':
                directions.append(113)
        elif direction == 'SSE':
                directions.append(158)
	
np.savetxt("wind_speeds.txt", np.array(wind_speeds), fmt="%s")
np.savetxt("directions.txt", np.array(directions), fmt="%s")
np.savetxt("coordinates_parsed.txt", np.array(coordinates), fmt="%s")



#Print the arrays so we can see the speeds and direction, and 
#print the number of speeds and directions
print(wind_speeds)
print(directions)
print(len(wind_speeds))
print(len(directions))



























