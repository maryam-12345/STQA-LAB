import pytest

from grade_tracker.calculator import class_average, to_gpa, to_letter_grade, top_student
from grade_tracker.student import Student


@pytest.mark.parametrize(
    "score,grade",
    [(100, "A"), (90, "A"), (89, "B"), (80, "B"), (79, "C"), (70, "C"),
     (69, "D"), (60, "D"), (59, "F"), (0, "F")],
)
def test_letter_grade_boundaries(score, grade):
    assert to_letter_grade(score) == grade


@pytest.mark.parametrize("score", [-0.1, 100.1])
def test_letter_grade_invalid(score):
    with pytest.raises(ValueError):
        to_letter_grade(score)


def test_gpa():
    assert to_gpa(95) == 4.0
    assert to_gpa(65) == 1.0
    assert to_gpa(10) == 0.0


def _make(name, sid, *scores):
    s = Student(name, sid)
    for i, sc in enumerate(scores):
        s.add_score(f"C{i}", sc)
    return s


def test_class_average():
    assert class_average([]) == 0.0
    assert class_average([_make("A", 1, 80), _make("B", 2, 60)]) == 70.0


def test_top_student():
    assert top_student([]) is None
    a, b = _make("A", 1, 70), _make("B", 2, 95)
    assert top_student([a, b]) is b
