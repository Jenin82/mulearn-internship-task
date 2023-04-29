from django.urls import path
from . import views

urlpatterns = [
		path('', views.homePage, name="home"),
		path('login/', views.loginPage, name="login"),
		path('logout/', views.logoutPage, name="logout"),
    path('signup/', views.signup, name="signup"),
]

