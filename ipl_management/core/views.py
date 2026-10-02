from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.

from .models import Team

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

# Teams view
def teams_view(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})

from .models import Player

# Players view
def players_view(request):
    players = Player.objects.select_related('team')
    return render(request, 'players.html', {'players': players})

#Points view
from .models import PointsTable

def points_view(request):
    points = PointsTable.objects.select_related('team').order_by('-points')
    return render(request, 'points.html', {'points': points})

