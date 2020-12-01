# ********************************************************************************
# Title: Lyric Opener
# Author: Jess Lonetti
# Purpose: Act as a data handler for main program to obtain lyrics from files
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

import re

class lyricopener:
    def __init__(self,name):
        # names: is a list of strings that correspond with the musician
        # dir: is the file directory path of the data from this file
        # self.listoflyrics: is a list of text
        dir = "../archive/"
        self.lyrics = {}

        self.lyrics=open(dir+name+".txt","r").read()
        self.lyrics=self.clean(self.lyrics)

    def clean(self,passage):
        passage=passage.replace('\t','')
        passage=passage.replace('"','')
        passage=passage.replace('\'','')
        passage=passage.replace(',','')
        passage=passage.replace(':','')
        passage=passage.replace('Mr.','Mr')
        passage=passage.replace('Mrs.','Mrs')
        passage=passage.replace(';','')
        passage=passage.replace('?','')
        passage=passage.replace('!','')
        passage=passage.replace('.','')
        passage=passage.replace('Ms.','Ms')
        passage=re.sub('[[].*[]]','',passage)
        passage=re.sub('[().*[)]','',passage)

        return passage



    def gettext(self):
        return self.lyrics

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"])
    print(lo.gettext())
