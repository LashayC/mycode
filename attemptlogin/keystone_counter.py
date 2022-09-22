#!/usr/bin/env python3
""" Parsing files using methods/functions """

def main():
    
    #parse keystone.common.wsgi and return number of failed login attempts

    #counter for fails
    loginfail = 0

    #open file for reading
    keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

    #convert to list
    keystone_file_lines = keystone_file.readlines()

    #loop over list of lines
    for line in keystone_file_lines:
        
        # IF fail patter appeas in line
        if "- - - - -] Authorization failed" in line:
            loginfail += 1    #increment loginfail count

    #print login fails
    print("The number of failed login attempts is", loginfail)

    keystone_file.close()

if __name__ == "__main__":
    main()
