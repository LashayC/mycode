#!/usr/bin/env python3

#imports
import netifaces

def main():
    
    # call netfaces.interfaces() inside print
    print(netifaces.interfaces())
    
    # loop over netifaces.inside()
    for i in netifaces.interfaces():
        # print line to indicate which interface is shown
        print('\n**************Details of Interface - ' + i + ' *********************')
        
        #code to catch possible errors
        try:
            #print mac address of interface being looked at
            print('MAC: ', end='') # This print statement will always print MAC without an end of line)
            print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

            #prints ip addrss of interface being looked at
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        except:
            print('Could not collect adapter information') #prints error message

if __name__ == "__main__":
    main()
