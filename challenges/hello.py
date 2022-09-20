#!/usr/bin/env python3
"""Asks user name and day of the week then stdout"""

def main():

    # input to ask name and store value
    name = input("What is your name?")

    # input to ask what day of the week it is and store value
    day_of_week = input("What day of the week is it?")

    # print to display inputs back in format: Hello, <name>! Happy <day of the week>!
    print(f"Hello, {name}! Happy {day_of_week}!")

# this calls main
main()
