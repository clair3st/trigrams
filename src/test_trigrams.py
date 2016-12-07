"""Tests for trigrams.py moduel."""


test_string = "I Wish I may I wish I might"


test_list = ["sddf", "dfsfs", "sdgsdf", "word", "another", "blue", "orange"]


def test_make_list():
    """Test whether function makes list."""
    from trigrams import make_baselist, sentence
    new_list = make_baselist(sentence)
    assert type(new_list) == list


def test_make_bigrams():
    """Test whether function makes bigram."""
    from trigrams import make_bigram
    new_bigram = make_bigram(test_list)
    assert len(new_bigram[1].split()) == 2
