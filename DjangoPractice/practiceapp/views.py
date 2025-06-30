from idlelib.rpc import request_queue
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from practiceapp.models import Author,Book
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=User.objects.create_user(username = username,password = password)
        return redirect('login')
    return render(request,'resistration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('book')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def Insert_author(request):
    if request.method=='POST':
        name=request.POST.get('name')
        Author.objects.create(name=name)
        return HttpResponse('Author Added Successfully')
    return render(request,'author.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)



def Insert_book(request):
    if request.method=='POST':
        name=request.POST.get('name')
        author_name =request.POST.get('author')
        price = request.POST.get('price')

        authors=Author.objects.create(name=author_name)
        Book.objects.create(name=name,author=authors,price=price)
        return HttpResponse('Book Added Successfully')
    return render(request,'book.html')
@login_required
@user_passes_test(lambda u: u.is_superuser)

def author(request):
    bk = Book.objects.all()
    au = Author.objects.all()
    di = {'bk': bk, 'au': au}
    return render(request,'author2.html',di)
@login_required


def edit_data(request,id):
    da = Author.objects.get(id = id)
    di={'da':da}
    if request.method=='POST':
        da.name=request.POST.get('name')
        da.save()
        return redirect('author')
    return render(request,'edit_data.html',di)
@login_required
@user_passes_test(lambda u: u.is_superuser)



def delete_data(request,id):
    da=Author.objects.get(id=id)
    da.delete()
    return redirect('author')
@login_required



def book(request):
    bk=Book.objects.all()
    au=Author.objects.all()
    di={'bk':bk,'au':au}
    return render(request,'author2.html',di)
@login_required


def edit(request,id):
    da=Book.objects.get(id=id)
    di={'da':da}
    if request.method=='POST':
        da.name=request.POST.get('name')
        name=request.POST.get('author')
        authors=Author.objects.get(name=author)
        da.author=authors
        da.price=request.POST.get('price')
        da.save()
        return redirect(book)
    return render(request,'book_edit.html',di)
@login_required
@user_passes_test(lambda u: u.is_superuser)


def delete(request,id):
    da=Book.objects.get(id=id)
    da.delete()
    return redirect('book')

