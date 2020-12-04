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
import copy
from termcolor import colored, cprint
import re

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
        verse1=self.postproduction(verse1)
        verse2=self.postproduction(verse2)
        verse3=self.postproduction(verse3)
        chorus=self.postproduction(chorus)
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
    def postproduction(self, passage):
        # rerange Repeats
        line_prob = self.trainer.getrepstruct()
        line_prob=dict(sorted(line_prob.items(), key=lambda item: item[1]))
        listofrepeated = list()
        listofunique = list()
        counter = 0
        # finds repeated lines
        for line in passage:
            if line in listofunique:
                listofrepeated.append(counter)
            else:
                listofunique.append(line)
            counter+=1
        list_repeated_copy = copy.deepcopy(listofrepeated)
        # switches repeated lines with most popular repeated line structure from artist
        for order in reversed(line_prob):
            if not listofrepeated:
                break

            if random.random()<.6:
                continue

            if order in range(len(passage)):
                place=listofrepeated.pop()
                temp = passage[order]
                passage[order] = passage[place]
                passage[place] = temp

        rhyhme_prob = self.trainer.Rhythm.getprob()
        rhyhme_struct = self.trainer.Rhythm.getstruct()
        list_tochange = []
        counter = int(rhyhme_prob*len(passage))

        for order in reversed(rhyhme_struct):
            if order in listofrepeated:
                continue
            if counter == 0:
                break
            if order in range(len(passage)):
                list_tochange.append(order)

            counter -= 1

            # RHYME FUN! many try catches because I dont have access to the library used for rhyme
        while(1):
            first_loc=list_tochange.pop()
            if not list_tochange:
                break
            sec_loc = list_tochange.pop()
            if not list_tochange:
                break
            first_lword = passage[first_loc].split()[len(passage[first_loc].split())-1]
            second_lword =  passage[sec_loc].split()[len(passage[sec_loc].split())-1]
            dict_of_rhymes = {}
            num_of_slword = 3
            flag = True
            sent = []
            try:
                dict_of_rhymes = self.trainer.Rhythm.get_otherwords(first_lword)
                sent=passage[sec_loc].split()
            except:
                flag = False
                try:
                    dict_of_rhymes = self.trainer.Rhythm.get_otherwords(second_lword)
                    sent=passage[first_loc].split()
                except:
                    continue
            if flag:
                try:
                    num_of_slword = self.trainer.Syllable.syllablecount(second_lword)
                except:
                    continue
            else:
                try:
                    num_of_slword = self.trainer.Syllable.syllablecount(first_lword)
                except:
                    continue

            newword = ""

            for i in range(10):
                try:
                    newword = dict_of_rhymes[num_of_slword][random.randint(0,len(dict_of_rhymes[num_of_slword]))]
                except:
                    num = random.choice(list(dict_of_rhymes))
                    num2 = random.randint(0,len(dict_of_rhymes[num])-1)
                    newword = dict_of_rhymes[num][num2]

                if newword in self.models[1].vocab:
                    break

            newword = re.sub('[().*[)]','',newword)
            sent.pop()
            sent.append(newword)
            if flag:
                passage[sec_loc] = " ".join(sent)
            else:
                passage[first_loc] = " ".join(sent)

        return passage


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
