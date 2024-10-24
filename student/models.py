from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    class_name = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name