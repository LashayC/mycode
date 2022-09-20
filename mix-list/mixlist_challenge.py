#!/usr/bin/env python3
"""Prints the IP addresses from the list"""

def main():

    #Create IP list
    iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

    #Display IP addresses in list
    print(f"IP Addresses: {iplist[3:5]} {iplist[3]}, {iplist[4]}")

#calls main
if __name__ == "__main__":
    main()
