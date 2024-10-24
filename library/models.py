from django.db import models
from student.models import Student

class Library(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.book_title
