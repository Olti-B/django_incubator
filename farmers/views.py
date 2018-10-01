from django.shortcuts import render
from django.utils import timezone

from farmers.db_farmers.farmes_regiser_model import FarmesRegistraton


def index(req):
    return render(req, 'farmers/home.html')


def register(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        email = req.POST.get("email")
        password = req.POST.get("password")
        password_confirm = req.POST.get("password_confirm")
        city = req.POST.get("city")
        id_reg_farmer = req.POST.get("id")
        phone = req.POST.get("phone")

        if len(username) != 0 and len(email) != 0 and len(password) != 0 and len(password_confirm) != 0 and len(
                id_reg_farmer) != 0 and len(phone) != 0 and len(city) != 0:
            if password == password_confirm:
                registration = FarmesRegistraton(name=username, email=email, password=password,
                                                 id_reg_farmer=id_reg_farmer, phone_number=phone, city=city,
                                                 date=timezone.now())
                registration.save()
                return render(req, 'farmers/login.html')

            else:
                return render(req, 'farmers/register.html', {'error_password_conf': "Please enter the same password"})

    return render(req, 'farmers/register.html')


def products(req):
    return render(req, 'farmers/products.html')


def land(req):
    return render(req, 'farmers/land.html')


def invest(req):
    return render(req, 'farmers/invest.html')


def plant_register(req):
    return render(req, 'farmers/plant_register.html')


def profile(req):
    return render(req, 'farmers/profile.html')


def login(req):
    if req.method == 'POST':
        email = req.POST.get("email")
        password = req.POST.get("password")
        if len(email) != 0 and len(password) != 0:
            #       ToDo
            if FarmesRegistraton.objects.filter(email=email, password=password):
                return render(req, 'farmers/profile.html')

    return render(req, 'farmers/login.html')


def reset(req):
    return render(req, 'farmers/reset.html')


def make_post(req):
    return render(req, 'farmers/make_post.html')


def sold_products(req):
    return render(req, 'farmers/sold_products.html')