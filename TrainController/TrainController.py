# ********************************************************************************
# Title: TrainController
# Author: Jess Lonetti
# Purpose: create a class for easy to use anaylsis data
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from .lyric_opener import Lyricopener
from .repetition import Repetition
from .vocab import Vocab
from .rhythm import Rhythm
from .syllable import Syllable

class TrainController():

    def __init__(self,author):
        #Dictionary Key are Authors


        lyrics = Lyricopener(author)
        data = lyrics.gettext()

        self.Repition = Repetition(data)
        self.Rhythm= Rhythm(data)
        self.Syllable = Syllable(data)
        self.Vocab = Vocab(data).vocabscore()

    #Returns a score on how reptitous the text is between 0,1
    def getrep(self):
        return self.Repition.getscore()
    #Returns a dict of the popular places a repetition occurs
    def getrepstruct(self):
        return self.Repition.getstruct()

    #Returns a prob of how much rhyming is in an artist lyrics
    def getrhy(self):
        return self.Rhythm.getprob()
    #Returns the popular places a artist rhyhmes
    def getrhystruct(self):
        return self.Rhythm.getstruct()

    #Returns dictionary of A,B,C... with list that repersent the line that correspond with the rhyme
    def getrhy(self):
        return self.Rhythm
    #Returns a list; [0] is the line average and [1] is word average syllable
    def getsyl(self):
        return self.Syllable.syllablescore()
    #Returns a list of LanguageModels; 0-Unigram 1-BigramSmooth 2-TrigramSmooth
    def getvoc(self):
        return self.Vocab




if __name__ == "__main__":
    trainer = TrainController("adele")
    print(trainer.getrep())
