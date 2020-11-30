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


class Generator():

    def __init__(self,phrase,artist):
        # user input determines author
        self.phrase = phrase
        print(artist)
        artstring = artist[0]
        self.artist = artist
        self.trainer = TrainController(artist)
        self.models = self.trainer.getvoc(artstring)
        self.vocab = self.models[0].wordcounts # Dictionary
        self.repetition = self.trainer.getrep(artstring)
        self.syllable = self.trainer.getsyl(artstring)[0]
        # self.models[1].train(paragrahp)


    def generate_song(self):
        verse1 = self.make_verse()
        verse2 = self.make_verse()
        verse3 = self.make_verse()
        chorus = self.make_chorus()
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

    def make_verse(self):
        # each line generated will have a probability of repeating based off of self.repetition score
        verse = []
        verse.append(self.generate_line(self.syllable+random.randint(-2,2)))
        lines = random.randint(4, 6)
        for i in range(lines):
            if self.repetition-(self.repetition * .8) > random.random():
                verse.append(verse[len(verse)-1])
            else:
                verse.append(self.generate_line(self.syllable+random.randint(-2,2)))


        return verse

    def make_chorus(self):
        chorus = []
        chorus.append(self.generate_line(self.syllable))
        for i in range(5):
            if self.repetition-(self.repetition * .4) > random.random():
                chorus.append(chorus[len(chorus)-1])
            else:
                chorus.append(self.generate_line(self.syllable))
        return chorus

    def generate_line(self,syllable_modified):
        # check self.syllable average is within verse threshold before confirming line
        line = ["<S>"]
        endtag = "</S>"
        counter=0
        for word in line:
            prevword=self.models[1].generate_word(word)
            while prevword == endtag:
                prevword=self.models[1].generate_word(word)

            line.append(prevword)
            #print(self.syllables.estimate(line[len(line)-1]))
            counter+=syllables.estimate(line[len(line)-1])
            if syllable_modified <= counter:
                break;


        return " ".join(line[1:])

    def modify_rythm(self,stanza):
        # function finds wich lines repeated

        # rerange repeated lines for key points

        # function finds wich lines rhyme

        # make a function that artifically rhymes

        return


if __name__ == "__main__":
    #print(generate_line(self.trainer.getsyl(artstring)[0]+random.randint(-2,2)))
    # print("VERSE")
    # print("\n".join(make_verse(self.trainer.getrep(artstring), self.trainer.getsyl(artstring)[0])))
    # print("CHORUS")
    # print("\n".join(make_chorus(self.trainer.getrep(artstring), self.trainer.getsyl(artstring)[0])))
    gen=Generator("words", ["adele"])
    print("\n".join(gen.generate_song()))
