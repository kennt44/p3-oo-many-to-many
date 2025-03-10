from datetime import datetime

class Student:
    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def enroll_in_course(self, course):
        """Enroll the student in a course by creating an enrollment object."""
        Enrollment(self, course)

    def enrollments(self):
        """Return a list of the student's enrollments."""
        return [enrollment for enrollment in Enrollment.all if enrollment.student == self]

    def courses(self):
        """Return a list of courses the student is enrolled in."""
        return [enrollment.course for enrollment in self.enrollments()]
