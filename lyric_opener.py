# ********************************************************************************
# Title: Lyric Opener
# Author: Jess Lonetti
# Purpose: Act as a data handler for main program to obtain lyrics from files
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

import re

class lyricopener:
    def __init__(self,names,dir):
        # names: is a list of strings that correspond with the musician
        # dir: is the file directory path of the data from this file
        # self.listoflyrics: is a list of text
        self.listoflyrics = {}
        for name in names:
            self.listoflyrics[name]=open(dir+name+".txt","r").read()
            self.listoflyrics[name]=self.clean(self.listoflyrics[name])

    def clean(self,passage):
        passage=passage.replace('\t','')
        passage=passage.replace('"','')
        passage=passage.replace(',','')
        passage=passage.replace(':','')
        passage=passage.replace('Mr.','Mr')
        passage=passage.replace('Mrs.','Mrs')
        passage=passage.replace(';','')
        passage=passage.replace('?','')
        passage=passage.replace('!','')
        passage=passage.replace('Ms.','Ms')
        passage=re.sub('[[].*[]]','',passage)
        return passage



    def gettext(self):
        return self.listoflyrics

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"],"archive/")
    print(lo.gettext())
