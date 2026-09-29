"""Grade calculation helpers."""


def to_letter_grade(score):
    """Convert a numeric score (0-100) to a letter grade."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def to_gpa(score):
    """Convert a numeric score to a 4.0 scale GPA."""
    grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    return grades[to_letter_grade(score)]


def class_average(students):
    """Return the average of all student averages (0.0 for empty list)."""
    if not students:
        return 0.0
    return sum(s.average() for s in students) / len(students)


def top_student(students):
    """Return the student with the highest average, or None if empty."""
    if not students:
        return None
    return max(students, key=lambda s: s.average())
