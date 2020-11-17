# Title: Lyric Opener
# Author: Holly Koerwer
# Purpose: identify pattern training for repetition
#
# ********************************************************************************

from lyric_opener import lyricopener
from LanguageModels import *

# clean up lyrics for processing
def scrubdata(passage):
    passage=passage.replace(')', '')
    passage=passage.replace('(', '')
    passage=passage.replace('\t','')
    passage=passage.replace('"','')
    passage=passage.replace(',','.')
    passage=passage.replace(':','.')
    passage=passage.replace('Mr.','Mr')
    passage=passage.replace('Mrs.','Mrs')
    passage=passage.replace(';','')
    passage=passage.replace('?','.')
    passage=passage.replace('!','.')
    passage=passage.replace('.', '')
    passage=passage.replace('Ms.','Ms')
    return passage

def repeatscore(passage):
    linelist = [] # list of total training lines for that musician
    uniquelines = [] # list of unique lines out of total lines for musician
    for sent in passage.split("\n"):
        linelist.append(sent)
        if sent not in uniquelines: #only add lyric line to unique list if it has not been seen before
            uniquelines.append(sent)
    # calulcate a repeat ratio for each musician text
    # this is the total unique line out of the total lyric lines
    # subtract the calculation from one to get the repeat likelihood, otherwise the ratio is the unique likelihood
    repeatescore = 1 - (len(uniquelines) / len(linelist)
    return repeatscore

if __name__ == "__main__":
    lo = lyricopener(["adele"],"archive/")
    #print(lo.gettext()["adele"])
    lyrics = scrubdata(lo.gettext()["adele"])
    print(repeatscore(lyrics))
