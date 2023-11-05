from django.urls import path
from .import views

urlpatterns = [

    path('',views.home,name = 'Home'),
    path('register/',views.register,name = 'Register'),
    path('login/',views.login_view,name = 'Login'),
    path('application/', views.account_application, name='Account_application'),
]