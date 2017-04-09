"""wordfreq.py - open a text file, 
read the text, process it using clearnwords.
Count the number of occurences of each unique word."""

import re
from sys import argv
from collections import Counter


def cleanwords(text):
    """removes punctuation, removes words which are just numbers, 
       convert all words to lower case and return them"""
    
    return re.findall('[a-z]+[\d]+[a-z]+|[a-z]+[\d]+|[\d]+[a-z]+|[a-z]+', text.lower())

def wordfreq(file_path):
    "counts the frequency of words in a file."
    
    with open(file_path, 'r') as infile:
        counts = Counter(cleanwords(infile.read()))
        return sorted(counts.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    if argv[1]:
        print wordfreq(argv[1])
    

