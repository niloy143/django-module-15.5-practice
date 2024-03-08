from django.shortcuts import render, redirect
from . import forms, models

def album(request):
    return render(request, "album.html")

def create_album(request):
    form = None

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")
    else:
        form = forms.AlbumForm()
    return render(request, "create_album.html", {'form': form})


def edit_album(request, id):
    try:
        album = models.Album.objects.get(pk=id)

        if request.method == 'POST':
            form = forms.AlbumForm(request.POST, instance=album)
            form.save()
            return redirect("home")

        form = forms.AlbumForm(instance=album)
        return render(request, "edit_album.html", {'form': form})
    except:
        return redirect("home")

def delete_album(request, id):
    try:
        album = models.Album.objects.get(pk=id)
        album.delete()
    finally:
        return redirect("home")