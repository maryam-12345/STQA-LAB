import pytest

from grade_tracker.student import Student


def test_create_student():
    s = Student("  Ali  ", 1)
    assert s.name == "Ali"
    assert s.student_id == 1
    assert s.scores == {}


@pytest.mark.parametrize("name,sid", [("", 1), ("   ", 1), (None, 1), ("Ali", 0), ("Ali", -5)])
def test_invalid_student(name, sid):
    with pytest.raises(ValueError):
        Student(name, sid)


def test_add_and_update_score():
    s = Student("Sara", 2)
    s.add_score("Math", 80)
    s.add_score("Math", 90)
    assert s.scores == {"Math": 90}


@pytest.mark.parametrize("score", [-1, 101])
def test_invalid_score(score):
    with pytest.raises(ValueError):
        Student("Sara", 2).add_score("Math", score)


def test_remove_score():
    s = Student("Sara", 2)
    s.add_score("Math", 80)
    s.remove_score("Math")
    assert s.scores == {}


def test_remove_missing_score():
    with pytest.raises(KeyError):
        Student("Sara", 2).remove_score("Physics")


def test_average():
    s = Student("Sara", 2)
    assert s.average() == 0.0
    s.add_score("Math", 80)
    s.add_score("Physics", 90)
    assert s.average() == 85.0
