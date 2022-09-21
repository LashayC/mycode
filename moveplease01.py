#!/usr/bin/env python3
""" Moving and Renaming Files Practice """

#imports
import shutil
import os

def main():

    # make program start in the working directory
    os.chdir('/home/student/mycode/')

    # move file into different folder
    shutil.move('raynor.obj', 'ceph_storage/')

    # ask user for new kerrigan.obj file name
    xname = input('What is the new name for kerrigan.obj?')

    # rename the kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#calls main
if __name__ == "__main__":
    main()
