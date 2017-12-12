#!/usr/bin/env python
"""
This program will process dict file and create a new one,
to ensure that there is no invalid word in the dict file.

@author: FATESAIKOU
@argv[1]: orginal dict file
@argv[2]: new dict file name
"""

import sys
import re

def main():
    ORI_FILE = sys.argv[1]
    TAR_FILE = sys.argv[2]

    r_src = open(ORI_FILE, 'r')
    content = r_src.read()
    r_src.close()

    w_src = open(TAR_FILE, 'w')
    content = re.sub(r'\n?[^\n]*[^\w^\n][^\n]*\n', '\n', content)
    content = re.sub(r'[\n]+', '\n', content)
    w_src.write(content)
    w_src.close()


if __name__ == "__main__":
    main()


