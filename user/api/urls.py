from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from .api import RegisterApi

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
		path('', views.getRoutes),
		path('todo/', views.getTodo),
		#path('status/', views.statusTodo),
		path('register/', RegisterApi.as_view()),
		path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
