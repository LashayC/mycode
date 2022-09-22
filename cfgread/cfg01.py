#!/usr/bin/env python3
""" Exploring different ways of using .read() """

def main():

    #create file object in read mocde
    configfile = open("vlanconfig.cfg", "r")

    # display file to screen
    print(configfile.read())

    # close file
    configfile.close()

    ##Explore readlines
    #recreate file object
    configfile = open("vlanconfig.cfg", "r")

    #make list of files lines with .readlines()
    configlist = configfile.readlines()
    print(configlist)

    # iterate through configlist
    for x in configlist:
        print(x.strip())

    #close file
    configlist.close()

if __name__ == "__main__":
    main()
