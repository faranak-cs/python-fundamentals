#!/usr/bin/python

import os, sys

for (path, dirs, files) in os.walk(sys.argv[1]):
    # depth = len(path.split('/'))
    print path.split('/')[-1] + "\n"
    for file in files:
         print "         " + file
