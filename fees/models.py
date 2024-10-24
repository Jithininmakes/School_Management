from django.db import models
from student.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

    def __str__(self):
        return f'{self.student.name} - {self.amount}'
