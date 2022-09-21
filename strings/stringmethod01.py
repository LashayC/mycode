#!/usr/bin/env python

def main():

   # create a string, then split into a list and print
   lilstring = "Alta3 Research offers classes on Python coding"
   newlist = lilstring.split(" ")
   print(newlist)

   # create a list of strings
   myiplist = ["192", "168", "0", "12"]

   #set singleip to result of joining myiplist around "."
   singleip = ".".join(myiplist)

   #display single ip
   print(singleip)

#calls main
if __name__ == "__main__":
    main()
