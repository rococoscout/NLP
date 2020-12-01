# Title: Generate the Song
# Author: Jess Lonetti/Holly Koerwer
# Purpose: Generate song based on dataset statistics
#
# Contact Information: rococoscout@gmail.com
# ********************************************************************************
import syllables
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec
from TrainController import TrainController
from TrainController import lyricopener
import random
<<<<<<< HEAD
import time
from termcolor import colored, cprint
# user input determines author
artist = ["adele"]
artstring = "adele"
trainer = TrainController(artist)
models = trainer.getvoc(artstring)
vocab = models[0].wordcounts # Dictionary
# print(vocab)
# models[1].train(paragraph)
wordVecList = []
fillerList = ["the","of","to","and","a","in","is","it","you","that","he","was",
"for","on","are","with","as","I","his","they","be","at","one","have","this","from",
"or","had","by","not","word","but","what","some","we","can","out","other","were",
"all","there","when","up","use","your","how","said","an","each","she"]

embeds = api.load("glove-wiki-gigaword-50") # 66MB
userDict = {}

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
    cprint("[VERSE 1]", 'yellow')
    cprint(verse1, 'cyan', attrs=['bold'])
    cprint("[CHORUS]", 'yellow')
    cprint(chorus, 'cyan', attrs=['bold'])
    cprint("[VERSE 2]", 'yellow')
    cprint(verse2, 'cyan', attrs=['bold'])
    cprint("[CHORUS]", 'yellow')
    cprint(chorus, 'cyan', attrs=['bold'])
    cprint("[VERSE 3]", 'yellow')
    cprint(verse3, 'cyan', attrs=['bold'])


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
=======


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
>>>>>>> a13662b9a85559652a2dbdb201dc1354d77ea05f

def generateVec(word, threshold):

    vec = embeds[word]
    sims = embeds.similar_by_vector(vec)
    # file = open("filler.txt", 'w')
    for i in range(0, 10):
        wordVecList.append(sims[i][0])
    oneList = []
    for i in range(0, int((int(threshold) / 100) * 500)):
        line =[]
        for ii in range(0, 7):
            line.append(fillerList[random.randint(0, len(fillerList)-1)])
            line.append(wordVecList[random.randint(0,9)])
        oneList.append(" ".join(line))

    # print(oneList)
    models[1].train(oneList)
    # print(vocabscore"\n".join(oneList))

# def CountFrequency(my_list):
#
#     # Creating an empty dictionary
#     freq = {}
#     for items in my_list:
#         freq[items] = my_list.count(items)
#     return freq


if __name__ == "__main__":
<<<<<<< HEAD
    # text = colored("Welcome to Jolly Records (where anyone can be a musician)!", 'green', 'on_red', attrs=['reverse', 'blink'])
    cprint("Welcome to Jolly Records (where anyone can be a musician)!", 'yellow', attrs=['bold'])
    # print(text)
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    print(" ")
    line = input('Pick one word to be the theme of your song:  ')
    threshold = input('How biased toward that theme do you want the song to be? (percentage 1-100): ')
    musician = input('Tell us a popular artist who you would like to sound like: ')
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    print(" ")
    generateVec(line, threshold)
    print(wordVecList)
    generate_song("words", "adele")
=======
    #print(generate_line(self.trainer.getsyl(artstring)[0]+random.randint(-2,2)))
    # print("VERSE")
    # print("\n".join(make_verse(self.trainer.getrep(artstring), self.trainer.getsyl(artstring)[0])))
    # print("CHORUS")
    # print("\n".join(make_chorus(self.trainer.getrep(artstring), self.trainer.getsyl(artstring)[0])))
    gen=Generator("words", ["adele"])
    print("\n".join(gen.generate_song()))
>>>>>>> a13662b9a85559652a2dbdb201dc1354d77ea05f
