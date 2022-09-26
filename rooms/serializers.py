from cgi import print_exception
from unicodedata import name
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Room

class RoomSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()
    
    class Meta:
        model = Room
        fields = ("name", "address", "price", "user")