#!/usr/bin/env python3

##
##  SnakeShot.py
##  SnakeShot
##
##  Created by mflr0 on 13/03/2024.
##  Contributor(s): mflr0
##

from include.lib import *
from include.funcs_library import *

def main():
    print ("Welcome to SnakeShot, the vSphere inventory tool")
    print ("This tool will list all ESXi hosts in the vSphere server and print information about the vCenter Server.")
    print ("Developed by mflr0")
    print ("https://github.com/mflr0/SnakeShot")
    print ("Version: ", version_number())

    try:
        si = vAuth()
        if si is not None:
            prompt(si)
        else:
            print("Failed to connect to vSphere")
    except KeyboardInterrupt:
        print("\nUser interrupted the program, exiting...")

if __name__ == "__main__":
    main()