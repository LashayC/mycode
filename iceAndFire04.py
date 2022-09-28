#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        #return house and list of books they appear in
        #send 2nd request for house from character
        print(f'the books they appear in are {got_dj["books"]}')
        
        if got_dj['allegiances']:

            char_house_req = requests.get(got_dj['allegiances'])
            char_house = char_house_req.json()
            print(f'Their house is {char_house["name"]}')
        else:
            print('No house associated')

if __name__ == "__main__":
        main()

