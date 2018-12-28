from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from super_market.form import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'super_market/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            # user = authenticate(
            #     request,
            #     username=username,
            #     password=password
            # )
            # login(request, user)
            return redirect(reverse('super_market:login'))
    else:
        form = RegisterForm()
        return render(request, 'super_market/registered.html', {'form':form})


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
    else:

        return render(request, 'super_market/login.html', {})


@csrf_exempt
def contact(request):
    return render(request, 'super_market/contact.html')
