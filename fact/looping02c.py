#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""

def main():
    
    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        #indent to keep dns file object open
        # loop across lines in file
        for svr in dnsfile:   # didn't have to create list of lines to store in memory
            #print and end w/out new line
            print(svr, end="")

#calls main
if __name__ == "__main__":
    main()
