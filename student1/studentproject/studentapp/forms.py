from django import forms
from .models import FormStudents


class StudentForm(forms.ModelForm):
    class Meta:
        model=FormStudents
        fields=['stu_name','age','course','email_id','stu_photo']