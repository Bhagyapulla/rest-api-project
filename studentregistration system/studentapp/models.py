from django.db import models


class Student(models.Model):
    name= models.CharField(max_length=40)
    age=models.IntegerField()
    phone_number=models.IntegerField()
    location=models.CharField(max_length=80)

    def __str__(self):
        return self.name

