"""define url patterns for users"""

from django.contrib.auth.views import LoginView

from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
  path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
]