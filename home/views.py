from django.shortcuts import render
from .models import Contact

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        message = request.POST.get('message', 'default')

        en = Contact(name=name, email=email, message=message)
        en.save()

    return render(request, 'Home.html')


def about(request):
    return render(request, 'About.html')


def team(request):
    return render(request, 'Team.html')


def lets(request):
    return render(request, 'lets.html')
