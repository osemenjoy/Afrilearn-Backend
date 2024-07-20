from django.db import models
from django.contrib.auth.models import User


COURSE_CHOICES = [
    ('data_analysis', 'Data Analysis'),
    ('renewable_energy', 'Renewable Energy'),
    ('cyber_security', 'Cyber Security'),
    ('iot', 'Internet Of Things')
]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, default='learner')
    name = models.CharField(max_length=100, default='Mimi')
    phone_number = models.CharField(max_length=15, default='125')
    country = models.CharField(max_length=100, default='Nigeria')
    gender = models.CharField(max_length=10, default='M')
    qualifications = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES, default='data_analysis')
    
    def __str__(self):
        return self.user.username
