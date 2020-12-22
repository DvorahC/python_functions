import pytest
from week2.exercice2 import left_right_chars
from io import StringIO


@pytest.fixture
def empty_file():
    return StringIO('')


@pytest.fixture
def alphabet_file():
    return StringIO('''abcdefg
hijklmnop
qrstuvwxyz
''')


@pytest.fixture
def numbers_file():
    return StringIO('''12345
67890
''')


def test_no_file():
    assert left_right_chars() == []


def test_empty_file(empty_file):
    assert left_right_chars(empty_file) == []


def test_alphabet_file(alphabet_file):
    assert left_right_chars(alphabet_file) == [['a', 'g'],
                                               ['h', 'p'],
                                               ['q', 'z']]


def test_alphabet_file_n_3(alphabet_file):
    assert left_right_chars(alphabet_file, numchars=3) == [['abc', 'efg'],
                                                           ['hij', 'nop'],
                                                           ['qrs', 'xyz']]


def test_numbers_file_n_3(numbers_file):
    assert left_right_chars(numbers_file, numchars=3) == [['123', '345'],
                                                          ['678', '890']]


def test_both_file_n_3(alphabet_file, numbers_file):
    assert left_right_chars(alphabet_file,
                            numbers_file, numchars=3) == [['abc', 'efg'],
                                                          ['hij', 'nop'],
                                                          ['qrs', 'xyz'],
                                                          ['123', '345'],
                                                          ['678', '890']]
