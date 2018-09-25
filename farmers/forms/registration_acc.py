from django.forms import forms

from farmers.db_farmers.farmes_regiser_model import FarmesRegistraton


class RegisterFaremerForm(forms.Form):

    name = None
    email = None
    password = None
    phone_number = None
    city = None
    id_reg_farmer = None

    # def __init__(self, name, email, id_reg_farmer, password, phone, city):
    #     self.name = name
    #     self.email = email
    #     self.password = password
    #     self.id_reg_farmer = id_reg_farmer
    #     self.phone = phone
    #     self.city = city

    def save(self, commit=True):
        super(FarmesRegistraton, self).save(commit=False)