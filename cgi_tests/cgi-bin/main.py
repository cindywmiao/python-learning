#!/usr/bin/env python

import cgi, cgitb
from .sources import *

print("Content-type : text/html \n\n")
print(img("../views/add.png"))