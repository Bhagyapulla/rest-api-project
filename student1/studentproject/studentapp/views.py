from django.shortcuts import render ,redirect
from .forms import StudentForm
from .models import FormStudents

def student(request):
    return render (request,'stu.html')


def welcome(request):
    name = request.GET.get('name', 'Guest')
    return render(request, 'home.html', {'name': name})




from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import FormStudents

def register_stu(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "register.html", {"form": form})

def student_list(request):
    students = FormStudents.objects.all()
    return render(request, "details.html", {"students": students})
