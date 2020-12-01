# ********************************************************************************
# Title: TrainController
# Author: Jess Lonetti
# Purpose: create a class for easy to use anaylsis data
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************

from lyric_opener import lyricopener
from repetition import repeatscore
from rhythm import rhymescore
from vocab import vocabscore
from syllable import syllablescore

class TrainController():

    def __init__(self,listofauthors):
        #Dictionary Key are Authors


        lyrics = lyricopener(listofauthors)
        data = lyrics.gettext()

        self.Repition_Score = repeatscore(data)
        # self.Rhythm= rhymescore(data)
        self.Syllable_Score = syllablescore(data)
        self.Vocab = vocabscore(data)

    #Returns a score on how reptitous the text is between 0,1
    def getrep(self):
        return self.Repition_Score
    #Returns dictionary of A,B,C... with list that repersent the line that correspond with the rhyme
    def getrhy(self):
        return self.Rhythm
    #Returns a list; [0] is the line average and [1] is word average syllable
    def getsyl(self):
        return self.Syllable_Score
    #Returns a list of LanguageModels; 0-Unigram 1-BigramSmooth 2-TrigramSmooth
    def getvoc(self):
        return self.Vocab




if __name__ == "__main__":
    trainer = TrainController(["adele"])
    print(trainer.getrep("adele"))
