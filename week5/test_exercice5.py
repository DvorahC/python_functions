import pytest
from week5.exercice5 import file_sizes, file_to_dict
from io import StringIO


@pytest.fixture
def short_file():
    s = StringIO('abcd\n')
    s.name = 'short_file'
    return s


@pytest.fixture
def medium_file():
    s = StringIO('efgh\n' * 10)
    s.name = 'medium_file'
    return s


@pytest.fixture
def long_file():
    s = StringIO('ijklmnopqrstuvwx\n' * 100)
    s.name = 'long_file'
    return s


def test_no_files():
    assert file_sizes() == []


def test_all_files(short_file, medium_file, long_file):
    fs = file_sizes(short_file, medium_file, long_file)
    assert type(fs) == list
    assert len(fs) == 3
    assert all([type(one_item) == dict
                for one_item in fs])
    assert len(fs) == 3
    assert fs[0]['name'] == 'short_file'
    assert fs[1]['name'] == 'medium_file'
    assert fs[2]['name'] == 'long_file'

    assert fs[0]['size'] == 5
    assert fs[1]['size'] == 50
    assert fs[2]['size'] == 1700


def test_all_files_backward(long_file, medium_file, short_file):
    fs = file_sizes(short_file, medium_file, long_file)
    assert type(fs) == list
    assert len(fs) == 3
    assert all([type(one_item) == dict
                for one_item in fs])
    assert len(fs) == 3
    assert fs[0]['name'] == 'short_file'
    assert fs[1]['name'] == 'medium_file'
    assert fs[2]['name'] == 'long_file'

    assert fs[0]['size'] == 5
    assert fs[1]['size'] == 50
    assert fs[2]['size'] == 1700
