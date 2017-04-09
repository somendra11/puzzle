"""Modify wordfreq.py to open a second file 
that contains only noise words.
Create a word frequency eliminating all the noise words."""

import re
from sys import argv


def Counter(data_file, noise_data, count_dict = {}):
    """custom counter function, takes file data 
       count frequency of each word ignoring noise data"""
    
    for i in data_file:
        if i not in noise_data:
            count_dict.setdefault(i, 0)
            count_dict[i]+=1
            
    return count_dict
        

def cleanwords(text):
    """removes punctuation, removes words which are just numbers, 
       convert all words to lower case and return them"""
    
    return re.findall('[a-z]+[\d]+[a-z]+|[a-z]+[\d]+|[\d]+[a-z]+|[a-z]+', text.lower())


def wordfreq(data_file_path, noise_file_path):
    """counts the frequency of words in a file."""
    
    with open(data_file_path, 'r') as data_file, open(noise_file_path, "r") as noise_file:
        
        noise_data = set(cleanwords(noise_file.read()))
        counts = Counter(cleanwords(data_file.read()), noise_data)
        return sorted(counts.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    if argv[1]:
        print wordfreq(argv[1], argv[2])
    

