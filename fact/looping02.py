#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

def main():

    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")

    #create list of lines
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        #print and end w/out a new line
        print(svr, end="")

    #close the file - best practice when using open()
    dnsfile.close()

#calls main
if __name__ == "__main__":
    main()
