#!/usr/bin/env python3
""" Complex List Challenge: Create a list of animals and print them """

def main():

    #create list of animals
    animals = ["cat", "dog", "fox", "cow", "hen", "cod"]

    #print list of animals
    print(animals)

    #insert item into list
    animals.insert(2, "fly")

    #print list with ant inside
    print(animals)

    #remove cod from list
    animals.remove("cod")

    #print list without cod
    print(animals)

    #create copy of animal list
    animals2 = animals.copy()

    #print animals2 list
    print(animals2)

    #append copy of animals2 to animals
    animals.append(animals2)

    #print animals
    print(animals)

#calls main
if __name__ == "__main__":
    main()
