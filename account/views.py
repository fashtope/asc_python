from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


from .models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.type == User.Types.HOD:
                return redirect('hod:home')
            elif user.type == User.Types.LECTURER:
                return redirect('lecturer:home')
            elif user.type == User.Types.STUDENT:
                return redirect('student:home')
            else:
                return HttpResponseRedirect('<h3> Unknown User type<h3>')
        else:
            messages.error(request, "Username and password does not match")
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('account:login')