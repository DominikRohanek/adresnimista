from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("address/<int:city_id>/",views.address, name="address"),
    path("accounts/registration/", views.registration, name="registration")
]
