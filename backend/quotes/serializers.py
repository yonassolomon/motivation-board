from rest_framework import serializers
from .models import Quote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class QuoteSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Quote
        fields=['id','user','text','author','created_at']        