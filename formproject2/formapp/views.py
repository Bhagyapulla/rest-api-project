from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import FormAuthor, FormBook
from .forms import AuthorForm, BookForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('book_author')
        else:
            return HttpResponse('Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def insert_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_author')
    else:
        form = AuthorForm()

    return render(request, 'insert_author.html', {'form': form})  # Fixed indentation


@login_required
@user_passes_test(lambda u:u.is_superuser)
def insert_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_author')
    else:
        form = BookForm()

    return render(request, 'insert_book.html', {'form': form})

@login_required
def book_author(request):
    authors = FormAuthor.objects.all()
    books = FormBook.objects.all()
    return render(request, "book_auth.html", {"authors": authors, "books": books})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def edit_book(request,book_id):
    book=FormBook.objects.get(id=book_id)
    if request.method == 'POST':
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_author')
    else:
        form=BookForm(instance=book)
    return render(request,'edit_book.html',{'form':form})

@login_required
@user_passes_test(lambda u:u.is_superuser)
def del_book(request,book_id):
    book = FormBook.objects.get(id=book_id)
    book.book_image.delete(save=False)
    book.delete()
    return redirect('book_author')

@login_required
@user_passes_test(lambda u:u.is_superuser)
def edit_author(request,auth_id):
    author=FormAuthor.objects.get(id=auth_id)
    if request.method=='POST':
        form=AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return  redirect('book_author')
    else:
        form=AuthorForm(instance=author)
    return render(request,'edit_author.html',{'form':form})

@login_required
@user_passes_test(lambda u:u.is_superuser)

def del_author(request,auth_id):
    author=FormAuthor.objects.get(id=auth_id)
    author.delete()
    return redirect('book_author')






