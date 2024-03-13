##
##  version.py
##  src/shell/commands
##
##  Created by mflr0 on 13/03/2024.
##  Contributor(s): mflr0
##

from include.lib import *
from include.funcs_library import *

def version_number():
    version_number = "0.1.0"
    return version_number

def version(version_number):
    print ("SnakeShot version ", version_number)
    print ("Developed by mflr0\n")
    print ("Versioning scheme: A.B.C")
    print ("A represents the major version (backward-incompatible changes).\nB represents the minor version (backward-compatible additions).\nC represents the patch version (backward-compatible bug fixes).\n")
    print ("Current version: ", version_number)