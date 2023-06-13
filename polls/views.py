from django.shortcuts import render
from polls.forms import ImageForm
from polls.models import product
from django.http import HttpResponse, HttpResponseRedirect
from polls import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import redirect
'''from .forms import UserRegistrationForm'''

@login_required(login_url="/login")
def upload_image(request):
    form=ImageForm()
    res=render(request,'upimage/upload.html',{'form':form})
    return res
def add(request):
    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        photo=models.product()
        photo.image=form.data['image']
        photo.save()
    else:
        form=ImageForm()
    s="Record Stored<br><a href='display'>View All Books</a>"
    return HttpResponse(s)


def display(request):
    images=product.objects.all()
    res=render(request,'disimage/display.html',{'images':images})
    return res
def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('upload')
        else:
            data['error']="Username or password is incorrect"
            res=render(request,'log/user_login.html',data)
            return res
    else:
        return render(request,'log/user_login.html',data)
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('login')

def search_loc(request):
    res=render(request,'searc/search.html')
    return res
def home_de(request):
    res=render(request,'home2/home2.html')
    return res
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'sign_up/signup.html', {'form': form})
