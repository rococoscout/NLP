# Title: Generate the Song
# Author: Jess Lonetti/Holly Koerwer
# Purpose: Generate song based on dataset statistics
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************


def generate_song(phrase,artist):
    
    return


def generate_structure(rhythm, repetition, syllable):
    # will structure output of song
    # structure will be verse, chorus, verse, chorus
    # structure will be based off of rhythm, repetition, & syllable score
    verse1 = make_verse(repetition, syllable)
    chorus = make_chorus(repetition, syllable)
    verse2 = make_verse(repetition, syllable)
    
    return

def make_verse(repetition, syllable):
    # each line generated will have a probability of repeating based off of repetition score
    verse = []
    line1 = generate_line_verse(syllable)
    line2 = generate_line_verse(syllable)
    line3 = generate_line_verse(syllable)
    line4 = generate_line_verse(syllable)
    verse.append(line1)
    verse.append(line2)
    verse.append(line3)
    verse.append(line4)
    return verse

def make_chorus(repetition, syllable):
    chorus = []
    line1 = generate_line_chorus(syllable)
    line2 = generate_line_chorus(syllable)
    line3 = generate_line_chorus(syllable)
    line4 = generate_line_chorus(syllable)
    line5 = generate_line_chorus(syllable)
    line6 = generate_line_chorus(syllable)
    chorus.append(line1)
    chorus.append(line2)
    chorus.append(line3)
    chorus.append(line4)
    chorus.append(line5)
    chorus.append(line6)
    return chorus
    
def generate_line_verse(syllable):
    # check syllable average is within verse threshold before confirming line
    return

def generate_line_chorus(syllable):
    # check syllable average is within chorus threshold before confirming line
    return


if __name__ == "__main__":
    print("success")
