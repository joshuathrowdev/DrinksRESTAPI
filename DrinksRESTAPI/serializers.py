from rest_framework import serializers

from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
  # Linked Model Class for Model Serializer
  class Meta:
    model = Drink # Linked Model
    fields = ['id', 'name', 'description'] # Fields that we are serializing