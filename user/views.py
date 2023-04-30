from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from user.forms import TodoForm

from user.models import Todo

# Create your views here.

@login_required(login_url='login')
def homePage(request):
  todo = Todo.objects.all()
  context = {'todo': todo}
  return render(request, 'user/home.html', context)

def loginPage(request):
  if request.user.is_authenticated:
    return render(request, "user/home.html")

  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username , password=password)
    if user is not None:
      login(request, user)
      if 'next' in request.POST:
        return HttpResponseRedirect(request.POST.get('next'))
      else:
        todo = Todo.objects.all()
        context = {'todo': todo}
        return render(request, "user/home.html",context)
    else:
      return render(request, "user/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "user/login.html") 

def logoutPage(request):
  logout(request)
  context = {}
  return render(request, "user/login.html", context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/signup.html', {'form': form})
  
def createTodo(request):
  todo = Todo()
  form = TodoForm()
  context = {'todo': todo, 'form': form}
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      todo = form.save(commit=False)
    title = request.POST["title"]
    description = request.POST["description"]
    todo.status = 'In-progress'
    todo.title = title
    todo.description = description
    todo.save()
    return redirect('home')
  return render(request, "user/create_todo.html", context)


def todo(request, pk):
  todo = Todo.objects.get(id=pk)
  context = {'todo': todo}
  return render(request, "user/todo.html", context)

def statusCompleted(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.status = 'Completed'
  todo.save()
  return redirect('home')

def statusInprogress(request, pk):
  todo = Todo.objects.get(id=pk)
  todo.status = 'In-progress'
  todo.save()
  return redirect('home')
