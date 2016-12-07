"""Write new stories based on inputted sentences or books using trigram algo."""


sentence = 'I wish I may I wish I might'


def make_baselist(sentence):
    """Create baselist from an inputted sentence."""
    baselist = sentence.split()
    return baselist

def make_bigram(baselist):
    """Make bigrams out of an ordinary list."""
    bigrams = []
    for c, i in enumerate(baselist, 2):
            bigrams.append(baselist[c - 2] + " " + baselist[c - 1])
            if c == len(baselist):
                return bigrams
