#!/usr/bin/env python3
""" Send 51 requests to fast URL api """

#imports
import requests

def main():

    for i in range(51):

        URL = "http://0.0.0.0:2224/fast"
        resp = requests.get(URL)
        print(resp)

    print("request to fast has finished")

if __name__ == "__main__":
    main()
