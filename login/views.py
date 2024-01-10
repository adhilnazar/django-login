from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def log_in(request):
   
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        user_name = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = user_name,password = password)
        if user is not None:            
            login(request,user)
            return redirect('home')
        else:
            print('invalid data')
    return render(request,'login.html')

@login_required(login_url='/')
def home(request):
    return render(request,'home.html')

@login_required(login_url='/')    
def log_out(request):
    logout(request)
    return redirect('log_in')