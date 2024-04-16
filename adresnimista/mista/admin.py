from django.contrib import admin

from .models import City, Address

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass