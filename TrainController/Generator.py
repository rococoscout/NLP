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
    verse1 = make_verse(trainer.getrep(artstring), trainer.getsyl(artstring)[0])
    verse2 = make_verse(trainer.getrep(artstring), trainer.getsyl(artstring)[0])
    verse3 = make_verse(trainer.getrep(artstring), trainer.getsyl(artstring)[0])
    chorus = make_chorus(trainer.getrep(artstring), trainer.getsyl(artstring)[0])
    song = []
    verse1 = "\n".join(verse1)
    verse2 = "\n".join(verse2)
    verse3 = "\n".join(verse3)
    chorus = "\n".join(chorus)
    song.append("[VERSE 1]")
    song.append(verse1)
    song.append("[CHORUS]")
    song.append(chorus)
    song.append("[VERSE 2]")
    song.append(verse2)
    song.append("[CHORUS]")
    song.append(chorus)
    song.append("[VERSE 3]")
    song.append(verse3)
    return song

def make_verse(repetition, syllable):
    # each line generated will have a probability of repeating based off of repetition score
    verse = []
    verse.append(generate_line(syllable+random.randint(-2,2)))
    for i in range(random.randint(4, 6)):
        if repetition-(repetition * .8) > random.random():
            verse.append(verse[len(verse)-1])
        else:
            verse.append(generate_line(syllable+random.randint(-2,2)))
    return verse

def make_chorus(repetition, syllable):
    chorus = []
    chorus.append(generate_line(syllable))
    for i in range(5):
        if repetition-(repetition * .4) > random.random():
            chorus.append(chorus[len(chorus)-1])
        else:
            chorus.append(generate_line(syllable))
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
    # print("VERSE")
    # print("\n".join(make_verse(trainer.getrep(artstring), trainer.getsyl(artstring)[0])))
    # print("CHORUS")
    # print("\n".join(make_chorus(trainer.getrep(artstring), trainer.getsyl(artstring)[0])))
    print("\n".join(generate_song("words", "adele")))
<<<<<<< HEAD
=======

>>>>>>> 36721f6aefb84622ecd25049e0b82b13bdfc789f
