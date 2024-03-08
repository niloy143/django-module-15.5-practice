from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50, help_text="Enter the musicians first name")
    last_name = models.CharField(max_length=50, help_text="Enter the musicians last name")
    email = models.EmailField(help_text="Enter the musicians email address")
    phone = models.CharField(max_length=11, help_text="Enter the musicians phone number")
    instrument_type = models.CharField(max_length=100, help_text="Enter the instrument type")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"