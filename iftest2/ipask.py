#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

def main():

    # get input for ip address
    ipchk = input ("Apply an IP address: ")

    # conditional to check if string is true
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("You did not provide input")
   

#calls main
if __name__ == "__main__":
    main()
