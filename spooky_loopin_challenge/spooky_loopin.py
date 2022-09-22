#!/usr/bin/env python3
""" Looping challenge on the book 'Dracula' by Bram Stoker"""

def main():

    ## PART1: read contents of Dracula novel as file object
    ## PART2: Loop over every line in Dracula, print ea line out
    ## PART3: Actually, fix that for loop... only print out the line if it has the word vampire in it!
    ## PART4: If you didn't already, make sure it prints the line no matter what case vampire is!
    ## PART5: Count that up! How many times does the word vampire appear?
    ## PART6: Take the lines from Dracula that have vampire in it and write them to a second file named vampytimes.txt.
   
   # create counter
    vampire_counter = 0

    # open dracula file object
    with open("/home/student/mycode/spooky_loopin_challenge/dracula.txt", "r") as dracula_file:
       
        # loop through dracula_ list  
        for line in dracula_file:

            # IF vampire in line print, increment counter
            if "vampire" in line.lower():
                print(line, end="")
                vampire_counter += 1

                # create and open file in append mode. write each line containing vampire to it
                with open("/home/student/mycode/spooky_loopin_challenge/vampytimes.txt", "a") as vampytimes_file:
                    vampytimes_file.write(line + "\n")

    # print vampire_counter
    print(f"The word vampire is mentioned {vampire_counter} times.")

    # print loop has ended (flair)
    print("\nThe loop has ended")

if __name__ == "__main__":
    main()
