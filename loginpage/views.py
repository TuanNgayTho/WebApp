from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.sessions.exceptions import SuspiciousSession
# Create your views here.


class homepage(LoginView):
    template_name = 'home.html'


@login_required(login_url="/login")
def home(request):
    return render(request, "home.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            remember = request.POST.get('remember')
            if remember:
                print("remember")
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
            else:
                print("Dont remember")
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        except:
            print("Dont remember")
            is_private = False
            settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, '!Tên đăng nhập hoặc mật khẩu không chính xác')
    context = {}
    return render(request, "login.html", context)


def logoutpage(request):
    logout(request)
    return redirect('/login')

