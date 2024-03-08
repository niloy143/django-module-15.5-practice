from django.shortcuts import render, redirect
from . import forms, models

def musician(request):
    return render(request, "musician.html")

def create_musician(request):
    form = None

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("home")
    else:
        form = forms.MusicianForm()
    return render(request, "create_musician.html", {'form': form})

def edit_musician(request, id):
    try:
        musician = models.Musician.objects.get(pk=id)

        if request.method == 'POST':
            form = forms.MusicianForm(request.POST, instance=musician)
            form.save()
            return redirect("home")

        form = forms.MusicianForm(instance=musician)
        return render(request, "edit_musician.html", {'form': form, 'musician_id': id})
    except:
        return redirect("home")

def delete_musician(request, id):
    try:
        musician = models.Musician.objects.get(pk=id)
        musician.delete()
    finally:
        return redirect("home")