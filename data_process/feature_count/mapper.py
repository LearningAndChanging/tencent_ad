#!/usr/bin/env python
from operator import itemgetter
import sys
import os

def mapper():
    filepath = os.environ["map_input_file"]
    filename = os.path.split(filepath)[-1]
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        if "userFeature" in filename:

            # remove leading and trailing whitespace

            line = line.strip()
            # split the line into words
            words_raw = line.split('|')
            # increase counters
            for words in words_raw:
                # write the results to STDOUT (standard output);
                # what we output here will be the input for the
                # Reduce step, i.e. the input for reducer.py
                #
                # tab-delimited; the trivial word count is 1
                word_split = words.strip().split()
                word_list = word_split[1:]
                word_list.sort()
                word_data = ' '.join(word_list)
                if "uid" not in words and "app" not in words and "topic" not in words and "interest" not in words and "kw" not in words:
                    for i in range(1,len(word_split)):
                        print '%s\t%s' % (word_split[0] + ' ' + word_data, 1)

if __name__ == "__main__":
    mapper()
