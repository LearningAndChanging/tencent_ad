#!/usr/bin/env python

from operator import itemgetter
import sys


def reducer():
    current_word = None
    current_count_0 = 0
    current_count_1 = 0
    word = None
    
    print '%s\t%s\t%s' % ("current_word", "current_count_0", "current_count_1")
    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        if line.strip() == "":
            continue

        # parse the input we got from mapper.py
        word_raw, label = line.split('\t', 1)
        # convert count (currently a string) to int
        word = ' '.join(word_raw.split()[:-1])
        try:
            label = int(label)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue
        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_word == word and label == 0:
            current_count_0 += 1
        elif current_word == word and label == 1:
            current_count_1 += 1
        else:
            if current_word:
                # write result to STDOUT
                print '%s\t%s\t%s' % (current_word, current_count_0, current_count_1)
            if label == 0:
                current_count_0 = 1
                current_count_1 = 0
            if label == 1:
                current_count_0 = 0
                current_count_1 = 1
            current_word = word
    # do not forget to output the last word if needed!
    if current_word == word:
        print '%s\t%s\t%s' % (current_word, current_count_0, current_count_1)

if __name__ == '__main__':
    reducer()
