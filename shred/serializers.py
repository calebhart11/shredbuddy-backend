from .models import Session
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Session Serializer
class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #the model to serialize
        model = Session
        # fields to include in serialized output
        fields = ['id', 'date', 'mountain', 'goals']
        