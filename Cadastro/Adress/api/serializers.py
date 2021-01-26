from rest_framework import serializers
from Adress import models

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adress
        fields = '__all__'

