#!/usr/bin/env python3
""" Send request to alta3research-flask01.py for zodiac data """

# imports
import requests
import json
from pprint import pprint
import yaml

# URL link to zodiac api
URL = "http://127.0.0.1:2224/"

def main():

    # request to api
    resp = requests.get(URL + "/alldata")

    # convert JSON to pythonic data
    data = resp.json()

    # display python data with pprint
    print(data)
    pprint(data)
    
    #convert to yaml
    yaml_data = yaml.dump(data, explicit_start = True, default_flow_style = False)
    print(yaml_data)


if __name__ == "__main__":
    main()
