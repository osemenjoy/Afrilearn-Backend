from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='home'),
    path('signup/tutor/', views.tutor_signup, name='tutor_signup'),
    path('signup/student/', views.learner_signup, name='learner_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
