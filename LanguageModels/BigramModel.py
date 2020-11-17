from .LanguageModel import LanguageModel
import random


class BigramModel(LanguageModel):

    def __init__(self):
        super().__init__()
        self.wordcounts = dict()
        self.vocab = dict()
        self.vocab[self.START] = 0
        self.vocab[self.STOP] = 0
        self.N = 0
    # REQUIRED FUNCTIONS from abstract parent LanguageModel

    def train(self, sentences):
        for s in sentences:
            bs = s.split()
            bs.append(self.STOP)
            bs.insert(0,self.START)

            for w in range(len(bs)-1):
                bigram = bs[w]+" "+bs[w+1]

                if not bs[w] in self.wordcounts:
                    self.wordcounts[bs[w]] = 1
                    self.vocab[bs[w]]= 1
                else:
                    self.wordcounts[bs[w]] += 1

                if not bigram in self.wordcounts:
                    self.wordcounts[bigram] = 1
                else:
                    self.wordcounts[bigram] += 1


            self.N += len(bs)-1

        return

    def get_word_probability(self, sentence, index):
        # print(sentence)
        bs = sentence.copy()
        bs.insert(0,self.START)
        return self.get_bigram_probability(bs[index]+" "+bs[index+1],bs[index])


    def get_vocabulary(self):
        words = list(self.vocab.keys())
        return words

    def generate_sentence(self):
        words = []
        word = self.START
        while word != self.STOP:
            words.append(word)
            word = self.generate_word(words[len(words)-1])
        return words

    def generate_word(self,word):
        threshold = random.uniform(0, 1)
        sum = 0.0

        for w in self.vocab.keys():
            # print(threshold)
            sum += self.get_bigram_probability(word+" "+w,word)
            if sum > threshold:
                return w

    def get_bigram_probability(self,bigram,unigram):
        # print(bigram+"\t"+unigram)

        if not bigram in self.wordcounts:
            return 0
        else:
            return self.wordcounts[bigram] / self.wordcounts[unigram]

#
# TESTING ONLY
#
if __name__ == '__main__':
    print('hi!')
