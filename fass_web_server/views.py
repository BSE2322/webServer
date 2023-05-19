from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

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
    permission_classes = [AllowAny]
    filterset_fields = ['id', 'time', 'location', 'device_id', 'event_type', 'sound_file', 'device']

    @action(methods=["GET"], detail=False)
    def get_yearly_deforestation_rate(self, request):
        year = request.GET["year"]
        # get all events for the specified year
        return Response({
            "data": [
                {"month": "January", "number": "10"},
                {"month": "February", "number": "183"},
                {"month": "March", "number": "4"},
                {"month": "April", "number": "45"},
                {"month": "May", "number": "60"},
                {"month": "June", "number": "80"},
                {"month": "July", "number": "80"},
                {"month": "August", "number": "120"},
                {"month": "September", "number": "70"},
                {"month": "October", "number": "180"},
                {"month": "November", "number": "300"},
                {"month": "December", "number": "200"}
            ]
        }, status=status.HTTP_200_OK)




class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['id', 'name', 'model', 'location', 'forest', 'events']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['id', 'phonenumber']


class NoificationViewSet(viewsets.ModelViewSet):
    queryset = Noification.objects.all()
    serializer_class = NoificationSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['id', 'content', 'timesta'
                                         'mp']
