# Title: Vocab tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from .lyric_opener import Lyricopener
from .LanguageModels import *

class Vocab():
    def __init__(self,passage):
        self.passage = passage

    def vocabscore(self):
        Tsmooth = SmoothedTrigram()
        Bsmooth = SmoothedBigram()
        Unary = UnigramModel()
        Tsmooth.train(self.passage.split("\n"))
        Bsmooth.train(self.passage.split("\n"))
        Unary.train(self.passage.split("\n"))
        # print("passage: ", passage)
        return [Unary,Bsmooth,Tsmooth]



if __name__ == "__main__":
    lo = Lyricopener("adele")
    # print(lo.gettext())
    print(Vocab(lo.gettext()).vocabscore())
