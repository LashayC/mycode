#!/usr/bin/env python3
""" ISS Tracker api challenge"""

#imports
import requests
import datetime
import reverse_geocoder as rg

def main():
    
    # Send request to api
    resp = requests.get("http://api.open-notify.org/iss-now.json")

    # decode response to python data
    data = resp.json()

    # convert epoch time to date time
    epoch = data["timestamp"]
    date_time = datetime.datetime.fromtimestamp(epoch)

    # get location from lat/lon
    lat = data["iss_position"]["latitude"]
    lon = data["iss_position"]["longitude"]

    # reverse_geocoder MUST be passed a tuple as the argument!
    coords_tuple= (lat, lon)
    result = rg.search(coords_tuple)

    #splice through geocoder result
    city = result[0]["name"]
    country = result[0]["cc"]

    # print current location of ISS
    print(f'''
            CURRENT LOCATION OF THE ISS:
            Timestamp: {date_time}
            Lon: {data["iss_position"]["longitude"]}
            Lat: {data["iss_position"]["latitude"]}
            City/Country: {city}, {country}
            ''')


if __name__ == "__main__":
    main()
