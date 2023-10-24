from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Concert(models.Model):
    concert_name = models.CharField(max_length=255)  # Field for concert name, limited to 255 characters
    duration = models.IntegerField() 
    city = models.CharField(max_length=255)  # Field for city, limited to 255 characters
    date = models.DateField(default=datetime.now) 

    def __str__(self):
        return self.concert_name


class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendee"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending


class Photo(models.Model):
    id =  models.IntegerField(primary_key=True) # Explicitly defining id field as AutoField for the primary key
    pic_url = models.CharField(max_length=1000)  # Field for the URL of the photo, limited to 1000 characters
    event_country = models.CharField(max_length=255)  # Field for event country, limited to 255 characters
    event_state = models.CharField(max_length=255)  # Field for event state, limited to 255 characters
    event_city = models.CharField(max_length=255)  # Field for event city, limited to 255 characters
    event_date = models.DateField(default=datetime.now)  # Field for event date, stores date in YYYY-MM-DD format

    class Meta:
        managed = False

    def __str__(self):
        return self.pic_url


class Song(models.Model):
    id =  models.IntegerField(primary_key=True)  # Explicitly defining id field as AutoField for the primary key
    title = models.CharField(max_length=255)  # Field for the title of the song, limited to 255 characters
    lyrics = models.TextField()  # Field for the lyrics of the song, can store large text

    class Meta:
        managed = False

    def __str__(self):
        return self.title
