from django.contrib import admin
from farmers.db_farmers.farmes_regiser_model import FarmesRegistraton, SoldProducts, PostProducts

# Register your models here.

admin.site.register(FarmesRegistraton)
admin.site.register(SoldProducts)
admin.site.register(PostProducts)
