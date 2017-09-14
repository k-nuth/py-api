#!/usr/bin/env python
"""
Remove "self" parameter from Doxygen-generated XML documentation
"""

import glob
import os
import sys

if len(sys.argv) != 2:
    print "Usage: remove_self.py <xml_dir>"
    sys.exit(1)

os.chdir(sys.argv[1])
for class_doc in glob.glob("*.xml"):
    print class_doc
    with open(class_doc, 'r') as current_file:
        lines = current_file.readlines()
        print len(lines)
