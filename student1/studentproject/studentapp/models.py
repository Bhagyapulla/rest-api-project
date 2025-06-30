from django.db import models

# Create your models here.

class FormStudents(models.Model):
    stu_name=models.CharField(max_length=70)
    age=models.IntegerField()
    course=models.CharField(max_length=60)
    email_id=models.EmailField(max_length=80)
    stu_photo=models.ImageField(upload_to='stu_images/',null=True,blank=True)
    def  _str_(self):
        return self.stu_name
