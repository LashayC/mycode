#!/usr/bin/env python3
## create file object in "r"ead mode
file_name = input("What is the name of the file you want to load? ")

with open(file_name, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    counter = 0
    configlist = configfile.readlines()
    for line in configlist:
        counter += 1
print(f"There are {counter} lines in file")

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

