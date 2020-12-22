from week3.exercice3 import family_ages
from io import StringIO


def test_empty():
    s = StringIO()
    family_ages(s)

    s.seek(0)
    assert s.read() == ''


def test_one_person():
    s = StringIO()
    family_ages(s, a=1)

    s.seek(0)
    assert s.read() == 'a,1\n'


def test_five_people():
    s = StringIO()
    family_ages(s, a=1, b=2, c=3, d=4, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'


def test_sorted_five_people():
    s = StringIO()
    family_ages(s, a=1, d=4, b=2, c=3, e=5)

    s.seek(0)
    assert s.read() == 'a,1\nb,2\nc,3\nd,4\ne,5\n'
