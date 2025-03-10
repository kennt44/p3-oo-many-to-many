class Course:
    all = []

    def __init__(self, title):
        self.title = title
        Course.all.append(self)

    def enrollments(self):
        """Return a list of enrollments for this course."""
        return [enrollment for enrollment in Enrollment.all if enrollment.course == self]

    def students(self):
        """Return a list of students enrolled in this course."""
        return [enrollment.student for enrollment in self.enrollments()]

    def enroll_student(self, student):
        """Enroll a student in the course."""
        Enrollment(student, self)
