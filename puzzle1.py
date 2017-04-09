# Write a function getwords(text) to take a string, parse it and return words (tokens).

from sys import argv

def getwords(text):
    """take a string, parse it and return words"""
    
    return text.strip().split()


if __name__ == "__main__":
    if argv[1]:
        print getwords(argv[1])
    