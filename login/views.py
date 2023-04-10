from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def getLogin(request):
    form = LoginForm()
    content = {'form': form}
    return render(request,'login.html',content)

def postLogin(request):
    usernamee = request.POST['username']

    passwordd = request.POST['password']
    # usercount = User.objects.filter(username = username,email=email,password = password).count()
    user = authenticate(request, username = usernamee, password = passwordd)
    # dkiau = authenticate()
    if user is not None:
        login(request,user)
        return redirect('/admin')
    else:
        messages.add_message(request, messages.ERROR, 'Sai tên đăng nhập hoặc mật khẩu!!!') 
        return redirect('/admin/login')
def Logout(request):
    logout(request)
    return redirect('/admin/login')
        

    