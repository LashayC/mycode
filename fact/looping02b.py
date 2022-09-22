#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

def main():
    
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        #indent ot keep dnsfile open
        #create list of lines
        dnslist = dnsfile.readlines()

        #loop over lines
        for svr in dnslist:
            #print and end w/out new line
            print(svr, end="")

#file closed automatically

#calls main
if __name__ == "__main__":
    main()
