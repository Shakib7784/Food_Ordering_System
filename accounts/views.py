
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout # it will come from our user model
from accounts.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def User_login(request):
    data ={} # for showing error message
    error = False
    if request.user.is_authenticated: # here we are giving condition that if a user do login then he/she will not go to the login page again. he must have to stay on home page.
        return redirect("home")
    else:
        if request.method == "POST":
            email = request.POST.get("email")  #here we are accessing email and password from template.
            password = request.POST.get("password")
            email.lower()

            user = authenticate(request, email=email,password = password) # here we are checking that user is exist on database or not. if not exist then user variable will hold None

            if user is not None:
                login(request, user) # if user will not none then user can do login through this function.
                return redirect("home") #then redirect to the home page.
            else:
                error=True
                data = {
                    "error" :error
                }
        
    return render(request,"accounts/login.html",data) # this user_login funciton will take us login page.

def registration(request):
    is_exist = False
    data ={
        "exist":is_exist
    }
    if request.user.is_authenticated: # here we are giving condition that if a user do login then he/she will not go to the login page again. he must have to stay on home page.
        return redirect("home")
    else:
        if request.method == "POST" and request.FILES['image']: # checking condition that user have subbmited form with an image
            first_name = request.POST.get("first_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            password = request.POST.get("password")
            address = request.POST.get("address")
            image = request.FILES['image'] # we can capture uploaded image by calling FILES

            #now check that this email is already exist on database or not
            email_exist = User.objects.filter(email=email)

            if not email_exist: # if email is not exist then we will create new user
                user = User.objects.create_user(first_name = first_name,email=email,phone=phone,password = password,address=address,image=image) #creating new user if user isn't exist
                user.is_active = True # making user active
                user.save()
                return render(request,"accounts/login.html",data) # after creating new user it will render login page
            else:
                is_exist =True
                data ={
                    "exist":is_exist
                }
    return render(request,"accounts/registration.html",data)






@login_required #we are using login required decorater. that means this decorator insure us that user must have to be login to do logout
def User_logout(request):
    logout(request)
    return redirect('home')