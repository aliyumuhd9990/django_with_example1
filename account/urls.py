from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', SignupView.as_view(), name= 'signup'),
    path('logout/', LogoutView, name= 'logout'),
    path('login/', auth_views.LoginView.as_view(), name= 'login'),
    # path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
]
