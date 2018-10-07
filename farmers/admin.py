from django.contrib import admin
from farmers.db_farmers.farmes_regiser_model import FarmesRegistraton, SoldProduct, PostProduct

# Register your models here.

admin.site.register(FarmesRegistraton)
admin.site.register(SoldProduct)
admin.site.register(PostProduct)
