# Title: Generate the Song
# Author: Jess Lonetti/Holly Koerwer
# Purpose: Generate song based on dataset statistics
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************
import syllables
from TrainController import TrainController
from TrainController import lyricopener
import random
# user input determines author
artist = ["adele"]
artstring = "adele"
trainer = TrainController(artist)
models = trainer.getvoc(artstring)
vocab = models[0].wordcounts # Dictionary


def generate_song(phrase,artist):

    return

def make_verse(repetition, syllable):
    # each line generated will have a probability of repeating based off of repetition score
    verse = []
    verse.append(generate_line(syllable+random.randint(-2,2)))
    for i in range(random.randint(4, 6)):
        if repetition-(repetition * .5) > random.random():
            verse.append(verse[len(verse)-1])
        else:
            verse.append(generate_line(syllable+random.randint(-2,2)))
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

def generate_line(syllable):
    # check syllable average is within verse threshold before confirming line
    line = ["<S>"]
    endtag = "</S>"
    counter=0
    for word in line:
        prevword=models[1].generate_word(word)
        while prevword == endtag:
            prevword=models[1].generate_word(word)

        line.append(prevword)
        #print(syllables.estimate(line[len(line)-1]))
        counter+=syllables.estimate(line[len(line)-1])
        if syllable <= counter:
            break;


    return " ".join(line[1:])


if __name__ == "__main__":
    #print(generate_line(trainer.getsyl(artstring)[0]+random.randint(-2,2)))
    print("\n".join(make_verse(trainer.getrep(artstring), trainer.getsyl(artstring)[0])))
