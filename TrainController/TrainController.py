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
        self.Repition_Score = {}
        self.Rhythm = {}
        self.Syllable_Score = {}
        self.Vocab = {}


        lyrics = lyricopener(listofauthors)
        data = lyrics.gettext()
        for author in data:
            self.Repition_Score[author] = repeatscore(data[author])
            self.Rhythm[author] = rhymescore(data[author])
            self.Syllable_Score[author] = syllablescore(data[author])
            self.Vocab[author] = vocabscore(data[author])

    #Returns a score on how reptitous the text is between 0,1
    def getrep(self,author):
        return self.Repition_Score[author]
    #Returns dictionary of A,B,C... with list that repersent the line that correspond with the rhyme
    def getrhy(self,author):
        return self.Rhythm[author]
    #Returns a list; [0] is the line average and [1] is word average syllable
    def getsyl(self,author):
        return self.Syllable_Score[author]
    #Returns a list of LanguageModels; 0-Unigram 1-BigramSmooth 2-TrigramSmooth
    def getvoc(self,author):
        return self.Vocab[author]




if __name__ == "__main__":
    trainer = TrainController(["adele"])
    print(trainer.getrep("adele"))
