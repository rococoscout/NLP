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


def train(passages):
    '''
    Given a list of passages and their known authors, train your learning model.
    passages: a List of passage pairs (author,text)
    Returns: void
    '''

    trainingtotals["total"]=len(passages)
    for author in passages:
        if passages[author] not in Tsmooth:
            Tsmooth[author]= SmoothedTrigram()
            Bsmooth[author]= SmoothedBigram()
            Unary[author]= UnigramModel()
            trainingtotals[author]=1
        else:
            trainingtotals[author]+=1



        Tsmooth[author].train(passages[author].split("\n"))
        Bsmooth[author].train(passages[author].split("\n"))
        Unary[author].train(passages[author].split("\n"))
        

    pass

if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"],"archive/")
    # print(lo.gettext())
    train(lo.gettext())
