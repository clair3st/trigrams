"""Tests for trigrams.py moduel."""


test_string = "I Wish I may I wish I might"


def test_tri_is_list():
    """Test whether tri is a non empty list."""
    from trigrams import tri
    assert type(tri) is list and len(tri) is not 0
