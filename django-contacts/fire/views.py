from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def home(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

def goodbye(request):
    return HttpResponse("See you soon")