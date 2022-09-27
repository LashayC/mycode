#!/usr/bin/env python3
"""Review of try and except logic | Alta3 Research"""

# Starrt with an infinite loop 
while True:
    try:
        print("Enter a file name: ")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems witht that file name.")
        break
    except:
        print("Error with that file name! Try again...")
