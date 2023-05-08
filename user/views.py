from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from user.models import Todo

# Create your views here.

@login_required(login_url='login')
def homePage(request):
  todo = Todo.objects.all()
  context = {'todo': todo}
  return render(request, 'user/home.html', context)

def loginPage(request):
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username , password=password)
    if user is not None:
      login(request, user)
      if 'next' in request.POST:
        return HttpResponseRedirect(request.POST.get('next'))
      else:
        return redirect('home')
    else:
      return render(request, "user/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "user/login.html") 

def logoutPage(request):
  logout(request)
  return redirect('login')


def signup(request):
  form = UserCreationForm(request.POST)
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home')
  context = {'form': form}
  return render(request, "user/signup.html", context)

@login_required(login_url='login')
def createTodo(request):
  todo = Todo()
  context = {'todo': todo}
  if request.method == 'POST':
    todo = Todo.objects.create(
			host = request.user,
			title = request.POST["title"],
		)
    return redirect('home')
  return render(request, "user/create_todo.html", context)

@login_required(login_url='login')
def todo(request, pk):
  todo = Todo.objects.get(id=pk)
  context = {'todo': todo}
  return render(request, "user/todo.html", context)

def statusCompleted(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.isCompleted = True
  todo.save()
  return redirect('home')

def statusInprogress(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.isCompleted = False
  todo.save()
  return redirect('home')
