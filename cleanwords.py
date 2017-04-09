"""clearnwords.py - Modify getwords and call it cleanwords(text). 
Cleanwords removes punctuation, removes words which are just numbers, 
convert all words to lower case and return them."""

import re
from sys import argv

def cleanwords(text):
    """removes punctuation, removes words which are just numbers, 
       convert all words to lower case and return them"""
    
    return re.findall('[a-z]+[\d]+[a-z]+|[a-z]+[\d]+|[\d]+[a-z]+|[a-z]+', text.lower())


if __name__ == "__main__":
    if argv[1]:
        print cleanwords(argv[1])
    

