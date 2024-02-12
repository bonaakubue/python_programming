# Importing a module

import mod

# Importing specific names
from mod import multiply
from mod import divide

#importing with an alias
import mod as md
from mod import multiplication as mp

# Importing all definitions
from mod import *

# Reloading modules
import greeting
import importlib
#reload module greeting
importlib.reload(greeting)
