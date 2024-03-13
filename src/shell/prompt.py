##
##  prompt.py
##  src/shell
##
##  Created by mflr0 on 13/03/2024.
##  Contributor(s): mflr0
##

from include.lib import *
from include.funcs_library import *

def prompt(si):
    while True:
        command = input("SnakeShot $ ")
        if command == "exit":
            break
        elif os.path.isfile(f"commands/{command}.py"):
            exec(open(f"commands/{command}.py").read())
        else:
            print("Command not found")