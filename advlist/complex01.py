#!/usr/bin/env python3
""" Practicing Complex Lists"""

def main():

    #create a simple list
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    #print list
    print(list1)

    #print out second item in list1
    print(list1[1])

    #create a new list with one item
    list2 = ["juniper"]

    #combine lists using extend()
    list1.extend(list2)

    #display list1 which now has list2
    print(list1)

    #create list 3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #append list1 to list3
    list1.append(list3)

    #print the now complex list1
    print(list1)

    #display ip addresses within list1
    print(list1[4])

    #display first item in nested list inside list1
    print(list1[4][0])

#calls main
if __name__ == "__main__":
    main()
