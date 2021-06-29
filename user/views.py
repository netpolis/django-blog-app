from django.contrib import auth
from django.forms.forms import Form
from django.shortcuts import redirect, render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def logoutUser(request):
    logout(request)
    messages.success(request,"başarılı bir şekilde çıkış yaptınız")
    return redirect("index")








def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Kullanıcı adı yada parola hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarılı bir şekilde giriş yaptınız")
        login(request,user)
        next=request.GET.get("next")
        next=next if next != None else "index"   
               
        return redirect(next)

    return render(request,"login.html",context)



def register(request):
    form =RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        auth.login(request,newUser)
        messages.info(request,"Başırı ile kayıt yapıldı.")
        return redirect("index")
    
    context={
        "form":form
    }
    return render(request,"register.html",context)







    
        






    