from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    sex = serializers.CharField()
