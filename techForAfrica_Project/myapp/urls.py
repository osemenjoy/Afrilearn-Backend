from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/tutor/', views.tutor_signup, name='tutor_signup'),
    path('signup/learner/', views.learner_signup, name='learner_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('programmes/', views.programmes_view, name='programmes'),
    path('tutors/', views.tutors_view, name='tutors'),
    path('popular_programmes/', views.popular_programmes_view, name='popular_programmes'),
]
