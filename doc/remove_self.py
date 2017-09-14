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
    lines_to_write = []
    with open(class_doc, 'r') as current_file:
        read_lines = current_file.readlines()
        i = 0
        while i < len(read_lines):
            if read_lines[i].strip() == "<param>":
                if "self" in read_lines[i+1].strip():
                    i = i + 4
                else:
                    lines_to_write.append(read_lines[i])
                    i = i + 1
            elif "(self" in read_lines[i]:
                lines_to_write.append(read_lines[i].replace("(self,", "(").replace("(self", "("))
                i = i + 1
            else:
                lines_to_write.append(read_lines[i])
                i = i + 1
    with open(class_doc, 'w') as modified_file:
        modified_file.writelines(lines_to_write)
