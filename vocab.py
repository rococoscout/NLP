# Title: Vocab tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener
from LanguageModels import *

Tsmooth = {}
Bsmooth = {}
Unary = {}
trainingtotals = {}
trainingtotals["total"]=0

def dirtydata(passage):
    listofsent = []

    passage=passage.replace('\n','')
    passage=passage.replace('\t','')
    passage=passage.replace('"','')
    passage=passage.replace(',','.')
    passage=passage.replace(':','.')
    passage=passage.replace('Mr.','Mr')
    passage=passage.replace('Mrs.','Mrs')
    passage=passage.replace(';','')
    passage=passage.replace('?','.')
    passage=passage.replace('!','.')
    passage=passage.replace('Ms.','Ms')
    for sent in passage.split("."):
        listofsent.append(sent.split())


    return listofsent

def train(passages):
    '''
    Given a list of passages and their known authors, train your learning model.
    passages: a List of passage pairs (author,text)
    Returns: void
    '''
    trainingtotals["total"]=len(passages)
    for passage in passages:
        if passage[0] not in Tsmooth:
            Tsmooth[passage[0]]= SmoothedTrigram()
            Bsmooth[passage[0]]= SmoothedBigram()
            Unary[passage[0]]= UnigramModel()
            trainingtotals[passage[0]]=1
        else:
            trainingtotals[passage[0]]+=1



        cleandata=dirtydata(passage[1])
        Tsmooth[passage[0]].train(cleandata)
        Bsmooth[passage[0]].train(cleandata)
        Unary[passage[0]].train(cleandata)

    pass

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"],"archive/")
    print(lo.gettext())
    train(lo.gettext())
