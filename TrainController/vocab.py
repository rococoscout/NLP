# Title: Vocab tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener
from LanguageModels import *

def vocabscore(passage):
    Tsmooth = SmoothedTrigram()
    Bsmooth = SmoothedBigram()
    Unary = UnigramModel()
    Tsmooth.train(passage.split("\n"))
    Bsmooth.train(passage.split("\n"))
    Unary.train(passage.split("\n"))
    return [Unary,Bsmooth,Tsmooth]



if __name__ == "__main__":
    lo = lyricopener(["adele","al-green"])
    # print(lo.gettext())
    vocabscore(lo.gettext()["adele"])
