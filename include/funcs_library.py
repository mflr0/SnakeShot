##
##  funcs_library.py
##  src
##
##  Created by mflr0 on 13/03/2024.
##  Contributor(s): mflr0
##

from src.auth.vAuth import *

def auth_funcs():
    auth_funcs = [vAuth]
    for func in auth_funcs:
        func()

