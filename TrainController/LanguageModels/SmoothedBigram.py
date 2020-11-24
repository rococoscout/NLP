from .BigramModel import BigramModel

class SmoothedBigram(BigramModel):

    def __init__(self):
        super().__init__()


    def get_bigram_probability(self,bigram,unigram):
            k = .0002
            if not bigram in self.wordcounts:
                if unigram in self.wordcounts:
                    return k/(self.wordcounts[unigram]+(len(self.vocab)*k))
                else:
                    return k/(len(self.vocab)*k)
            else:
                return (self.wordcounts[bigram]+k) / (self.wordcounts[unigram]+(len(self.vocab)*k))
