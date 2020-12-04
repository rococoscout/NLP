# Title: Rhythm tally
# Author: Jess Lonetti
# Purpose: identify meta data for rhythm
#
# Contact Information: rococoscout@gmail.com
# Credit: Phyme
# ********************************************************************************

from .lyric_opener import Lyricopener
from Phyme import Phyme

class Rhythm():
    def __init__(self,passage):
        self.ph = Phyme()
        self.passage = passage
        self.rhymescore()
        self.rhymeprob
        self.rhymestruct

    def getprob(self):
        return self.rhymeprob

    def getstruct(self):
        return self.rhymestruct

    def get_otherwords(self,word):
        return self.ph.get_perfect_rhymes(word)

    def rhymeword(self,word1,word2):
        try:
            rhymelist=self.ph.get_perfect_rhymes(word1)
        except:
            return False

        for syll in rhymelist:
            if word2 in rhymelist[syll]:
                return True

        return False

    def toplisttomod(self,powerlist):
        sorteddict = {}
        total = 0
        mod = 7
        for item in powerlist:
            if not item%mod in sorteddict.keys():
                sorteddict[item%mod] = 1
            else:
                sorteddict[item%mod]+= 1

            total += 1
        for i in sorteddict:
            sorteddict[i] = sorteddict[i]/total

        return sorteddict

    def rhymescore(self):
        initialDict = {}
        finalDict = {}
        lineon = 0
        lastwords = list()
        for line in self.passage.split('\n'):
            listofwords = line.split()
            if listofwords:
                # print(len(listofwords)-1)
                lastwords.append(listofwords[len(listofwords)-1])

        numbersused = list()

        for num in range(len(lastwords)):
            if num in numbersused:
                continue
            finalDict[num] = list()
            numbersused.append(num)
            for num2 in range(len(lastwords)):
                if num2 in numbersused:
                    continue

                if self.rhymeword(lastwords[num],lastwords[num2]):
                    finalDict[num].append(num2)
                    numbersused.append(num2)
        top1 = 0
        top1list = list()

        nonrhyme = 0
        for i in finalDict:
            if finalDict[i]:
                if len(finalDict[i])>top1:
                    top1 = len(finalDict[i])
                    top1list = finalDict[i]
            else:
                nonrhyme +=1



        self.rhymeprob = 1-nonrhyme/len(lastwords)

        self.rhymestruct=self.toplisttomod(top1list)




if __name__ == "__main__":
    lo = lyricopener("adele")
    rh = Rhythm(lo.gettext())
    print(rh.rhymescore())
    print(rh.rhymeword("ever","never"))
