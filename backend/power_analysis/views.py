from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PowerAnalysisSerializer
from .models import PowerAnalysis

# Create your views here.

class PowerAnalysisView(viewsets.ModelViewSet):
    serializer_class = PowerAnalysisSerializer
    queryset = PowerAnalysis.objects.all()
    last = queryset.last()
    print('Hi')
    print(last.calculate_power_analysis())
    # queryset.calculate_power_analysis()