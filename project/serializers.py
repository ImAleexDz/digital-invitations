from rest_framework import serializers
from .models import Family, Confirmation

class FamilySerializers(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('id', 'name', 'tickets')

class ConfirmationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Confirmation
        fields = ('id', 'name', 'tickets', 'confirm', 'message')

