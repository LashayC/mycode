#!/usr/bin/env python3
""" Using python to parse CSV data """

def main():
    
    # create and open adming.rc file object
    outFile = open("admin.rc", "a")

    # get input from user for os_auth_url
    osAuth = input("What is the OS_AUTH_URL? ")

    # print os auth and also append to outFile. Also renames outFile to file
    print("export OS_AUTH_URL=" + osAuth, file=outFile)

    # print and append statement to ouFile
    print("export OS_IDENTITY_API_VERSION=3", file=outFile)

    # get input for OS_PROJECT_NAME, print, and write to file
    osPROJ = input("What is the OS_PROJECT_NAME? ")
    print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

    # get input for OS_PROJECT_DOMAIN_NAME, print and write to file
    osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
    print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

    osUSER = input("What is the OS_USERNAME? ")
    print("export OS_USERNAME=" + osUSER, file=outFile)

    osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
    print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

    osPASS = input("What is the OS_PASSWORD? ")
    print("export OS_PASSWORD=" + osPASS, file=outFile)
    outFile.close()

if __name__ == "__main__":
    main()
