from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework import viewsets
from API.serializers import TargetSerializer

from API.models import TargetData

class TargetDataViewSet(viewsets.ModelViewSet):
    """
    Post to this one to add target data
    """
    queryset = TargetData.objects.all().order_by('id')
    serializer_class = TargetSerializer