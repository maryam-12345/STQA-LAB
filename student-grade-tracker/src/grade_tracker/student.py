"""Student model."""


class Student:
    """Represents a student and their course scores."""

    def __init__(self, name, student_id):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if student_id <= 0:
            raise ValueError("Student ID must be positive")
        self.name = name.strip()
        self.student_id = student_id
        self.scores = {}

    def add_score(self, course, score):
        """Add or update a score (0-100) for a course."""
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")
        self.scores[course] = score

    def remove_score(self, course):
        """Remove a course score. Raises KeyError if it does not exist."""
        del self.scores[course]

    def average(self):
        """Return the average score, or 0.0 if there are no scores."""
        if not self.scores:
            return 0.0
        return sum(self.scores.values()) / len(self.scores)
