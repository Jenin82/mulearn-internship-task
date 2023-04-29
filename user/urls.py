from django.urls import path
from . import views

urlpatterns = [
		path('', views.homePage, name="home"),
		path('login/', views.loginPage, name="login"),
		path('logout/', views.logoutPage, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('create-todo/', views.createTodo, name="create-todo"),
    path('todo/<str:pk>/', views.todo, name="todo"),
    path('todo/<str:pk>/completed', views.statusCompleted, name="completed"),
    path('todo/<str:pk>/inprogress', views.statusInprogress, name="inprogress"),
]

