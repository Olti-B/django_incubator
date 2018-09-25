from django.shortcuts import render

from farmers.db_farmers.farmes_regiser_model import FarmesRegistraton
from farmers.forms.registration_acc import RegisterFaremerForm


def index(req):
    return render(req, 'farmers/home.html')


def register(req):
    if req.method == 'POST':
        form = RegisterFaremerForm(req.POST)
        if form.is_valid():
            print("test")
            # name = form.va
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # city = form.cleaned_data['city']
            # id_reg_farmer = form.cleaned_data['id']
            # phone = form.cleaned_data['phone']
            # print(name, email, password, password, city, phone, id_reg_farmer)
            # form.__init__(name, email, id_reg_farmer, password, phone, city)
            # form.save()

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
    return render(req, 'farmers/login.html')


def reset(req):
    return render(req, 'farmers/reset.html')
