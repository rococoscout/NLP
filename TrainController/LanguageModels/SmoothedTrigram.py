from .TrigramModel import TrigramModel

class SmoothedTrigram(TrigramModel):

    def __init__(self):
        super().__init__()


    def get_trigram_probability(self,trigram,bigram):
            k = .000095
            if not trigram in self.wordcounts:
                if bigram in self.wordcounts:
                    return k/(self.wordcounts[bigram]+(len(self.vocab)*k))
                else:
                    return k/(len(self.vocab)*k)
            else:
                return (self.wordcounts[trigram]+k) / (self.wordcounts[bigram]+(len(self.vocab)*k))
