# Title: Lyric Opener
# Author: Holly Koerwer
# Purpose: identify pattern training for repetition
#
# ********************************************************************************

from lyric_opener import lyricopener
from LanguageModels import *
from syllables import syllables

def syllablescore(passage):
    line_total_syllable  = []
    for sent in passage.split("\n"):
        sentence_syllable_total = 0
        sentence_word_count = 0
        for word in sent:
            sentence_word_count += 1
            sentence_syllable_total = sentence_syllable_total + syllables.estimate(word)
        line_total_syllable.append((sentence_syllable_total, sentence_word_count))

    average_syllable_total = 0
    for line in line_total_syllable:
        average_syllables = line[0] / line[1]
        average_syllable_total = average_syllable_total + average_syllables

    final_average = average_syllable_total / len(line_total_syllable)
    return final_average



if __name__ == "__main__":
    lyrics = lyricopener(["adele"],"archive/")
    #print(lo.gettext()["adele"])
    print(syllablescore(lyrics.gettext()["adele"]))
