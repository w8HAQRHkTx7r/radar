icao24=0
callsign=1
origin_country=2
time_position=3
last_contact=4
latitude=5
longitude=6
baro_altitude=7
on_ground=8
velocity=9
true_track=10
vertical_rate=11
sensors=12
geo_altitude=13
squawk=14
spi=15
position_source=16
category=17

import requests

categoryTable = {
	0 : "No information at all",
	1 : "No ADS-B Emitter Category Information",
	2 : "Light (< 15500 lbs)",
	3 : "Small (15500 to 75000 lbs)",
	4 : "Large (75000 to 300000 lbs)",
	5 : "High Vortex Large (aircraft such as B-757)",
	6 : "Heavy (> 300000 lbs)",
	7 : "High Performance (> 5g acceleration and 400 kts)",
	8 : "Rotorcraft",
	9 : "Glider / sailplane",
	10 : "Lighter-than-air",
	11 : "Parachutist / Skydiver",
	12 : "Ultralight / hang-glider / paraglider",
	13 : "Reserved",
	14 : "Unmanned Aerial Vehicle",
	15 : "Space / Trans-atmospheric vehicle",
	16 : "Surface Vehicle – Emergency Vehicle",
	17 : "Surface Vehicle – Service Vehicle",
	18 : "Point Obstacle (includes tethered balloons)",
	19 : "Cluster Obstacle",
	20 : "Line Obstacle",
}

# Make the REST API request
url = "https://opensky-network.org/api/states/all?lamin=41.6&lomin=-88.5&lamax=42.0&lomax=-87.6&extended=1"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    json_data = response.json()
    print(json_data['time'])
    for i in range(len(json_data['states'][0])) :
        print(json_data['states'][0][i]," ", end='')
    print("")
    for i in range(len(json_data['states'])) :
        d = json_data['states'][i]
        print(d[category], d[origin_country], d[callsign], d[latitude], d[longitude], d[baro_altitude])

    # Print the JSON data in columnar form
#    if isinstance(json_data, list) and len(json_data) > 0 and isinstance(json_data[0], dict):
#        print_columnar_data(json_data)
#    else:
#        print("Invalid JSON format.")

else:
    print(f"Request failed with status code {response.status_code}.")

