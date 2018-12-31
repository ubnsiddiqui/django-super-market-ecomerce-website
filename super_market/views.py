from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from super_market.form import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .models import Cart,Product


def index(request):
    prod1 = Product.objects.all()[2:]
    return render(request, 'super_market/index.html', {'products': prod1})


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


def display_products(request):
    prod = Product.objects.all()
    return render(request, 'super_market/products.html', {'products': prod})


@login_required
def checkout(request):

    return render(request, 'super_market/checkout.html')


def single(request, product):
    prod = Product.objects.all()
    prod1 = Product.objects.all().exclude(id=product)[:4]
    for i in prod:
        if i.id == int(product):
            return render(request, 'super_market/single.html', {'product': i, 'prod': prod1})
        else:
            continue


