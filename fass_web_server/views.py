from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from project.settings import db
from fass_web_server.expoPushNotifications import send_push_message
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # save data to firebase and send out a push notification
        doc_ref = db.collection("logs").document(str(serializer.data.get("id")))
        doc_ref.set({
            "date": serializer.data.get("time"),
            "location": "4,4",
            "status": serializer.data.get("status")
        })
        send_push_message({
            "to": "ExponentPushToken[yMArsZDum9xLacf6Gtk28y]",
            "title": "Tree Cutting",
            "body": "Click here to see where tree cutting is happening",
            "data": {
                "longitude": 0.33,
                "latitude": 32.57,
                "forestName": "Makerere Forest"
            }
        })
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
