from datetime import datetime
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

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

class Routes(APIView):
  def get(self, request, format=None):
    routes = [
		'api/token',
		'api/token/refresh',
		'register/',
		'api/todo/   - use GET to retrieve all Todo and POST to create a new one. body:[title:'']',
		'todo/<str:pk>/   - use PUT or DELETE to update status/delete a Todo, provide todo id in url eg: todo/7/',
		]
    return Response(routes)

@permission_classes([IsAuthenticated])
class TodoGetOrPost(APIView):
  
	def get(self, request, format=None):
		user = request.user
		todo = user.todo_set.all()
		serializer = TodoSerializer(todo, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		if request.method == 'POST':
			todo = Todo.objects.create(
				host = request.user,
				title = request.POST["title"],
			)
			serializer = TodoSerializer(todo)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		if request.method == 'PUT':
			user = request.user
			todo = user.todo_set.get(id=pk)
			if todo.isCompleted == False:
				todo.isCompleted = True
			elif todo.isCompleted == True:
				todo.isCompleted = False
			todo.save()
			serializer = TodoSerializer(todo)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		if request.method == 'DELETE':
			user = request.user
			todo = user.todo_set.get(id=pk)
			todo.delete()
			serializer = TodoSerializer(todo)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# function based views :

# @api_view(['GET'])
# def getRoutes(request):
#   routes = [
# 		'api/token',
# 		'api/token/refresh',
# 		'api/todo/',
# 		'register/',
# 		'updatetodo/<str:pk>/',
# 	]
#   return Response(routes)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getTodo(request):
#   user = request.user
#   todo = user.todo_set.all()
#   serializer = TodoSerializer(todo, many=True)
#   return Response(serializer.data)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def updateTodo(request, pk):
#   if request.method == 'POST':
#     user = request.user
#     todo = user.todo_set.get(id=pk)
#     if todo.status == 'PR':
#       todo.status = 'CO'
#     elif todo.status == 'CO':
#       todo.status = 'PR'
#     todo.save()
#     serializer = TodoSerializer(todo)
#     return Response(serializer.data)
#   return Response({"message": "use POST method"})