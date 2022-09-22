#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt."""

def main():
    
    #open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:

        #loop accross lines in file
        for svr in dnsfile:
            svr = svr.rstrip('\n') ##removes newline char if there. In here its on everything but the last line
            print(svr)

            # IF the string svr ends with 'org'
            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile: #a is append mode
                    srvfile.write(svr + "\n")

            # ELIF string svr ends with 'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile: 
                    srvfile.write(svr + "\n")


if __name__ == "__main__":
    main()

