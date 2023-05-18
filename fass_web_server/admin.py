from django.contrib import admin

from .models import Device, Event, Noification, User

admin.site.register(Event)
admin.site.register(Device)
admin.site.register(User)
admin.site.register(Noification)
