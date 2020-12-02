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
import random
import time
from termcolor import colored, cprint


class Generator():

    def __init__(self,phrase,artist,threshold):
        # user input determines author
        self.artist = artist
        self.trainer = TrainController(artist)
        self.models = self.trainer.getvoc()
        self.vocab = self.models[0].wordcounts # Dictionary
        self.phrase = phrase.lower()
        # print(self.vocab)
        # self.models[1].train(paragraph)
        self.generateVec(threshold)


    def generate_song(self):
        verse1 = self.make_verse(self.trainer.getrep(), self.trainer.getsyl()[0])
        verse2 = self.make_verse(self.trainer.getrep(), self.trainer.getsyl()[0])
        verse3 = self.make_verse(self.trainer.getrep(), self.trainer.getsyl()[0])
        chorus = self.make_chorus(self.trainer.getrep(), self.trainer.getsyl()[0])
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


    def make_verse(self,repetition, syllable):
        # each line generated will have a probability of repeating based off of repetition score
        verse = []
        verse.append(self.generate_line(syllable+random.randint(-2,2)))
        for i in range(random.randint(4, 6)):
            if repetition-(repetition * .8) > random.random():
                verse.append(verse[len(verse)-1])
            else:
                verse.append(self.generate_line(syllable+random.randint(-2,2)))
        return verse

    def make_chorus(self,repetition, syllable):
        chorus = []
        chorus.append(self.generate_line(syllable))
        for i in range(5):
            if repetition-(repetition * .4) > random.random():
                chorus.append(chorus[len(chorus)-1])
            else:
                chorus.append(self.generate_line(syllable))
        return chorus

    def generate_line(self,syllable):
        # check syllable average is within verse threshold before confirming line
        line = ["<S>"]
        endtag = "</S>"
        counter=0
        for word in line:
            prevword=self.models[1].generate_word(word)
            while prevword == endtag:
                prevword=self.models[1].generate_word(word)

            line.append(prevword)
            #print(syllables.estimate(line[len(line)-1]))
            counter+=syllables.estimate(line[len(line)-1])
            if syllable <= counter:
                break;


        return " ".join(line[1:])

    def generateVec(self,threshold):
        wordVecList = []
        fillerList = ["the","of","to","and","a","in","is","it","you","that","he","was",
        "for","on","are","with","as","I","his","they","be","at","one","have","this","from",
        "or","had","by","not","word","but","what","some","we","can","out","other","were",
        "all","there","when","up","use","your","how","said","an","each","she"]

        embeds = api.load("glove-wiki-gigaword-50") # 66MB
        userDict = {}
        vec = embeds[self.phrase]
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
        self.models[1].train(oneList)
        # print(vocabscore"\n".join(oneList))

    # Function: Post Production
    # Input: Passage of length up to 10 lines
    # Output: Same Passage but reranged to fit the artist style
    #
    def postproduction():
            return


if __name__ == "__main__":
    # text = colored("Welcome to Jolly Records (where anyone can be a musician)!", 'green', 'on_red', attrs=['reverse', 'blink'])
    cprint("Welcome to Jolly Records (where anyone can be a musician)!", 'yellow', attrs=['bold'])
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
    gen=Generator(line,musician,threshold)
    gen.generate_song()
