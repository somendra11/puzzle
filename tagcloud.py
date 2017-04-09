"""tagcloud.py - Use wordfreq to generate a html tag cloud 
(an html tag cloud displays words in alphabetical order.)
The higher the word frequency, the bigger the word."""

import re
from sys import argv

class Puzzle5(object):
    
    def __init__(self, data_file_path, noise_file_path):
        
        self.data_file_path = data_file_path
        self.noise_file_path = noise_file_path
        self.freq_count = {}
        self.initial_font_size = 20
        
    def tagcloud(self):
        """Creates a tag cloud html file in the folder"""
        
        self.noise_data = self.get_noise_data()
        data = self.wordfreq()
        html_data = self.html_wraper(data)
        
        with open("tagcloud.html", "w") as tagcloud_file:
            tagcloud_file.write(html_data)
        print "file Generated"
        
        
    def counter(self, file_line):
        """custom counter function, takes file data 
           count frequency of each word ignoring noise data"""

        for i in file_line:
            if i not in self.noise_data:
                self.freq_count.setdefault(i, 0)
                self.freq_count[i]+=1


    def cleanwords(self, text):
        """removes punctuation, removes words which are just numbers, 
           convert all words to lower case and return them"""

        return re.findall('[a-z]+[\d]+[a-z]+|[a-z]+[\d]+|[\d]+[a-z]+|[a-z]+', text.lower())


    def html_wraper(self, data):
        """create html for tagcloud"""
        
        res = '<html><head></head><body><div style="word-wrap: break-word;width: 1000px;">'
        res += "&nbsp;".join(
            '<span style="font-size: {}; word-wrap: normal;">{}</span>'.format(
                self.initial_font_size+int(freq), 
                word
            ) for word, freq in data
        )
        res += "</div></body></html>"
        return res

    
    def get_noise_data(self):
        """get noise data"""
        
        with open(self.noise_file_path, "r") as noise_file:
            noise_data = set(self.cleanwords(noise_file.read()))
            
        return noise_data
    
    
    def wordfreq(self):
        """counts the frequency of words in a file."""
        
        with open(self.data_file_path, 'r') as data_file:
            for line in data_file.readlines():
                self.counter(self.cleanwords(line))

            return sorted(self.freq_count.items(), key=lambda x: x[0])


if __name__ == "__main__":
    if argv[1]:
        p5 = Puzzle5(argv[1], argv[2])
        p5.tagcloud()
    

