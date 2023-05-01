from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TodoSerializer
from user.models import Todo

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
		'api/token',
		'api/token/refresh',
	]
  
  return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTodo(request):
  user = request.user
  todo = user.todo_set.all()
  serializer = TodoSerializer(todo, many=True)
  return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def updateTodo(request, pk):
  if request.method == 'POST':
    user = request.user
    todo = user.todo_set.get(id=pk)
    if todo.status == 'PR':
      todo.status = 'CO'
    elif todo.status == 'CO':
      todo.status = 'PR'
    todo.save()
    serializer = TodoSerializer(todo)
    return Response(serializer.data)
  return Response({"message": "use POST method"})