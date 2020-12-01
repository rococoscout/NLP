from LanguageModel import LanguageModel
import random


class TrigramModel(LanguageModel):

    def __init__(self):
        super().__init__()

        self.triwordcounts = dict()
        self.biwordcounts = dict()
        self.singlewords = dict()
        self.N = 0
    # REQUIRED FUNCTIONS from abstract parent LanguageModel

    def train(self, sentences):
        for s in sentences:
            s = s.copy()          # don't want to alter the original given sentences
            s.append(self.STOP)
            previous1 = self.START #initially the previous word will be the start of sentence symbol
            previous2 = self.START
            for w in s:
                trigram = (previous1, previous2, w)
                bigram = (previous2, w)
                if not bigram in self.biwordcounts:
                    self.biwordcounts[bigram] = 1
                else:
                    self.biwordcounts[bigram] += 1
                if not trigram in self.triwordcounts:
                    self.triwordcounts[trigram] = 1
                else:
                    self.triwordcounts[trigram] += 1
                if not w in self.singlewords:
                    self.singlewords[w] = 1
                elif w in self.singlewords:
                    self.singlewords[w] += 1
                previous1 = previous2
                previous2 = w #make the current word the previous for the next iteration
            self.N += len(s)


    def get_word_probability(self, sentence, index):
        if index == len(sentence):
            bigram = (sentence[index-2], sentence[index-1])
            return self.get_trigram_probability(bigram, self.STOP)
        elif index == 0:
            bigram = (self.START, self.START)
            return self.get_trigram_probability(bigram, sentence[index])
        elif index == 1:
            bigram = (self.START, sentence[index-1])
            return self.get_trigram_probability(bigram, sentence[index])
        else:
            bigram = (sentence[index-2], sentence[index-1])
            return self.get_trigram_probability(bigram, sentence[index])

    def get_vocabulary(self):
        self.singlewords["UNK"] = 1
        return self.singlewords

    def generate_sentence(self):
        words = []
        words.append(self.START)
        words.append(self.START)
        bigram = (words[len(words)-2], words[len(words)-1])
        word = self.generate_word(bigram)
        while word != self.STOP:
            words.append(word)
            bigram = (words[len(words)-2], words[len(words)-1])
            word = self.generate_word(bigram)
        words.pop(0)
        words.pop(0)
        return words

    def get_trigram_probability(self, bigram, word):
        previous1 = bigram[0]
        previous2 = bigram[1]
        trigram = (previous1, previous2, word)
        if trigram not in self.triwordcounts.keys():
            return 0
        numer = self.triwordcounts[trigram]
        if previous2 == self.START and previous1 == self.START:
            #make count equal to number of sentences
            denom = self.singlewords[self.STOP]
            return numer / denom
        if bigram not in self.biwordcounts.keys():
            return 0
        else:
            denom = self.biwordcounts[bigram]
        if numer == 0 or denom == 0:
            return 0
        return numer / denom

    def generate_word(self, bigram):
        threshold = random.uniform(0, 1)
        sum = 0.0
        for w in self.singlewords:

            sum += self.get_trigram_probability(bigram, w)
            if sum > threshold:
                return w

#
# TESTING ONLY
#
if __name__ == '__main__':
    print('hi!')
