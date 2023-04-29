from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def homePage(request):
  context = {}
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
        return render(request, "user/home.html")
    else:
      return render(request, "user/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "user/login.html") 

def logoutPage(request):
  logout(request)
  context = {}
  return render(request, "user/login.html", context)