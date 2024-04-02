##
##  get_obj.py
##  src
##
##  Created by mflr0 on 02/04/2024.
##  Contributor(s): mflr0
##

from include.lib import *

def get_obj(content, vimtype, name):
    """
    Get the vsphere object associated with a given text name.
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj