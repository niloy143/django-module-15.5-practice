from django.shortcuts import render
from album import models

def home(request):
    albums = models.Album.objects.all()
    return render(request, "home.html", {'albums': albums})
