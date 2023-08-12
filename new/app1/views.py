from django.shortcuts import render
from app1.models import Place,Team,Myuser
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'home.html',{'p':p,'t':t})

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        pl = request.POST['pl']
        n = request.POST['n']
        u = Myuser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,place=pl,phonenumber=n)
        u.save()
        return home(request)
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,"Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return user_login(request)

