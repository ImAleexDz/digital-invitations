from rest_framework import serializers
from .models import Family, Confirmation, Bf_Family, Friends

class FamilySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    tickets = serializers.IntegerField()

    class Meta:
        model = Family
        fields = ('id', 'name', 'tickets')

    def validate_name(self, value):
        if value == '':
            raise serializers.ValidationError("Error")
        return value

    def validate_tickets(self, value):
        if value < 0:
            raise serializers.ValidationError("No puede haber números negativos")
        return value

    def validate(self, data):
        print('General validation')
        return data

class Bf_FamilySerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    tickets = serializers.IntegerField()

    class Meta:
        model = Bf_Family
        fields = ('id', 'name', 'tickets')

    def validate_name(self, value):
        if value == '':
            raise serializers.ValidationError("Error")
        return value

    def validate_tickets(self, value):
        if value < 0:
            raise serializers.ValidationError("No puede haber números negativos")
        return value

    def validate(self, data):
        print('General validation')
        return data

class FriendsSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    tickets = serializers.IntegerField()

    class Meta:
        model = Friends
        fields = ('id', 'name', 'tickets')

    def validate_name(self, value):
        if value == '':
            raise serializers.ValidationError("Error")
        return value

    def validate_tickets(self, value):
        if value < 0:
            raise serializers.ValidationError("No puede haber números negativos")
        return value

    def validate(self, data):
        print('General validation')
        return data

class ConfirmationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Confirmation
        fields = ('id', 'name', 'tickets', 'confirm', 'message')

