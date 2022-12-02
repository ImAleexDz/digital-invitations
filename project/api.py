from .models import Family, Confirmation
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import FamilySerializers, ConfirmationSerializers
from django.shortcuts import get_object_or_404

class FamilyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = FamilySerializers

    def list(self, request):
        queryset = Family.objects.all()
        serializer = FamilySerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Family.objects.all()
        family = get_object_or_404(queryset, pk=pk)
        serializer = FamilySerializers(family)
        return Response(serializer.data)

    
    def create(self, request, pk=None):
        family = Family()
        fam_serializer = FamilySerializers(data=request.data, context=request.data)

        if fam_serializer.is_valid():
            
            family.name = fam_serializer.validated_data['name']
            family.tickets = fam_serializer.validated_data['tickets']
            family.save()
            return Response({'Mensaje': 'Se ha creado con éxito'})

        else:
            print(fam_serializer.errors)
            return Response(fam_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ConfirmationViewSet(viewsets.ModelViewSet):
    queryset = Confirmation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConfirmationSerializers