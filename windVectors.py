import requests
import json


coordinate_file = open("coordinates.txt", "r")
for line in coordinate_file:
	coordinates = line[0:-1].split(' ')


#print(coordinates[7])

wind_speeds = []
wind_direction = []

for coords in coordinates:
	response = requests.get("https://api.weather.gov/points/" + coords)
	#find the forecast component of the above file (have to go thru properties first):
	response = response.json()['properties']
	response = response['forecast']
	#new API call on response, where response is now in the correct URL format because of line 16
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
		wind_speeds.append(response_gridpoints[0]['windSpeed'])
		wind_direction.append(response_gridpoints[0]['windDirection'])
	


print(wind_speeds)
print(wind_direction)

'''
response = requests.get("https://api.weather.gov/gridpoints/PQR/62,81/forecast")

print(response.status_code)

windspeeds = response.json()['properties']
windspeeds = windspeeds['periods']


windspeeds1 = []

for d in windspeeds:
	speed = d['windSpeed']
	windspeeds1.append(speed)

print(windspeeds1)
'''
	
