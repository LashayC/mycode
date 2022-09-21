#!/usr/bin/env python3
"""Conditionals - strings test true """

def main():
    
    # create string
    ipchk = "192.168.0.1"

    # conditional that tests string as True
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)

#calls main
if __name__ == "__main__":
    main()
