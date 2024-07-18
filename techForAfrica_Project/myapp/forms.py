from django import forms
from django.contrib.auth.models import User

class TutorSignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=15, required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'input-field'}), choices=[('M', 'Male'), ('F', 'Female')], required=True)
    qualifications = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-field'}), required=True)
    cv = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'input-field'}), required=True)

class LearnerSignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}), required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=15, required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field'}), max_length=100, required=True)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'input-field'}), choices=[('M', 'Male'), ('F', 'Female')], required=True)
