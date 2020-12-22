import pytest

from week1.exercice1 import acrobot


def test_empty_sentence():
    assert acrobot('') == ''


def test_one_word_sentence():
    assert acrobot('hello') == 'H'


@pytest.mark.parametrize('sentence, acronym', [
    ('central intelligence agency', 'CIA'),
    ('three letter acronym', 'TLA'),
    ('in my humble opinion', 'IMHO'),
    ('rolling on the floor laughing', 'ROTFL')])
def test_sentences(sentence, acronym):
    assert acrobot(sentence) == acronym


@pytest.mark.parametrize('sentence, min_word_length, acronym', [
    ('certificate of deposit', 3, 'CD'),
    ('in my humble opinion', 3, 'HO'),
    ('in my humble opinion', 10, ''),
    ('rolling on the floor laughing', 3, 'RTFL')])
def test_sentences_with_min_word_length(sentence, min_word_length, acronym):
    assert acrobot(sentence, min_word_length) == acronym
