from LanguageModel import LanguageModel
import random


class BigramModel(LanguageModel):

    def __init__(self):
        super().__init__()

        self.biwordcounts = dict()
        self.singlewords = dict()
        self.N = 0

    # REQUIRED FUNCTIONS from abstract parent LanguageModel
    # given list of words, count those words, save counts in dictionary, and youre done
    def train(self, sentences):
        for s in sentences:
            s = s.copy()          # don't want to alter the original given sentences
            s.append(self.STOP)
            previous = self.START #initially the previous word will be the start of sentence symbol
            for w in s:
                bigram = (previous, w)
                if not bigram in self.biwordcounts:
                    self.biwordcounts[bigram] = 1
                else:
                    self.biwordcounts[bigram] += 1
                if not w in self.singlewords:
                    self.singlewords[w] = 1
                elif w in self.singlewords:
                    self.singlewords[w] += 1
                previous = w #make the current word the previous for the next iteration
            self.N += len(s)


    # given a sentence (list of strings) and an index of the word we care about, give probability of word in that sentence
    #need to use counts from train function
    def get_word_probability(self, sentence, index):
        if index == len(sentence):
            return self.get_bigram_probability(sentence[index-1], self.STOP)
        elif index == 0:
            return self.get_bigram_probability(self.START, sentence[index])
        else:
            return self.get_bigram_probability(sentence[index-1], sentence[index])

    #return list of all unique types you get from train
    def get_vocabulary(self):
        self.singlewords["UNK"] = 1
        return self.singlewords

    #make a sentence
    def generate_sentence(self):
        words = []
        words.append(self.START)
        word = self.generate_word(words[len(words)-1])
        while word != self.STOP:
            words.append(word)
            word = self.generate_word(words[len(words)-1])
        words.pop(0)
        return words

    # HELPER FUNCTIONS for this bigram language model

    def get_bigram_probability(self, previous, word):
        bigram = (previous, word)
        if bigram not in self.biwordcounts.keys():
            return 0
        numer = self.biwordcounts[bigram]
        if previous == self.START:
            previous = self.STOP
        if previous not in self.singlewords.keys():
            return 0
        denom = self.singlewords[previous]
        if numer == 0 or denom == 0:
            return 0
        return numer / denom

    def generate_word(self, word):
        threshold = random.uniform(0, 1)
        sum = 0.0
        for w in self.singlewords:
            sum += self.get_bigram_probability(word, w)
            if sum > threshold:
                return w

#
# TESTING ONLY
#
if __name__ == '__main__':
    print('hi!')
