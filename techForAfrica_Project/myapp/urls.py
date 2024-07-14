from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage_view, name='landing_page'),
    path('afrilearn/', views.home_view, name='home'),
    path('signup/tutor/', views.tutor_signup, name='tutor_signup'),
    path('signup/learner/', views.learner_signup, name='learner_signup'),
    path('signup/student/', views.learner_signup, name='student-register'),  # Alias for student-register
    path('signup/tutor-register/', views.tutor_signup, name='tutor-register'),  # Alias for tutor-register
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('programmes/', views.programmes_view, name='programmes'),
    path('tutors/', views.tutors_view, name='tutors'),
    path('register/', views.register, name='register'),  # Added URL pattern for register
]
