#!/usr/bin/env python3
""" Create a list and print """

def main():

    #Creating a list
    my_list = ["192.168.0.5", 5060, "UP"]

    #Listing the first item of my_list
    print("The first item in the list (IP): " + my_list[0])

    #Listing the second item of my_list
    print("The second item in the list (port): " + str(my_list[1]))

    #Listing the third item of my_list
    print("The last item in the list (state): " + my_list[2])

#calls main()
if __name__ == "__main__":
    main()
