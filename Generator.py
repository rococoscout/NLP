# Title: Generate the Song
# Author: Jess Lonetti/Holly Koerwer
# Purpose: Generate song based on dataset statistics
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************
import syllables
from TrainController import TrainController
from TrainController import lyricopener
# user input determines author
artist = ["adele"]
trainer = TrainController(artist)
models = trainer.getvoc(artist)
vocab = models[0].wordcounts # Dictionary


def generate_song(phrase,artist):

    return


def generate_structure(rhythm, repetition, syllable):
    # will structure output of song
    # structure will be verse, chorus, verse, chorus
    # structure will be based off of rhythm, repetition, & syllable score
    verse1 = make_verse(rhythm, repetition, syllable)
    chorus = make_chorus(rhythm, repetition, syllable)
    verse2 = make_verse(rhythm, repetition, syllable)

    return

def make_verse(rhythm, repetition, syllable):
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
    line = ["<S>"]
    counter=0
    for word in line:
        line.append(models[1].generate_word(word))
        counter+=syllabes.estimate(line[len(line)-1])
        if syllable <= counter:
            break;

    return "".join(line[1:])

def generate_line_chorus(syllable):
    # check syllable average is within chorus threshold before confirming line
    return


if __name__ == "__main__":
    print(generate_line_verse(trainer.getsyl()))
