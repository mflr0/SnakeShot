##
##  lib.py
##  include
##
##  Created by mflr0 on 13/03/2024.
##  Contributor(s): mflr0
##

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import ssl
import getpass
import re