#!/usr/bin/env python3
""" Practincing for loops """

def main():

    #create list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]

    #list of approved vendors
    approved_vendors = ["cisco", "juniper", "big_ip"]

    #loop accross the list vendors
    for x in vendors:
        print("\nThe vendor is: " + x, end="")  #each loop print value of x
        if x not in approved_vendors:
            print("- NOT AN APPROVED VENDOR!", end="")

    #ending flair print
    print("Our loop has ended.")

#calls main
if __name__ == "__main__":
    main()
