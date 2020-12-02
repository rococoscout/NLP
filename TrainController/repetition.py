# Title: Repetition
# Author: Holly Koerwer
# Purpose: produce score for desired musician based on number of repeated lyric lines
#
# ********************************************************************************

from .lyric_opener import Lyricopener
from LanguageModels import *
class Repetition():
    def __init__(self,passage):
        self.passage = passage

    def repeatscore(self):
        linelist = [] # list of total training lines for that musician
        uniquelines = [] # list of unique lines out of total lines for musician
        for sent in self.passage.split("\n"):
            linelist.append(sent)
            if sent not in uniquelines: # only add lyric line to unique list if it has not been seen before
                uniquelines.append(sent)
        # calculate a repeat ratio for each musician text
        # this is the total unique line out of the total lyric lines
        # subtract the calculation from one to get the repeat likelihood, otherwise the ratio is the unique likelihood
        repeatscore = 1 - len(uniquelines) / len(linelist)
        return repeatscore

if __name__ == "__main__":
    lyrics = Lyricopener("adele")
    print(Repetition(lyrics.gettext()).repeatscore())
