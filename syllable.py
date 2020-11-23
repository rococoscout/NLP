# Title: Syllable
# Author: Holly Koerwer
# Purpose: produce a syllable score for the desired musician, score will be average syllables per line and per word
# Sources used: https://pypi.org/project/syllables/
#
# ********************************************************************************

from lyric_opener import lyricopener
from LanguageModels import *
import syllables

def syllablescore(passage):
    line_total_syllable  = []
    for line in passage.split("\n"):
        line_syllable_total = syllables.estimate(line)
        line_word_count = 0
        for word in line.split(' '):
            line_word_count += 1
        line_total_syllable.append((line_syllable_total, line_word_count))

    average_syllable_byword = 0 # number of syllables in each line / number of words in each line
    average_syllable_byline = 0 # number of syllables in each line
    for line in line_total_syllable:
        average_syllables = line[0] / line[1]
        average_syllable_byword = average_syllable_byword + average_syllables
        average_syllable_byline = average_syllable_byline + line[0]

    final_average_byword = average_syllable_byword / len(line_total_syllable)
    final_average_byline = average_syllable_byline / len(line_total_syllable)
    
    # final score output contains syllable average by line and syllable average by word
    return (final_average_byline, final_average_byword)



if __name__ == "__main__":
    lyrics = lyricopener(["adele"],"archive/")
    print("line syllable average: ", syllablescore(lyrics.gettext()["adele"])[0], "word syllable average: ", syllablescore(lyrics.gettext()["adele"])[1])
