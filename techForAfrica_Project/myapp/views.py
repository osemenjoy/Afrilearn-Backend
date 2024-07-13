from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import TutorSignUpForm, LearnerSignUpForm
from django.http import HttpResponse


def my_view(request):
    return HttpResponse("Hello, world!")

def home_view(request):
    return render(request, 'afri_learn.html')

def tutor_signup(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TutorSignUpForm()

    return render(request, 'Tutor-Register.html', {'form': form, 'user_type': 'Tutor'})

def learner_signup(request):
    if request.method == 'POST':
        form = LearnerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LearnerSignUpForm()

    return render(request, 'Student-Register.html', {'form': form, 'user_type': 'Learner'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def programmes_view(request):
    return render(request, 'Programmes.html')

def tutors_view(request):
    return render(request, 'Tutors.html')

def register(request):
    return render(request, 'Register.html')

