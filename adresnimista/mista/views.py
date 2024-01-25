from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PlaceForm
from .models import Place

def index(request):
    places=Place.objects.filter(user_id=request.user.id)
    return render(request,"index.html",{"places":places})
    
def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})

@login_required   
def add_item(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Místo bylo přidáno")
            form.save()
            return redirect("index")

    else:

        form = PlaceForm()
    return render(request, "add_item.html",{"form": form})

