from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import City, Address

def index(request):
    cities = City.objects.all()

    if request.GET.get("search"):
        cities=cities.filter(name__icontains=request.GET.get("search"))

    paginator = Paginator(cities, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"page_obj":page_obj})
    
def address(request, city_id):
    city = get_object_or_404(City, id=city_id)
    addresses=city.address_set.all()
    
    if request.GET.get("search"):
        addresses=addresses.filter(Q(street__icontains=request.GET.get("search")) | Q(descriptive_number=request.GET.get("search")) | Q(orientation_number=request.GET.get("search")))

    paginator = Paginator(addresses, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"address.html",{"page_obj":page_obj, "city":city}) 


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})

