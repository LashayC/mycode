#!/usr/bin/env python3
""" List Challenge: Use input, lists, print, concatenate, and variables"""

def main():

    #import random module
    import random

    #create wordbank list
    wordbank = ["indentation", "spaces"]

    #create tlg list
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    #append 4 to wordbank
    wordbank.append(4)

    #get input between 0 and 18, convert string to integer
    num = input("Please provide a number between 0 and 18")

    #get random input between 0 and 18
    random_num = random.randint(0, 18)

    #print num
    print(f"The value of num is: {num}")

    #print random number
    print(f"The random number is: {random_num}")

    #Slice one of the elements from tlgstudents list with num
    #student_name= tlgstudents[num]

    #If user gives name instead of number, store name in variable
    if num.isdigit():
        num = int(num)
        student_name = tlgstudents[num]
    else:
        student_name = num

    #print student_name and items from wordbank
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")


#calls main
if __name__ == "__main__":
    main()
