#!/usr/bin/env python3
""" Monty Python title guessing game using conditionals"""

def main():

    # counter to track rounds
    round = 0

    # while loop that is True until break
    while True:
        # counter to incr each round
        round = round + 1

        # print question
        print("Finish the movie title, 'Monty Python\'s The Life of _____'")

        # get user input
        answer = input("Your guess -->")

        # conditional to check if input correct
        if answer == "Brian":
            print("Correct")
            break
        elif round == 3:
            print("Sorry, the answer was Brian")
            break
        else:
            print("Sorry. Try again!")

#calls main
if __name__ == "__main__":
    main()
