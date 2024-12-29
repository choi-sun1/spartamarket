from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 회원가입 후 자동 로그인
            return redirect('home')  # 'home' URL로 리다이렉트 (적절히 수정)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 로그인
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')

    return render(request, 'accounts/login.html')

# 로그아웃
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')