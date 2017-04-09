"""linkedcloud.py - Modify tagcloud.py to link each word 
to all the lines that contain it.
For example, when you click on a word, 
it should display all the lines where the word occurs."""

import re
from sys import argv

class Puzzle6(object):
    
    def __init__(self, data_file_path, noise_file_path):
        
        self.data_file_path = data_file_path
        self.noise_file_path = noise_file_path
        self.freq_count = {}
        self.initial_font_size = 20
        self.file_dict = {}
        
    def tagcloud(self):
        """Creates a tag cloud html file in the folder"""
        
        self.noise_data = self.get_noise_data()
        data = self.wordfreq()
        html_data = self.html_wraper(data)
        
        with open("tagcloud.html", "w") as tagcloud_file:
            tagcloud_file.write(html_data)
        print "file Generated"
        
        
    def counter(self, file_line, line_number):
        """custom counter function, takes file data 
           count frequency of each word ignoring noise data"""

        for i in file_line:
            if i not in self.noise_data:
                self.freq_count.setdefault(i, [0,set()])
                self.freq_count[i][0]+=1
                self.freq_count[i][1].add(line_number)


    def cleanwords(self, text):
        """removes punctuation, removes words which are just numbers, 
           convert all words to lower case and return them"""

        return re.findall('[a-z]+[\d]+[a-z]+|[a-z]+[\d]+|[\d]+[a-z]+|[a-z]+', text.lower())


    def html_wraper(self, data):
        """create html for tagcloud"""
        
        res = '<html><head>'
        
        res += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>'
        res += '''
                <script>
                $(document).ready(function(){
                    $(".loginlink").click(function(){
                        var myClass = $(this).attr("class").split(" ");
                        myClass.shift();
                        alert(myClass);
                    });
                });
                </script>'''
        res += '</head><body><div style="word-wrap: break-word;width: 1000px;">'
        res += "&nbsp;".join(
            '<a href="javascript:void(0)" class="loginlink {}">'
            '<span style="font-size: {}; word-wrap: normal;">{}</span></a>'.format( 
                " ".join(str(i) for i in lines),
                self.initial_font_size+int(freq),
                word
            ) for word, (freq, lines) in data
        )
        res += "</div><div>"
        for key, value in self.file_dict.iteritems():
            res += '<p id="{}" class="file-data" style="display: none;">{}</p>'.format(key, value)
        res += '<div>'
        res += '</body></html>'
        return res

    
    def get_noise_data(self):
        """get noise data"""
        
        with open(self.noise_file_path, "r") as noise_file:
            noise_data = set(self.cleanwords(noise_file.read()))
            
        return noise_data
    
    
    def wordfreq(self):
        """counts the frequency of words in a file."""
        
        with open(self.data_file_path, 'r') as data_file:
            for line_number, line in enumerate(data_file.readlines()):
                self.file_dict.update({line_number: line})
                self.counter(self.cleanwords(line), line_number)

            return sorted(self.freq_count.items(), key=lambda x: x[0])


if __name__ == "__main__":
    if argv[1]:
        p6 = Puzzle6(argv[1], argv[2])
        p6.tagcloud()
    

