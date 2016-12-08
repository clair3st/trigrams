"""Write new stories based on inputted text using trigram algo."""
from random import sample


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


def make_dict(bigrams):
    """Build dictonary with bigram keys."""
    bigram_dict = {}
    for each in bigrams:
        bigram_dict.setdefault(each, [])
    return bigram_dict


def populate_dict(the_dict, bigram_list, word_list):
    """Populate dictonary values with words from wordlist."""
    for idx, item in enumerate(bigram_list):
        if idx + 1 == len(bigram_list):
            return the_dict
        new_value = word_list[idx + 2]
        the_dict[item].append(new_value)


def start_output(bigram_list):
    """The function takes one random bigram for the start of output."""
    a = sample(bigram_list, 1)
    output = ''.join(a)
    return output
