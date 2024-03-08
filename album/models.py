from django.db import models
from django.utils import timezone
from musician.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the album name")
    release_date = models.DateField(default=timezone.now, help_text="Enter the release date of the album")
    rating = models.IntegerField(default=5, choices=((1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5")), help_text="Enter the ratings of the album")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"