from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse("This account is dissabled!")
        else:
            return HttpResponse("Invalid login!")
    else:
        return HttpResponse("Unsupported method")

def logout_form(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))