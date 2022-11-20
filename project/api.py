from .models import Family, Confirmation
from rest_framework import viewsets, permissions
from .serializers import FamilySerializers, ConfirmationSerializers

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FamilySerializers

class ConfirmationViewSet(viewsets.ModelViewSet):
    queryset = Confirmation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConfirmationSerializers