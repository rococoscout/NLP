from BigramModel import BigramModel

class SmoothedBigram(BigramModel):   # inherit all the BigramModel goodies from Part 1

    def __init__(self):
        super().__init__()           # calls your parent's init function
        self.V = len(self.get_vocabulary())

    def get_bigram_probability(self, previous, word):
        self.V = len(self.singlewords)
        k = .001
        bigram = (previous, word)
        if bigram not in self.biwordcounts.keys():
            numer = k
        else:
            numer = self.biwordcounts[bigram] + k
        if previous == self.START:
            previous = self.STOP
        if previous not in self.singlewords.keys():
            denom = self.V*k
        else:
            denom = self.singlewords[previous] + (self.V*k)
        if numer == 0 or denom == 0:
            return k / (self.V*k)
        return numer / denom
