#!/usr/bin/env python 3
""" Runs git commands to push to HEAD """

#imports
import os

def main():

    # move to working directory
    os.chdir('/home/student/mycode/')

    # run git status
    git.status

    # run git add for all files in mycode/
    git add *

#calls main
if __name__ == "__main__":
    main()
