#!/usr/bin/env python
from operator import itemgetter

import sys

def reducer():

    for line in sys.stdin:
        if line.strip() == "":
            continue
        print line

if __name__ == '__main__':
    reducer()