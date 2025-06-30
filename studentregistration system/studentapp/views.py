from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})
