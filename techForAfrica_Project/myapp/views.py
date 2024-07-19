from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import TutorSignUpForm, LearnerSignUpForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import *

from .models import Profile

def my_view(request):
    return HttpResponse("Hello, world!")

def home_view(request):
    return render(request, 'Afri_Learn.html')

def LandingPage_view(request):
    return render(request, 'LandingPage.html')

def tutor_signup(request):
    if request.method == 'POST':
        form = TutorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            country = form.cleaned_data.get('country')
            gender = form.cleaned_data.get('gender')
            qualifications = form.cleaned_data.get('qualifications')
            cv = form.cleaned_data.get('cv')

            if password1 != password2:
                form.add_error('password2', 'Passwords do not match')
            else:
                # Check if username already exists
                if User.objects.filter(username=username).exists():
                    return HttpResponse("Username already exists")

                # Create user
                user = User.objects.create_user(username=username, email=email, password=password1)
                
                # Create profile
                profile = Profile.objects.create(
                    user=user,
                    user_type='tutor',
                    name=name,
                    phone_number=phone_number,
                    country=country,
                    gender=gender,
                    qualifications=qualifications,
                    cv=cv
                )
                
                # Authenticate and login the user
                user = authenticate(username=username, password=password1)
                if user is not None:
                    login(request, user)
                    return redirect('login')  # Redirect to tutor dashboard after signup
        else:
            # Print out form errors
            print(form.errors)
            return HttpResponse(f"Form is not valid: {form.errors}")
    else:
        form = TutorSignUpForm()
    return render(request, 'Tutor-Register.html', {'form': form})

def learner_signup(request):
    if request.method == 'POST':
        form = LearnerSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            country = form.cleaned_data['country']
            gender = form.cleaned_data['gender']

            if password1 != password2:
                form.add_error('password2', 'Passwords do not match')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    profile = Profile.objects.create(user=user, user_type='learner', name=name, phone_number=phone_number, country=country, gender=gender)
                    return redirect('home')
                except IntegrityError:
                    form.add_error('username', 'Username already taken')
    else:
        form = LearnerSignUpForm()
    return render(request, 'Student-Register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Username: {username}, Password: {password}")
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User authenticated")
                login(request, user)

                # Determine user type from Profile
                try:
                    profile = Profile.objects.get(user=user)
                    print(f"Profile user type: {profile.user_type}")
                    if profile.user_type == 'learner':
                        return redirect('student_dashboard')  # Change 'student_dashboard' to your actual URL name
                    elif profile.user_type == 'tutor':
                        return redirect('tutor_dashboard')  # Change 'tutor_dashboard' to your actual URL name
                    else:
                        print("Unknown user type")
                        return HttpResponse("Unknown user type.")
                except Profile.DoesNotExist:
                    print("Profile does not exist")
                    return HttpResponse("User profile does not exist.")
            else:
                print("Authentication failed")
                return HttpResponse("Invalid username or password.")
        else:
            print("Form is invalid")
            return render(request, 'login.html', {'form': form})
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

from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'student-dashboard.html')

def tutor_dashboard(request):
    return render(request, 'tutor-dashboard.html')
