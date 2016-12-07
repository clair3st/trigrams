"""Tests for trigrams.py moduel."""


test_string = "I Wish I may I wish I might"


test_list = ["sddf", "dfsfs", "sdgsdf", "word", "another", "blue", "orange"]

test_biograms = ["I wish", "wish I", "I may", "may I ", "I \
wish", "wish I", "I might"]


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


def test_all_bigrams():
    """Test whether all indexes of bigram list are bigrams."""
    from trigrams import make_bigram
    new_bigram = make_bigram(test_list)
    result = True
    for item in new_bigram:
        if len(item.split()) != 2:
            result = False
            break
    assert result


def test_dict():
    """Test whether dictionary is returned from make dict function."""
    from trigrams import make_dict
    assert type(make_dict(test_biograms)) == dict


def test_dict_contents():
    """Test whether dictionary contains all biograms."""
    from trigrams import make_dict
    result = True
    dict_ex = make_dict(test_biograms)
    for n in test_biograms:
        if n not in dict_ex:
            result = False
            break
    assert result
