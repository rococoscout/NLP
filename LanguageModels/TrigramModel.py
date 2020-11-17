from .LanguageModel import LanguageModel
import random


class TrigramModel(LanguageModel):

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
            ts = s.split()
            ts.append(self.STOP)
            ts.insert(0,self.START)
            ts.insert(0,self.START)
            # print(ts)
            for w in range(len(ts)-2):

                bigram = ts[w]+" "+ts[w+1]




                trigram = ts[w]+" "+ts[w+1]+" "+ts[w+2]

                if w == len(ts)-3:
                    if not ts[w+1] in self.vocab:
                        self.vocab[ts[w+1]]= 1

                if not ts[w] in self.vocab:
                    self.vocab[ts[w]]= 1

                if not bigram in self.wordcounts:
                    self.wordcounts[bigram] = 1
                else:
                    self.wordcounts[bigram] += 1

                if not trigram in self.wordcounts:
                    self.wordcounts[trigram] = 1
                else:
                    self.wordcounts[trigram] += 1


            self.N += len(ts)-1

        return


    def get_word_probability(self, sentence, index):
        ts = sentence.copy()
        ts.insert(0,self.START)
        ts.insert(0,self.START)
        return self.get_trigram_probability(ts[index]+" "+ts[index+1]+" "+ts[index+2],ts[index]+" "+ts[index+1])

    def get_vocabulary(self):
        words = list(self.vocab.keys())
        return words

    def generate_sentence(self):
        words = []
        words.append(self.START)
        word = self.START
        while word != self.STOP:
            words.append(word)
            word = self.generate_word(words[len(words)-2]+" "+words[len(words)-1])
        return words

    def generate_word(self,bigram):
        threshold = random.uniform(0, 1)
        sum = 0.0

        for w in self.vocab.keys():
            sum += self.get_trigram_probability(bigram+" "+w,bigram)
            if sum > threshold:
                return w

    def get_trigram_probability(self,trigram,bigram):

        if not trigram in self.wordcounts:
            return 0
        else:
            # print(trigram+"\t"+bigram)
            # print(self.wordcounts[trigram],self.wordcounts[bigram])
            return self.wordcounts[trigram] / self.wordcounts[bigram]
#
# TESTING ONLY
#
if __name__ == '__main__':
    print('hi!')
