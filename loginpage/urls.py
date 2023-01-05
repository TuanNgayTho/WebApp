from django.urls import path
from loginpage import views

app_name = "loginpage"
urlpatterns = [
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('home', views.home, name='home'),
    path('homepage', views.homepage.as_view(), name="homepage")
]