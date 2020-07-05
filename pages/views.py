from django.shortcuts import render
from .models import team, Carousel
from django.http import HttpResponse
# Create your views here.


def index(request):
    teams = team.objects.all().filter(is_published=True)
    context = {
        'teams': teams
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def donars(request):
    return render(request, 'pages/donars.html')