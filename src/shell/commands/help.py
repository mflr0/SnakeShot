##
##  list_vms.py
##  src/shell/commands
##
##  Created by mflr0 on 25/03/2024.
##  Contributor(s): mflr0
##

def run_help():
    help()

def help():
    """
    Display help message.
    """
    print("Available commands:")
    print("  - list_datacenters: List all datacenters")
    print("  - list_vms: List all VMs")
    print("  - help: Display this help message")
    print("  - exit: Exit the shell")