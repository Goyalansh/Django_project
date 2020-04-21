"""define url patterns for users"""

# LoginView takes care of username and password

from django.contrib.auth.views import LoginView

from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
  # login page
  path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
  # logout page
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register, name='register'),
]
