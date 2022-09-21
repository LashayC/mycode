#!/usr/bin/env python3
""" Gets input from user then runs conditional against value """

def main():
    
    # get input from user
    hostname = input("What value should we set for hostname?")
    
    # conditional that prints statement if hostname.lower() == mtg
    if hostname.lower() == "mtg":
        print("The hostname was found to be MTG")
        print("hostname matches expected config")

    # always prints out 'exiting the script' to user on final line
    print("Exiting the script")

#calls main
if __name__ == "__main__":
    main()
