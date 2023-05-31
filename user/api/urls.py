from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from .api import RegisterApi

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
	path('', views.Routes.as_view()),
	path('todo/', views.TodoGetOrPost.as_view()),
	path('todo/<str:pk>/', views.TodoGetOrPost.as_view()),
	path('register/', RegisterApi.as_view()),
	path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	# path('todo/', views.getTodo),
	# path('updatetodo/<str:pk>/', views.updateTodo, name='update_todo'),
]
