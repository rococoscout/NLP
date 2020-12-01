from TrigramModel import TrigramModel

class SmoothedTrigram(TrigramModel):   # inherit all the BigramModel goodies from Part 1

    def __init__(self):
        super().__init__()           # calls your parent's init function
        self.V = len(self.get_vocabulary())

    def get_trigram_probability(self, bigram, word):
        self.V = len(self.singlewords)
        k = .046
        previous1 = bigram[0]
        previous2 = bigram[1]
        trigram = (previous1, previous2, word)
        if trigram not in self.triwordcounts.keys():
            numer = k
        else:
            numer = self.triwordcounts[trigram] + k
        if previous2 == self.START and previous1 == self.START:
            #make count equal to number of sentences
            denom = self.singlewords[self.STOP] + self.V*k
            return numer / denom
        if bigram not in self.biwordcounts.keys():
            denom = self.V*k
        else:
            denom = self.biwordcounts[bigram] + self.V*k
        if numer == 0 or denom == 0:
            return k / (self.V*k)
        return numer / denom
