#!/usr/bin/env python3
""" Copying a file and creating a backup directory """

#imports
import shutil
import os

def main():

    #Move into working directory
    os.chdir("/home/student/mycode/")

    #Make copy of file inside directory
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #Copy directoryA to directoryB. Create directoryB if it doesn't already exit.
    shutil.copytree("5g_research/", "5g_research_backup/")

#calls main
if __name__ == "__main__":
    main()
