##
##  list_vms.py
##  src/shell/commands
##
##  Created by mflr0 on 25/03/2024.
##  Contributor(s): mflr0
##

from include.lib import *

def run_list_vms(si):
    list_vms(si)

def list_vms(si):
    """
    List all VMs.
    """
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vm_names = [vm.name for vm in container.view]
    vm_names.sort()
    for vm_name in vm_names:
        print(vm_name)
    container.Destroy()