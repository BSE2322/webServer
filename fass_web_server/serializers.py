from rest_framework import serializers

from .models import Device, Event, Noification, User


class EventSerializer(serializers.ModelSerializer):
    device = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(),
    )

    class Meta:
        model = Event
        fields = ['id', 'time', 'location', 'device_id', 'event_type', 'sound_file', 'device']


class DeviceSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Event.objects.all(),
        required=False
    )

    class Meta:
        model = Device
        fields = ['id', 'name', 'model', 'location', 'forest', 'events']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phonenumber']


class NoificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noification
        fields = ['id', 'content', 'timestamp']
