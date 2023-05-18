from rest_framework import viewsets

from .models import Device, Event, Noification, User
from .serializers import (
    DeviceSerializer,
    EventSerializer,
    NoificationSerializer,
    UserSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []
    filterset_fields = ['id', 'time', 'location', 'device_id', 'event_type', 'sound_file', 'device']


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'model', 'location', 'forest', 'events']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
    filterset_fields = ['id', 'phonenumber']


class NoificationViewSet(viewsets.ModelViewSet):
    queryset = Noification.objects.all()
    serializer_class = NoificationSerializer
    permission_classes = []
    filterset_fields = ['id', 'content', 'timestamp']
