from rest_framework.generics import RetrieveAPIView, ListAPIView
from Adress.api import serializers
from Adress import models
from rest_framework.response import Response

class AdressViewList(ListAPIView):
    serializer_class = serializers.AdressSerializer
    
    def get_queryset(self):
        cep = self.kwargs['cep']
        adress = models.Adress.objects.filter(cep=cep)
        return adress    

 