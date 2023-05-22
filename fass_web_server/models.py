from django.db import models
from django.utils import timezone


class Event(models.Model):

    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=True, blank=True, default=timezone.now)
    location = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, blank=True)
    event_type = models.CharField(max_length=255, null=True, blank=True)
    sound_file = models.CharField(max_length=255, null=True, blank=True)
    device = models.ForeignKey('Device', on_delete=models.CASCADE, related_name='events')

    class Meta:
        db_table = "event"


class Device(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    forest = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "device"


class User(models.Model):

    id = models.AutoField(primary_key=True)
    phonenumber = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "user"


class Noification(models.Model):

    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True, default=timezone.now)

    class Meta:
        db_table = "noification"
