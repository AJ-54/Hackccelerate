from django.shortcuts import render,redirect
from accounts.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from accounts.models import *
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser

# Create your views here.



def user_login(request) :
    if request.method == "POST" :    
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
       


        if user is not None :  
            login(request,user)       
            role = user.role 
            
            if role =="S" :
                return redirect('students:student_course_list')
            elif role=="T" :
                return redirect('courses:manage_course_list')
            elif role =="P" :
                return redirect('') 
            else :
                messages.error(request,"Invalid credentials")
                return render(request,"accounts/login.html")        
        else :
             messages.error(request,"Invalid credentials")
             return render(request,"accounts/login.html")


    else :
        if request.user and not isinstance(request.user ,AnonymousUser):
            role = request.user.role 
            if role =="DT" :
                return redirect('chits:deligate_index')
            elif role=="MD" :
                return redirect('chits:moderator_index')
            elif role =="JD" :
                return redirect('chits:judge_index') 
            else :
                messages.error(request,"Invalid credentials")
                return render(request,"accounts/login.html")
           
        else :
          return render(request,"accounts/login.html")


class Logout(LoginRequiredMixin,View):

    def get(self,request):
        logout(request)
        return redirect('accounts:login')

logout_user = Logout.as_view()
