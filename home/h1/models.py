from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)

    class Meta:
        db_table='student'